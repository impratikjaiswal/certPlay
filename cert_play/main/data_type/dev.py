from cert_play.main.data_type.data_type_master import DataTypeMaster
from cert_play.main.helper.data import Data


class Dev(DataTypeMaster):

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

    def set_data_pool(self):
        data_pool = [
            # TODO: Need to Fix
            Data(
                remarks='Folder',
                input_data=r'D:\Other\Github_Self\euiccSpecs\GSMA\SGP.26 RSP Test Certificates\certs\SGP.26_v1.2_files',
            ),
        ]
        super().set_data_pool(data_pool)
