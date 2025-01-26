from cert_play.main.helper.formats import Formats


class FormatsGroup:
    INPUT_FORMATS_SUPPORTED = [
        Formats.URL,
        Formats.DER,
    ]

    URL_TIME_OUT_SUPPORTED = list(range(10, 0, -1))
