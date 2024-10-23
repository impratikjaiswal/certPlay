from cert_play.main.data_type.data_type_master import DataTypeMaster
from cert_play.main.helper.data import Data
from cert_play.main.helper.formats import Formats


class UserData(DataTypeMaster):

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_quiet_mode(self):
        quite_mode = None
        super().set_quiet_mode(quite_mode)

    def set_remarks(self):
        remarks = None
        super().set_remarks(remarks)

    def set_input_format(self):
        input_format = None
        super().set_input_format(input_format)

    def set_url_time_out(self):
        url_time_out = None
        super().set_url_time_out(url_time_out)

    def set_url_pre_access(self):
        url_pre_access = None
        super().set_url_pre_access(url_pre_access)

    def set_url_cert_fetch_only(self):
        url_cert_fetch_only = None
        super().set_url_cert_fetch_only(url_cert_fetch_only)

    def set_url_all_certs(self):
        url_all_certs = None
        super().set_url_all_certs(url_all_certs)

    def set_data_pool(self):
        data_pool = [
            #
            Data(
                remarks='Url; AmenityPj',
                input_data='amenitypj.in',
                input_format=Formats.URL,
            ),
            #
        ]
        super().set_data_pool(data_pool)
