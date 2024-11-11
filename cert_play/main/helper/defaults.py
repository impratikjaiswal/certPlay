from python_helpers.ph_defaults import PhDefaults
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes

from cert_play.main.helper.formats import Formats


class Defaults:
    PRINT_INFO = PhDefaults.PRINT_INFO
    PRINT_INPUT = PhDefaults.PRINT_INPUT
    PRINT_OUTPUT = PhDefaults.PRINT_OUTPUT
    ARCHIVE_OUTPUT = PhDefaults.ARCHIVE_OUTPUT
    QUITE_MODE = PhDefaults.QUITE_MODE
    EXECUTION_MODE = PhExecutionModes.USER
    ERROR_HANDLING_MODE = PhErrorHandlingModes.CONTINUE_ON_ERROR
    ENCODING = PhDefaults.CHAR_ENCODING
    ENCODING_ERRORS = PhDefaults.ENCODING_ERRORS
    ARCHIVE_OUTPUT_FORMAT = PhDefaults.ARCHIVE_OUTPUT_FORMAT
    #
    URL_TIME_OUT = 5
    URL_PRE_ACCESS = True
    URL_CERT_FETCH_ONLY = False
    URL_ALL_CERTS = False
    FORMAT_INPUT = Formats.URL
