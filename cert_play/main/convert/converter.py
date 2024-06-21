import re

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from cert_play.main.convert.util import to_str, is_url_accessible
from cert_play.main.helper.data import Data
from cert_play.main.helper.defaults import Defaults
from cert_play.main.helper.formats import Formats


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
                get_dic_data_and_print(PhKeys.REMARKS, PhConstants.SEPERATOR_ONE_LINE, remarks_original))
        if remarks_generated:
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.REMARKS_GENERATED, PhConstants.SEPERATOR_ONE_LINE,
                                       remarks_generated))
        info = PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, [
            get_dic_data_and_print(PhKeys.TRANSACTION_ID, PhConstants.SEPERATOR_ONE_LINE, meta_data.transaction_id,
                                   dic_format=False, print_also=False),
            get_dic_data_and_print(PhKeys.INPUT_FORMAT, PhConstants.SEPERATOR_ONE_LINE, data.input_format,
                                   dic_format=False, print_also=False),
            get_dic_data_and_print(PhKeys.URL_TIME_OUT, PhConstants.SEPERATOR_ONE_LINE, data.url_time_out,
                                   dic_format=False, print_also=False) if data.input_format == Formats.URL else None,
            get_dic_data_and_print(PhKeys.URL_PRE_ACCESS, PhConstants.SEPERATOR_ONE_LINE, data.url_pre_access,
                                   dic_format=False, print_also=False) if data.input_format == Formats.URL else None,
            get_dic_data_and_print(PhKeys.QUITE_MODE, PhConstants.SEPERATOR_ONE_LINE, data.quite_mode,
                                   dic_format=False, print_also=False) if data.quite_mode else None,
        ]))
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INFO, PhConstants.SEPERATOR_INFO, info))
    if data.print_input:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INPUT_DATA, input_sep, meta_data.input_data_org))
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
    if data.input_format is None:
        data.input_format = Defaults.FORMAT_INPUT
    if data.url_time_out is None:
        data.url_time_out = Defaults.URL_TIME_OUT
    if data.url_pre_access is None:
        data.url_pre_access = Defaults.URL_PRE_ACCESS


def read_web_request(request_form):
    return Data(**parse_config(request_form))


def clean_der_data(input_data):
    """

    :return:
    """
    input_data_list = input_data.split('\n')
    if len(input_data_list) > 1:
        # Multi Line
        if PhConstants.CERTIFICATE in input_data_list[0]:
            input_data_list[0] = ''
        if PhConstants.CERTIFICATE in input_data_list[-1]:
            input_data_list[-1] = ''
    else:
        # Single Line
        # Cleaning of ----------, -----END CERTIFICATE----- from same line data
        input_data_list = re.sub(r'[- ]*(BEGIN|END) CERTIFICATE[- ]*', '', input_data_list[0])
    # Strip All Lines
    input_data_list = [str(x).strip() for x in input_data_list]
    single_line_data = ''.join(filter(None, input_data_list))
    single_line_data = PhUtil.decode_to_base64_if_hex(single_line_data)
    return '\n'.join([PhConstants.BEGIN_CERTIFICATE, single_line_data, PhConstants.END_CERTIFICATE])


def clean_and_pre_access_url_data(input_data, pre_access=True):
    """

    :return:
    """
    # compare_urlparse_urlsplit(input_data)
    schema, url, port = clean_url(input_data)
    if pre_access:
        if not schema:
            print(f'URL Type is missing (e.g.: http, https etc), hence {input_data} accessibility can not be validated')
        else:
            is_url_accessible('://'.join(filter(None, [schema, url])), fail_safe=False)
    return ':'.join(filter(None, [url, port]))


def clean_url(input_data):
    input_data = to_str(input_data)
    if input_data is None:
        raise ValueError('Invalid input_data')
    # urlsplit_data = urllib.parse.urlsplit(input_data)
    # print(f'input_data: {input_data}; urlsplit_data: {urlsplit_data}')
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
    # input_data = 'f{urlsplit_data.scheme}'
    if not url:
        result = input_data
        schema = ''
        # remove www., if any
        if result.startswith('www.'):
            result = result.replace('www.', '', 1)
        # remove Schemas, is any
        sep = '://' if '://' in result else '//'
        results = result.split(sep, maxsplit=1)
        if len(results) > 1:
            schema = results[0]
            result = results[1]
        else:
            result = result
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
    # print(f'schema: {schema}; url: {url}; port: {port}')
    # Trim the url for fetching certificate
    return schema, url, port
