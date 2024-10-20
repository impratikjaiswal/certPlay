import os

from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from cert_play.main.convert import converter
from cert_play.main.convert.handler import process_data
from cert_play.main.helper.formats_group import FormatsGroup
from cert_play.main.helper.metadata import MetaData


def parse_or_update_any_data(data, meta_data=None):
    """

    :param meta_data:
    :param data:
    :return:
    """
    """
    Bulk Data Handling (Recursive)
    """
    converter.set_defaults_for_printing(data)
    byte_array_format = False
    if meta_data is None:
        meta_data = MetaData(input_data_org=data.input_data)
    if not byte_array_format and isinstance(data.input_data, list):
        # List is provided
        meta_data.input_mode_key = PhKeys.INPUT_LIST
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
    if not byte_array_format and data.input_data and os.path.isdir(os.path.abspath(data.input_data)):
        # directory is provided
        meta_data.input_mode_key = PhKeys.INPUT_DIR
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
        PhUtil.print_heading(data.get_remarks_as_str(), heading_level=3)
        converter.print_data(data, meta_data)
        converter.set_includes_excludes_files(data, meta_data)
        files_list = PhUtil.traverse_it(top=os.path.abspath(data.input_data), traverse_mode='Regex',
                                        include_files=meta_data.include_files, excludes=meta_data.excludes)
        if files_list:
            files_list_data = data
            files_list_data.input_data = files_list
            return parse_or_update_any_data(files_list_data)
    """
    Individual File Handling
    """
    file_dic_all_str = {}
    data.set_auto_generated_remarks_if_needed()
    PhUtil.print_heading(data.get_remarks_as_str(), heading_level=2)
    if not byte_array_format and data.input_data and os.path.isfile(data.input_data):
        # file is provided
        try:
            with open(data.input_data, 'r') as the_file:
                resp = ''.join(the_file.readlines())
        except UnicodeDecodeError:
            # Binary File
            with open(data.input_data, 'rb') as the_file:
                resp = the_file.read()
        if not resp:
            raise ValueError(PhExceptionHelper(msg_key=Constants.INPUT_FILE_EMPTY))
        file_ext = PhUtil.get_file_name_and_extn(file_path=data.input_data, only_extn=True)
        if file_ext in FormatsGroup.INPUT_FILE_FORMATS_YML:
            meta_data.input_mode_key = PhKeys.INPUT_YML
            file_dic_all_str, data = converter.read_yaml(resp)
            converter.set_defaults_for_printing(data)
        else:
            meta_data.input_mode_key = PhKeys.INPUT_FILE
            converter.set_input_output_format(data)
            data.input_data = resp
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
    """
    Individual Data Handling
    """
    converter.set_defaults(data, meta_data)
    """
    Data Processing
    """
    meta_data.parsed_data = process_data(data, meta_data)
    converter.print_data(data, meta_data)
