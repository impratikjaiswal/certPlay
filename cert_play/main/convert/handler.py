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


def handle_certs(data, meta_data, info_data):
    if data.input_format == Formats.URL:
        data.input_data = clean_and_pre_access_url_data(data.input_data, data.url_pre_access)
    if data.input_format == Formats.DER:
        data.input_data = clean_der_data(data.input_data)
    return open_ssl_cmd(data)


def process_data(data, meta_data, info_data, flip_output=False):
    """

    :param data:
    :param meta_data:
    :param info_data:
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
    # Handle Certificate
    res = handle_certs(data=data, meta_data=meta_data, info_data=info_data)
    if flip_output is True:
        meta_data.re_parsed_data = res
    else:
        meta_data.parsed_data = res


def open_ssl_cmd_step_1(input_data, url_time_out, url_all_certs):
    nul_windows = 'NUL'
    nul_unix = '/dev/null'
    nul_handling = nul_windows if is_windows_environment() else nul_unix
    all_certs_flag = '-showcerts' if url_all_certs else None
    cmd = ' '.join(filter(None, [
        "openssl s_client -connect",
        input_data,
        all_certs_flag,
        "2>&1 < ",
        nul_handling,
        "| sed -n '/-----BEGIN/,/-----END/p'"
    ]))
    result = execute_cmd(cmd, time_out=url_time_out)
    if not result:
        raise ValueError(f'URL {input_data} is not accessible. Please try a different URL.')
    return result


def open_ssl_cmd_step_2(input_file_name, url_all_certs):
    """

    :param input_file_name:
    :param url_all_certs:
    :return:
    """
    open_ssl_lib = 'storeutl' if url_all_certs else 'x509'
    open_ssl_lib_param = '-certs' if url_all_certs else '-in'
    cmd = ' '.join(filter(None, [
        'openssl',
        open_ssl_lib,
        '-text',
        open_ssl_lib_param,
        input_file_name,

    ]))
    result = execute_cmd(cmd)
    if not result:
        raise ValueError(f'Parsing Failed. Please try again.')
    return result


def open_ssl_cmd(data):
    """

    :param input_data:
    :return:
    """

    """
    ***** Step 1:
    ***** *****  Unix:
    openssl s_client -connect amenitypj.in:443 2>&1 < /dev/null | sed -n '/-----BEGIN/,/-----END/p' > wikipedia.org.pem.txt
    ***** ***** Windows:
    openssl s_client -connect amenitypj.in:443 2>&1 < NUL | sed -n '/-----BEGIN/,/-----END/p' > amenitypj.in.pem.txt
    ***** ***** All Certs:
    openssl s_client -connect amenitypj.in:443 -showcerts 2>&1 < NUL | sed -n '/-----BEGIN/,/-----END/p' > amenitypj.in.bundle.pem.txt
    
    ***** Step 2:
    openssl x509 -text -out amenitypj.in.pem_parsed.txt -in amenitypj.in.pem.txt
    openssl storeutl -text -out amenitypj.in.bundle.pem_parsed.txt -certs amenitypj.in.bundle.pem.txt
    """
    # cmd = "dir"
    # execute_cmd(cmd)
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as fp1:
        print(f'Temp File {fp1.name} is created.')
        if data.input_format == Formats.URL:
            result = open_ssl_cmd_step_1(data.input_data, data.url_time_out, data.url_all_certs)
        if data.input_format == Formats.DER:
            result = data.input_data
        fp1.write(result)
        fp1.close()
        if data.url_cert_fetch_only:
            return result
        with open(fp1.name, mode='r') as fp2:
            result = open_ssl_cmd_step_2(fp1.name, data.url_all_certs)
            fp2.close()
    return result
