import tempfile

from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_util import PhUtil

from cert_play.main.convert import converter
from cert_play.main.convert.converter import validate_urls, validate_der_format
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
    converter.set_defaults_for_printing(data)
    if meta_data is None:
        meta_data = MetaData(raw_data_org=data.raw_data)
    data.set_auto_generated_remarks_if_needed()
    PhUtil.print_heading(data.get_remarks_as_str(), heading_level=2)
    converter.set_defaults(data, meta_data)
    if data.input_format not in FormatsGroup.INPUT_FORMATS_SUPPORTED:
        # TODO: Move to phConstants
        UNKNOWN_INPUT_FORMAT = 'Unknown input format'
        raise ValueError(
            PhExceptionHelper(msg_key=UNKNOWN_INPUT_FORMAT, msg_value=data.input_format))
    temp_data = data.raw_data
    if data.input_format == Formats.URL:
        temp_data = validate_urls(temp_data)
    if data.input_format == Formats.DER:
        temp_data = validate_der_format(temp_data)
    meta_data.parsed_data = open_ssl_cmd(temp_data, data.input_format)
    converter.print_data(data, meta_data)


def open_ssl_cmd_step_1(raw_data):
    nul_windows = 'NUL'
    nul_unix = '/dev/null'
    nul_handling = nul_windows if is_windows_environment() else nul_unix
    cmd = ' '.join(
        [
            "openssl s_client -connect",
            raw_data,
            "2>&1 < ",
            nul_handling,
            "| sed -n '/-----BEGIN/,/-----END/p'"
        ]
    )
    result = execute_cmd(cmd)
    if not result:
        raise ValueError(f'URL {raw_data} is not accessible. Please try a different URL.')
    return result


def open_ssl_cmd(raw_data, input_format):
    """

    :param raw_data:
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
        if input_format == Formats.URL:
            result = open_ssl_cmd_step_1(raw_data)
        if input_format == Formats.DER:
            result = raw_data
        fp1.write(result)
        fp1.close()
        with open(fp1.name, mode='r') as fp2:
            cmd = ' '.join(["openssl x509 -in", fp1.name, '-text'])
            result = execute_cmd(cmd)
            fp2.close()
    return result
