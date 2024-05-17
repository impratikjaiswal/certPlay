from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes

from cert_play.main.helper.formats import Formats


class Defaults:
    TIME_OUT_IN_SECONDS = 5
    PRINT_INFO = True
    PRINT_INPUT = True
    PRINT_OUTPUT = True
    QUITE_MODE = False
    EXECUTION_MODE = PhExecutionModes.USER
    ERROR_HANDLING_MODE = PhErrorHandlingModes.CONTINUE_ON_ERROR
    INPUT_FORMAT = Formats.URL
