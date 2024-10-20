import tempfile

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper

from cert_play.main.convert.converter import clean_and_pre_access_url_data, clean_der_data
from cert_play.main.convert.util import is_windows_environment, execute_cmd
from cert_play.main.helper.formats import Formats
from cert_play.main.helper.formats_group import FormatsGroup

_debug = False


# Enable Flag for Debugging
# _debug = True


def process_data(data, meta_data, flip_output=False):
    """

    :param data:
    :param meta_data:
    :param flip_output:
    :return:
    """
    if flip_output is True:
        input_data_new = meta_data.parsed_data
        input_format_new = data.output_format
        output_format_new = data.input_format
        data.input_data = input_data_new
        data.input_format = input_format_new
        data.output_format = output_format_new
    if not data.input_data:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.MISSING_INPUT_DATA))
    if data.input_format not in FormatsGroup.INPUT_FORMATS_SUPPORTED:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.UNKNOWN_INPUT_FORMAT, msg_value=data.input_format))
    if data.url_time_out not in FormatsGroup.URL_TIME_OUT_SUPPORTED:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.INVALID_URL_TIME_OUT, msg_value=data.url_time_out))
    if data.input_format == Formats.URL:
        data.input_data = clean_and_pre_access_url_data(data.input_data, data.url_pre_access)
    if data.input_format == Formats.DER:
        data.input_data = clean_der_data(data.input_data)
    meta_data.parsed_data = open_ssl_cmd(data)


def open_ssl_cmd_step_1(input_data, url_time_out):
    nul_windows = 'NUL'
    nul_unix = '/dev/null'
    nul_handling = nul_windows if is_windows_environment() else nul_unix
    cmd = ' '.join(
        [
            "openssl s_client -connect",
            input_data,
            "2>&1 < ",
            nul_handling,
            "| sed -n '/-----BEGIN/,/-----END/p'"
        ]
    )
    result = execute_cmd(cmd, time_out=url_time_out)
    if not result:
        raise ValueError(f'URL {input_data} is not accessible. Please try a different URL.')
    return result


def open_ssl_cmd(data):
    """

    :param input_data:
    :return:
    """

    """
    openssl s_client -connect amenitypj.in:443 2>&1 < /dev/null | sed -n '/-----BEGIN/,/-----END/p' > wikipedia.org.pem.txt
    openssl s_client -connect amenitypj.in:443 2>&1 < NUL       | sed -n '/-----BEGIN/,/-----END/p' > amenitypj.in.pem.txt
    openssl x509 -in amenitypj.in.pem.txt -text -out amenitypj.in.pem_parsed.txt
    """
    # cmd = "dir"
    # execute_cmd(cmd)
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as fp1:
        print(f'Temp File {fp1.name} is created.')
        if data.input_format == Formats.URL:
            result = open_ssl_cmd_step_1(data.input_data, data.url_time_out)
        if data.input_format == Formats.DER:
            result = data.input_data
        fp1.write(result)
        fp1.close()
        with open(fp1.name, mode='r') as fp2:
            cmd = ' '.join(["openssl x509 -in", fp1.name, '-text'])
            result = execute_cmd(cmd)
            fp2.close()
    return result
