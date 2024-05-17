from cert_play.main.data_type.data_type_master import DataTypeMaster
from cert_play.main.helper.data import Data


class AnyData(DataTypeMaster):

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

    def set_input_format(self):
        input_format = None
        super().set_input_format(input_format)

    def set_data_pool(self):
        data_pool = [
            #
            Data(
                remarks_list='AmenityPj; Home Page',
                raw_data='amenitypj.in',
            ),
            #
            Data(
                remarks_list='AmenityPj; www; https;',
                raw_data='https://www.amenitypj.in/',
            ),
            #
            Data(
                remarks_list='AmenityPj; Sub Domain',
                raw_data='beta.amenitypj.in',
            ),
            #
            Data(
                remarks_list='Google',
                raw_data='google.com',
            ),
            #
            Data(
                remarks_list='Google; https; www;',
                raw_data='https://www.google.com/',
            ),
            #
            Data(
                remarks_list='WikiPedia; Sub Pages',
                raw_data='https://en.wikipedia.org/wiki/Main_Page',
            ),
            #
        ]
        super().set_data_pool(data_pool)
