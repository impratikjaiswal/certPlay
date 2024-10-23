import tempfile

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_util import PhUtil

from cert_play.main.convert import converter
from cert_play.main.convert.converter import clean_and_pre_access_url_data, clean_der_data
from cert_play.main.convert.handler import open_ssl_cmd
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


