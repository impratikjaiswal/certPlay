from cert_play.main.data_type.data_type_master import DataTypeMaster
from cert_play.main.helper.data import Data
from cert_play.main.helper.formats import Formats


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

    def set_remarks_list(self):
        remarks_list = None
        super().set_remarks_list(remarks_list)

    def set_input_format(self):
        input_format = None
        super().set_input_format(input_format)

    def set_data_pool(self):
        data_pool = [
            # TODO
            Data(
                remarks_list='Begin & End in same line',
                raw_data=r"""-----BEGIN CERTIFICATE-----MIIISzCCB9GgAwIBAgIQB0GeOVg6THbPHqFDR/pfOjAKBggqhkjOPQQDAzBWMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMTAwLgYDVQQDEydEaWdpQ2VydCBUTFMgSHlicmlkIEVDQyBTSEEzODQgMjAyMCBDQTEwHhcNMjMxMDE4MDAwMDAwWhcNMjQxMDE2MjM1OTU5WjB5MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNU2FuIEZyYW5jaXNjbzEjMCEGA1UEChMaV2lraW1lZGlhIEZvdW5kYXRpb24sIEluYy4xGDAWBgNVBAMMDyoud2lraXBlZGlhLm9yZzBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABDVh9CEa/2rEO/oGR8YZbr5wOPHcFrG8OBQS1BQrHAsxgVn1Z/bnKtE8Hvqup+0GXdZvXYlMa8iw4A+Dz/XTitqjggZcMIIGWDAfBgNVHSMEGDAWgBQKvAgpF4ylOW16Ds4zxy6z7fvDejAdBgNVHQ4EFgQUyqwMZ6LjhkM/u0PnQdmhhzp43TMwggLtBgNVHREEggLkMIIC4IIPKi53aWtpcGVkaWEub3Jngg13aWtpbWVkaWEub3Jngg1tZWRpYXdpa2kub3Jngg13aWtpYm9va3Mub3Jnggx3aWtpZGF0YS5vcmeCDHdpa2luZXdzLm9yZ4INd2lraXF1b3RlLm9yZ4IOd2lraXNvdXJjZS5vcmeCD3dpa2l2ZXJzaXR5Lm9yZ4IOd2lraXZveWFnZS5vcmeCDndpa3Rpb25hcnkub3Jnghd3aWtpbWVkaWFmb3VuZGF0aW9uLm9yZ4IGdy53aWtpghJ3bWZ1c2VyY29udGVudC5vcmeCESoubS53aWtpcGVkaWEub3Jngg8qLndpa2ltZWRpYS5vcmeCESoubS53aWtpbWVkaWEub3JnghYqLnBsYW5ldC53aWtpbWVkaWEub3Jngg8qLm1lZGlhd2lraS5vcmeCESoubS5tZWRpYXdpa2kub3Jngg8qLndpa2lib29rcy5vcmeCESoubS53aWtpYm9va3Mub3Jngg4qLndpa2lkYXRhLm9yZ4IQKi5tLndpa2lkYXRhLm9yZ4IOKi53aWtpbmV3cy5vcmeCECoubS53aWtpbmV3cy5vcmeCDyoud2lraXF1b3RlLm9yZ4IRKi5tLndpa2lxdW90ZS5vcmeCECoud2lraXNvdXJjZS5vcmeCEioubS53aWtpc291cmNlLm9yZ4IRKi53aWtpdmVyc2l0eS5vcmeCEyoubS53aWtpdmVyc2l0eS5vcmeCECoud2lraXZveWFnZS5vcmeCEioubS53aWtpdm95YWdlLm9yZ4IQKi53aWt0aW9uYXJ5Lm9yZ4ISKi5tLndpa3Rpb25hcnkub3JnghkqLndpa2ltZWRpYWZvdW5kYXRpb24ub3JnghQqLndtZnVzZXJjb250ZW50Lm9yZ4INd2lraXBlZGlhLm9yZ4IRd2lraWZ1bmN0aW9ucy5vcmeCEyoud2lraWZ1bmN0aW9ucy5vcmcwPgYDVR0gBDcwNTAzBgZngQwBAgIwKTAnBggrBgEFBQcCARYbaHR0cDovL3d3dy5kaWdpY2VydC5jb20vQ1BTMA4GA1UdDwEB/wQEAwIDiDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwgZsGA1UdHwSBkzCBkDBGoESgQoZAaHR0cDovL2NybDMuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0VExTSHlicmlkRUNDU0hBMzg0MjAyMENBMS0xLmNybDBGoESgQoZAaHR0cDovL2NybDQuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0VExTSHlicmlkRUNDU0hBMzg0MjAyMENBMS0xLmNybDCBhQYIKwYBBQUHAQEEeTB3MCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC5kaWdpY2VydC5jb20wTwYIKwYBBQUHMAKGQ2h0dHA6Ly9jYWNlcnRzLmRpZ2ljZXJ0LmNvbS9EaWdpQ2VydFRMU0h5YnJpZEVDQ1NIQTM4NDIwMjBDQTEtMS5jcnQwDAYDVR0TAQH/BAIwADCCAYAGCisGAQQB1nkCBAIEggFwBIIBbAFqAHcA7s3QZNXbGs7FXLedtM0TojKHRny87N7DUUhZRnEftZsAAAGLQ1J6cgAABAMASDBGAiEA5reeeuLSzGPvJQ5hT3Bd8aOVxmIltXMTLhY619qDGWUCIQDO0LMbF3s42tyxgFIOt7rVOpsHe9Sy0wFQQj8BWO0LIQB2AEiw42vapkc0D+VqAvqdMOscUgHLVt0sgdm7v6s52IRzAAABi0NSegEAAAQDAEcwRQIgYJduBrioIun6FTeQhDxqK2eyZehguOkxScS3nwsGSakCIQC1FyuCpm+QQBRJFSTAnStRiP+hgGIhgzyZ837usahB0QB3ANq2v2s/tbYin5vCu1xr6HCRcWy7UYSFNL2kPTBI1/urAAABi0NSeg8AAAQDAEgwRgIhAOm1GvY8M4V+tUyjV9/PCj8rcWHUOvfY0a/onsKg/bitAiEA1Vm1pP8CDp7hGcQzBBTscpCVebzWCe8DK231mtv97QUwCgYIKoZIzj0EAwMDaAAwZQIwKuOOLjmwGgtjG6SASF4W2e8KtQZANRsYXMXJDGwBCi9fM7QyS9dvlFLwrcDg1gxlAjEA5XwJikbpk/qyQerzeUspuZKhqh1KPuj2uBdp8vicuBxuTJUd1W+d3LmikOUgGzil-----END CERTIFICATE-----""",
                input_format=Formats.DER,
            ),
            # TODO
            Data(
                remarks_list='Cloud fare Url; Crashing',
                raw_data=r'https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/',
                input_format=Formats.URL,
            ),
        ]
        super().set_data_pool(data_pool)
