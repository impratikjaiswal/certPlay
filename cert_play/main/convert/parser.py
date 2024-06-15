import tempfile

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_util import PhUtil

from cert_play.main.convert import converter
from cert_play.main.convert.converter import clean_and_pre_access_url_data, clean_der_data
from cert_play.main.convert.util import is_windows_environment, execute_cmd
from cert_play.main.helper.formats import Formats
from cert_play.main.helper.formats_group import FormatsGroup
from cert_play.main.helper.metadata import MetaData


def parse_or_update_any_data(data, meta_data=None):
    """

    :param meta_data:
    :param data:
    :return:
    """
    """
    Individual
    """
    converter.set_defaults_for_printing(data)
    if meta_data is None:
        meta_data = MetaData(input_data_org=data.input_data)
    data.set_auto_generated_remarks_if_needed()
    PhUtil.print_heading(data.get_remarks_as_str(), heading_level=2)
    converter.set_defaults(data, meta_data)
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
    converter.print_data(data, meta_data)


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
