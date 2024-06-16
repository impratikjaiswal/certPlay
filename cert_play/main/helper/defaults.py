from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes

from cert_play.main.helper.formats import Formats


class Defaults:
    PRINT_INFO = True
    PRINT_INPUT = True
    PRINT_OUTPUT = True
    QUITE_MODE = False
    EXECUTION_MODE = PhExecutionModes.USER
    ERROR_HANDLING_MODE = PhErrorHandlingModes.CONTINUE_ON_ERROR
    URL_TIME_OUT = 5
    URL_PRE_ACCESS = True
    FORMAT_INPUT = Formats.URL
