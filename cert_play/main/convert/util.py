import os
import platform
import subprocess
import urllib
from urllib.error import HTTPError

import sys
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_util import PhUtil


def is_url_accessible(url, fail_safe=False):
    try:
        urllib.request.urlopen(url)
        return True
    except HTTPError as e:
        if fail_safe is True:
            return False
        raise ValueError(f'URL {url} is not accessible. {e}.')
    except Exception as e:
        if fail_safe is True:
            return False
        raise ValueError(f'URL {url} is not accessible. Please try a different URL.')


def to_str(input_data, fail_safe=True):
    default_return = PhConstants.STR_EMPTY if fail_safe else None
    if not input_data or input_data is None:
        return default_return
    input_data = str(input_data).strip()
    input_data = input_data.strip()
    return input_data if input_data else default_return


def is_windows_environment():
    return True if get_os_name().startswith('win') else False


def is_unix_environment():
    """
    Behaviour of Unix & Mac remains similar
    :return:
    """
    return not is_windows_environment()


def get_os_name(detailed_output=False):
    """

    :return:
    """
    if detailed_output:
        """
        For Linux: 'posix'
        For Mac: 'posix'
        For Windows: 'nt'
        For Cygwin: 'nt'
        #
        # could be ''
        """
        print(f'os.name is {os.name}')

        """
        For Linux: 'linux' / 'linux2' / 'linux3'
        For Mac: 'darwin'
        For Windows: 'win32'
        For Cygwin: 'cygwin'
        #
        # could be 'freebsd8'
        """
        print(f'sys.platform is {sys.platform}')

        """
        For Linux: 'Linux'
        For Mac: 'Darwin'
        For Windows: 'Windows'
        """
        print(f'platform.system() is {platform.system()}')

        """
        For Linux: '2.6.22-15-generic'
        For Mac: '19.2.0'
        For Windows: '10' / 'Vista' / '7'
        """
        print(f'platform.release() is {platform.release()}')

        """
        For Linux: 'Linux-3.3.0-8.fc16.x86_64-x86_64-with-fedora-16-Verne'
        For Mac: '19.2.0'
        For Windows: 'Windows-10-10.0.19045-SP0'
        """
        print(f'platform.platform() is {platform.platform()}')
    return sys.platform


def execute_cmd(cmd, time_out=None):
    """

    :param time_out:
    :param cmd:
    :return:
    """
    PhUtil.print_heading(str_heading=cmd)
    # This command will print the output directly to the console.
    # os.system(cmd)
    result = subprocess.run(cmd, shell=True, capture_output=True, timeout=time_out)
    # Positive Case
    if result.stdout:
        return result.stdout.decode(PhConstants.CHAR_ENCODING_UTF8)
    # Error Case
    if result.stderr:
        # Sample Data b'Could not find certificate from C:\Users\impra\AppData\Local\Temp\tmpo0egstjt\r\n ...'
        error_data = result.stderr.decode(PhConstants.CHAR_ENCODING_UTF8).split('\r\n')[0]
        raise subprocess.CalledProcessError(returncode=result.returncode, cmd=result.args, stderr=error_data)
    return None
