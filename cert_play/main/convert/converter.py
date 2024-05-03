import urllib

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from cert_play.main.convert.util import to_str
from cert_play.main.helper.data import Data
from cert_play.main.helper.defaults import Defaults


def print_data(data, meta_data):
    if data.quite_mode:
        return
    input_sep = PhConstants.SEPERATOR_ONE_LINE
    output_sep = PhConstants.SEPERATOR_MULTI_LINE
    if data.print_info:
        remarks_original = data.get_remarks_as_str(user_original_remarks=True)
        remarks_generated = data.get_remarks_as_str()
        remarks_generated_stripping_needed = True if remarks_generated.endswith(
            PhConstants.DEFAULT_TRIM_STRING) else False
        if remarks_original:
            if remarks_generated_stripping_needed:
                if remarks_generated.strip(PhConstants.DEFAULT_TRIM_STRING) in remarks_original:
                    remarks_generated = ''
            else:
                if remarks_original in remarks_generated:
                    remarks_generated = ''
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.REMARKS_LIST, PhConstants.SEPERATOR_ONE_LINE, remarks_original))
        if remarks_generated:
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.REMARKS_LIST_GENERATED, PhConstants.SEPERATOR_ONE_LINE,
                                       remarks_generated))
        info = PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, [
            get_dic_data_and_print(PhKeys.QUITE_MODE, PhConstants.SEPERATOR_ONE_LINE, data.quite_mode,
                                   dic_format=False, print_also=False) if data.quite_mode else None,
        ]))
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INFO, PhConstants.SEPERATOR_INFO, info))
    if data.print_input:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INPUT_DATA, input_sep, data.raw_data))
    print_output = data.print_output
    if data.print_output and print_output:  # and meta_data.parsed_data:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.OUTPUT_DATA, output_sep, meta_data.parsed_data))
    PhUtil.print_separator()


def get_dic_data_and_print(key, sep, value, dic_format=True, print_also=True):
    return PhUtil.get_key_value_pair(key=key, value=value, sep=sep, dic_format=dic_format, print_also=print_also)


def parse_config(config_data):
    # PhUtil.print_iter(config_data, 'config_data initial', verbose=True)
    for k, v in config_data.items():
        if v:
            # Trim Garbage data
            v = PhUtil.trim_white_spaces_in_str(v)
            if v in ['None']:
                v = None
                config_data[k] = v
            if v in [PhConstants.STR_SELECT_OPTION]:
                v = None
                config_data[k] = v
            if v in ['True']:
                v = True
                config_data[k] = v
            if v in ['False']:
                v = False
                config_data[k] = v
        if not v:
            continue
        config_data[k] = v
    # PhUtil.print_iter(config_data, 'config_data processed', verbose=True, depth_level=1)
    return config_data


def set_defaults_for_printing(data):
    if data.quite_mode is None:
        data.quite_mode = Defaults.QUITE_MODE
    if data.print_input is None:
        data.print_input = Defaults.PRINT_INPUT
    if data.print_output is None:
        data.print_output = Defaults.PRINT_OUTPUT
    if data.print_info is None:
        data.print_info = Defaults.PRINT_INFO


def set_defaults(data, meta_data):
    """
    Set Default Values if nothing is set
    :param data:
    :param meta_data:
    :return:
    """
    pass


def read_web_request(request_form):
    return Data(**parse_config(request_form))


def validate_urls(raw_data):
    """

    :return:
    """
    # compare_urlparse_urlsplit(raw_data)
    url_w_port = clean_url(raw_data)
    return url_w_port


def clean_url(raw_data):
    raw_data = to_str(raw_data)
    if raw_data is None:
        raise ValueError('Invalid raw_data')
    # urlsplit_data = urllib.parse.urlsplit(raw_data)
    # print(f'raw_data: {raw_data}; urlsplit_data: {urlsplit_data}')
    url = ''
    port = ''
    # if urlsplit_data.netloc:
    #     # netloc is available
    #     results = str(urlsplit_data.netloc).split(':', maxsplit=1)
    #     url = results[0]
    #     port = results[1] if len(results) > 1 else 'XXX'

    # joint_data = []
    # # https://github.com/django/django/blob/main/django/core/validators.py#L74
    # if urlsplit_data.scheme:
    #     joint_data.append(f'urlsplit_data.scheme')
    # raw_data = 'f{urlsplit_data.scheme}'
    if not url:
        result = raw_data
        # remove www., if any
        if result.startswith('www.'):
            result = result.replace('www.', '', 1)
        # remove Schemas, is any
        sep = '://' if '://' in result else '//'
        results = result.split(sep, maxsplit=1)
        result = results[1] if len(results) > 1 else result
        # remove Fragment, if any
        results = result.split('#', maxsplit=1)
        result = results[0]
        # remove Query, if any
        results = result.split('?', maxsplit=1)
        result = results[0]
        # Split Url & Port, if any
        results = result.split(':', maxsplit=1)
        url = results[0]
        port = results[1] if len(results) > 1 else ''
        # remove path from url, if any
        results = url.split('/', maxsplit=1)
        url = results[0]
        # remove path from port, if any
        results = port.split('/', maxsplit=1)
        port = results[0]
        # port must be numeric
        port = port if port and PhUtil.is_numeric(port) else '443'
    print(f'url: {url}; port: {port}')
    # Trim the url for fetching certificate
    return ':'.join([url, port])