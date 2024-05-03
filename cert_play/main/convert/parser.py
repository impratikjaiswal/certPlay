import subprocess
import tempfile

from python_helpers.ph_util import PhUtil

from cert_play.main.convert import converter
from cert_play.main.convert.converter import validate_urls
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
    meta_data.parsed_data = open_ssl_cmd(validate_urls(data.raw_data))
    converter.print_data(data, meta_data)


def open_ssl_cmd(raw_data):
    """

    :param raw_data:
    :return:
    """

    """
    openssl s_client -connect amenitypj.in:443 2>&1 < NUL | sed -n '/-----BEGIN/,/-----END/p' > amenitypj.in.pem.txt
    openssl x509 -in amenitypj.in.pem.txt -text -out amenitypj.in.pem_parsed.txt
    """
    # cmd = "dir"
    # execute_cmd(cmd)
    # Move File to Temp Folder
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as fp:
        print(f'Temp File {fp.name} is created.')
        cmd = ' '.join(["openssl s_client -connect", raw_data, "2>&1 < NUL | sed -n '/-----BEGIN/,/-----END/p'"])
        result = execute_cmd(cmd)
        fp.write(result)
        fp.close()
        with open(fp.name, mode='r') as f:
            cmd = ' '.join(["openssl x509 -in", fp.name, '-text'])
            result = execute_cmd(cmd)
            fp.close()
    return result


def execute_cmd(cmd):
    """

    :param cmd:
    :return:
    """
    PhUtil.print_heading(str_heading=cmd)
    # This command will print the output directly to the console.
    # os.system(cmd)
    try:
        result = subprocess.check_output(cmd, shell=True, text=True)
    except subprocess.CalledProcessError as e:
        result = f"Error executing command: {e}"
    # print(result)
    return result
