from cert_play.main.data_type.data_type_master import DataTypeMaster
from cert_play.main.helper.data import Data


class UnitTesting(DataTypeMaster):

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

    def set_remarks_list(self):
        remarks_list = None
        super().set_remarks_list(remarks_list)

    def set_data_pool(self):
        data_pool_positive = [
            #
        ]
        data_pool_negative = [
            #
            Data(
                remarks_list='WikiPedia; Sub Pages',
                raw_data='https://amenitypj.com',
            ),
        ]
        super().set_data_pool(data_pool_positive + data_pool_negative)
