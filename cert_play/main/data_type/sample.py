from collections import OrderedDict

from python_helpers.ph_util import PhUtil

from cert_play.main.data_type.data_type_master import DataTypeMaster
from cert_play.main.helper.data import Data
from cert_play.main.helper.formats import Formats


# Data has to be declared in global, so that it can be used by other classes

class Sample(DataTypeMaster):

    def get_sample_data_pool_for_web(self):
        if not self.data_pool:
            self.set_data_pool()
        sample_data_dic = OrderedDict()
        for data in self.data_pool:
            remarks = data.remarks
            remarks = PhUtil.to_list(remarks, all_str=True, trim_data=True)
            if len(remarks) < 1:
                raise ValueError("Remarks should not be empty")
            key, data.data_group = PhUtil.generate_key_and_data_group(remarks)
            if key in sample_data_dic:
                raise ValueError(f'Duplicate Sample Remarks: {key}')
            sample_data_dic.update({key: super().to_dic(data)})
        return sample_data_dic

    def __init__(self):
        super().__init__()

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

    def set_encoding(self):
        encoding = None
        super().set_encoding(encoding)

    def set_encoding_errors(self):
        encoding_errors = None
        super().set_encoding_errors(encoding_errors)

    def set_output_path(self):
        output_path = None
        super().set_output_path(output_path)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

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
            Data(
                remarks='Url; IP; AmenityPj',
                input_data='3.141.211.207',
                input_format=Formats.URL,
            ),
            #
            Data(
                remarks='Url; All Certs; AmenityPj',
                input_data='amenitypj.in',
                input_format=Formats.URL,
                url_all_certs=True,
            ),
            #
            Data(
                remarks='Url; https; www; AmenityPj',
                input_data='https://www.amenitypj.in/',
                input_format=Formats.URL,
            ),
            #
            Data(
                remarks='Url; Sub Domain; AmenityPj',
                input_data='beta.amenitypj.in',
                input_format=Formats.URL,
            ),
            #
            Data(
                remarks='Url; Google',
                input_data='google.com',
                input_format=Formats.URL,
            ),
            #
            Data(
                remarks='Url; All Certs; Google; Fetch Only',
                input_data='google.com',
                input_format=Formats.URL,
                url_all_certs=True,
                url_cert_fetch_only=True,
            ),
            #
            Data(
                remarks='Url; https; www; Google',
                input_data='https://www.google.com/',
                input_format=Formats.URL,
            ),
            #
            Data(
                remarks='Url; AmenityPj; Fetch Only',
                input_data='amenitypj.in',
                input_format=Formats.URL,
                url_cert_fetch_only=True,
            ),
            #
            Data(
                remarks='Url; Sub Pages; WikiPedia; url_time_out=10',
                input_data='https://en.wikipedia.org/wiki/Main_Page',
                input_format=Formats.URL,
                url_time_out=10,
            ),
            #
            Data(
                remarks='Url; https; www; cloudflare; Forbidden; url_pre_access=False',
                input_data='https://www.cloudflare.com',
                input_format=Formats.URL,
                url_pre_access=False,
            ),
            #
            Data(
                remarks='Der; Base64; Certificate; Single Line; AmenityPj',
                input_data='MIIErzCCA5egAwIBAgISA8caMPaDk56P1v8RvxkQdgxpMA0GCSqGSIb3DQEBCwUAMDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQDEwJSMzAeFw0yNDA1MTEwNzM0MThaFw0yNDA4MDkwNzM0MTdaMBcxFTATBgNVBAMTDGFtZW5pdHlwai5pbjBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABL74hi/pJ2opqu+36ppYNCt65tD3B2Kq5u1C3n/QqlofA2tdW1MXMxTPX2x66cEuMWYH0eTi0EZWv0tRB18Hy0ajggKjMIICnzAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFNPucKQzTDVMjhjQEASfE1Gh44fWMB8GA1UdIwQYMBaAFBQusxe3WFbLrlAJQOYfr52LFMLGMFUGCCsGAQUFBwEBBEkwRzAhBggrBgEFBQcwAYYVaHR0cDovL3IzLm8ubGVuY3Iub3JnMCIGCCsGAQUFBzAChhZodHRwOi8vcjMuaS5sZW5jci5vcmcvMIGrBgNVHREEgaMwgaCCEmFscGhhLmFtZW5pdHlwai5pboIMYW1lbml0eXBqLmlughFiZXRhLmFtZW5pdHlwai5pboIRcGFzdC5hbWVuaXR5cGouaW6CFnd3dy5hbHBoYS5hbWVuaXR5cGouaW6CEHd3dy5hbWVuaXR5cGouaW6CFXd3dy5iZXRhLmFtZW5pdHlwai5pboIVd3d3LnBhc3QuYW1lbml0eXBqLmluMBMGA1UdIAQMMAowCAYGZ4EMAQIBMIIBBAYKKwYBBAHWeQIEAgSB9QSB8gDwAHYASLDja9qmRzQP5WoC+p0w6xxSActW3SyB2bu/qznYhHMAAAGPZsnk6QAABAMARzBFAiEA5YpmM1dVtOW7SH2/SVEHpi9TdDv1j1+SMbiaw1CrqN4CIH/ulMV5ItLuRMyvz63qdkPHuesahzkNUNe1lJax8mlPAHYA3+FW66oFr7WcD4ZxjajAMk6uVtlup/WlagHRwTu+UlwAAAGPZsnmAAAABAMARzBFAiEA5z82NzuMuMPKl7z2lthCsSGZkNvO4VKHYJbMfrFwCAYCIDOTKLX5p+9CS8rF38jM0JZi6Gh2GwoH04oEk6lIbdpGMA0GCSqGSIb3DQEBCwUAA4IBAQCYYN6K+WblpJXB3VDpoaxJB/raiD5m4B0Yr4b0SFdBRNac/N+dBxxBTSizlW+2DkqU4j0Ni7DrudwpqZWMe9pSTRtnIgUdAs9TqpwMszUuCrToDzIbBdxYyI+4cDbMpdJtRcJLBUvBrp38b6oFp3hLs34VruS+SyXGIcnCzhJjSfUIMM51VCyyO+qbLWWRGPxz231lB6pktznflJtCllqPaOGifLBa7it2I7chuMW00GuZ4MDytqmRtWu704KKy6jiuqp+c7+je6L+B63mVry1cZlWhDm4Mhs3wpJ2k8xjzOPiHHqGCAvjLZtXkx1y1T2Y1Si62lB1iGx939ucrYhF',
                input_format=Formats.DER,
            ),
            #
            Data(
                remarks='Der; Base64; Certificate; Multi Line; AmenityPj',
                input_data="""MIIErzCCA5egAwIBAgISA8caMPaDk56P1v8RvxkQdgxpMA0GCSqGSIb3DQEBCwUA
MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
EwJSMzAeFw0yNDA1MTEwNzM0MThaFw0yNDA4MDkwNzM0MTdaMBcxFTATBgNVBAMT
DGFtZW5pdHlwai5pbjBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABL74hi/pJ2op
qu+36ppYNCt65tD3B2Kq5u1C3n/QqlofA2tdW1MXMxTPX2x66cEuMWYH0eTi0EZW
v0tRB18Hy0ajggKjMIICnzAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYB
BQUHAwEGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFNPucKQzTDVM
jhjQEASfE1Gh44fWMB8GA1UdIwQYMBaAFBQusxe3WFbLrlAJQOYfr52LFMLGMFUG
CCsGAQUFBwEBBEkwRzAhBggrBgEFBQcwAYYVaHR0cDovL3IzLm8ubGVuY3Iub3Jn
MCIGCCsGAQUFBzAChhZodHRwOi8vcjMuaS5sZW5jci5vcmcvMIGrBgNVHREEgaMw
gaCCEmFscGhhLmFtZW5pdHlwai5pboIMYW1lbml0eXBqLmlughFiZXRhLmFtZW5p
dHlwai5pboIRcGFzdC5hbWVuaXR5cGouaW6CFnd3dy5hbHBoYS5hbWVuaXR5cGou
aW6CEHd3dy5hbWVuaXR5cGouaW6CFXd3dy5iZXRhLmFtZW5pdHlwai5pboIVd3d3
LnBhc3QuYW1lbml0eXBqLmluMBMGA1UdIAQMMAowCAYGZ4EMAQIBMIIBBAYKKwYB
BAHWeQIEAgSB9QSB8gDwAHYASLDja9qmRzQP5WoC+p0w6xxSActW3SyB2bu/qznY
hHMAAAGPZsnk6QAABAMARzBFAiEA5YpmM1dVtOW7SH2/SVEHpi9TdDv1j1+SMbia
w1CrqN4CIH/ulMV5ItLuRMyvz63qdkPHuesahzkNUNe1lJax8mlPAHYA3+FW66oF
r7WcD4ZxjajAMk6uVtlup/WlagHRwTu+UlwAAAGPZsnmAAAABAMARzBFAiEA5z82
NzuMuMPKl7z2lthCsSGZkNvO4VKHYJbMfrFwCAYCIDOTKLX5p+9CS8rF38jM0JZi
6Gh2GwoH04oEk6lIbdpGMA0GCSqGSIb3DQEBCwUAA4IBAQCYYN6K+WblpJXB3VDp
oaxJB/raiD5m4B0Yr4b0SFdBRNac/N+dBxxBTSizlW+2DkqU4j0Ni7DrudwpqZWM
e9pSTRtnIgUdAs9TqpwMszUuCrToDzIbBdxYyI+4cDbMpdJtRcJLBUvBrp38b6oF
p3hLs34VruS+SyXGIcnCzhJjSfUIMM51VCyyO+qbLWWRGPxz231lB6pktznflJtC
llqPaOGifLBa7it2I7chuMW00GuZ4MDytqmRtWu704KKy6jiuqp+c7+je6L+B63m
Vry1cZlWhDm4Mhs3wpJ2k8xjzOPiHHqGCAvjLZtXkx1y1T2Y1Si62lB1iGx939uc
rYhF""",
                input_format=Formats.DER,
            ),
            #
            Data(
                remarks='Der; Base64; Certificate; Multi Line; Header & Footer; AmenityPj',
                input_data="""-----BEGIN CERTIFICATE-----
MIIErzCCA5egAwIBAgISA8caMPaDk56P1v8RvxkQdgxpMA0GCSqGSIb3DQEBCwUA
MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
EwJSMzAeFw0yNDA1MTEwNzM0MThaFw0yNDA4MDkwNzM0MTdaMBcxFTATBgNVBAMT
DGFtZW5pdHlwai5pbjBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABL74hi/pJ2op
qu+36ppYNCt65tD3B2Kq5u1C3n/QqlofA2tdW1MXMxTPX2x66cEuMWYH0eTi0EZW
v0tRB18Hy0ajggKjMIICnzAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYB
BQUHAwEGCCsGAQUFBwMCMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFNPucKQzTDVM
jhjQEASfE1Gh44fWMB8GA1UdIwQYMBaAFBQusxe3WFbLrlAJQOYfr52LFMLGMFUG
CCsGAQUFBwEBBEkwRzAhBggrBgEFBQcwAYYVaHR0cDovL3IzLm8ubGVuY3Iub3Jn
MCIGCCsGAQUFBzAChhZodHRwOi8vcjMuaS5sZW5jci5vcmcvMIGrBgNVHREEgaMw
gaCCEmFscGhhLmFtZW5pdHlwai5pboIMYW1lbml0eXBqLmlughFiZXRhLmFtZW5p
dHlwai5pboIRcGFzdC5hbWVuaXR5cGouaW6CFnd3dy5hbHBoYS5hbWVuaXR5cGou
aW6CEHd3dy5hbWVuaXR5cGouaW6CFXd3dy5iZXRhLmFtZW5pdHlwai5pboIVd3d3
LnBhc3QuYW1lbml0eXBqLmluMBMGA1UdIAQMMAowCAYGZ4EMAQIBMIIBBAYKKwYB
BAHWeQIEAgSB9QSB8gDwAHYASLDja9qmRzQP5WoC+p0w6xxSActW3SyB2bu/qznY
hHMAAAGPZsnk6QAABAMARzBFAiEA5YpmM1dVtOW7SH2/SVEHpi9TdDv1j1+SMbia
w1CrqN4CIH/ulMV5ItLuRMyvz63qdkPHuesahzkNUNe1lJax8mlPAHYA3+FW66oF
r7WcD4ZxjajAMk6uVtlup/WlagHRwTu+UlwAAAGPZsnmAAAABAMARzBFAiEA5z82
NzuMuMPKl7z2lthCsSGZkNvO4VKHYJbMfrFwCAYCIDOTKLX5p+9CS8rF38jM0JZi
6Gh2GwoH04oEk6lIbdpGMA0GCSqGSIb3DQEBCwUAA4IBAQCYYN6K+WblpJXB3VDp
oaxJB/raiD5m4B0Yr4b0SFdBRNac/N+dBxxBTSizlW+2DkqU4j0Ni7DrudwpqZWM
e9pSTRtnIgUdAs9TqpwMszUuCrToDzIbBdxYyI+4cDbMpdJtRcJLBUvBrp38b6oF
p3hLs34VruS+SyXGIcnCzhJjSfUIMM51VCyyO+qbLWWRGPxz231lB6pktznflJtC
llqPaOGifLBa7it2I7chuMW00GuZ4MDytqmRtWu704KKy6jiuqp+c7+je6L+B63m
Vry1cZlWhDm4Mhs3wpJ2k8xjzOPiHHqGCAvjLZtXkx1y1T2Y1Si62lB1iGx939uc
rYhF
-----END CERTIFICATE-----""",
                input_format=Formats.DER,
            ),
            #
            Data(
                remarks='Der; Hex; Certificate; AmenityPj',
                input_data=r'308204AF30820397A003020102021203C71A30F683939E8FD6FF11BF1910760C69300D06092A864886F70D01010B05003032310B300906035504061302555331163014060355040A130D4C6574277320456E6372797074310B3009060355040313025233301E170D3234303531313037333431385A170D3234303830393037333431375A3017311530130603550403130C616D656E697479706A2E696E3059301306072A8648CE3D020106082A8648CE3D03010703420004BEF8862FE9276A29AAEFB7EA9A58342B7AE6D0F70762AAE6ED42DE7FD0AA5A1F036B5D5B53173314CF5F6C7AE9C12E316607D1E4E2D04656BF4B51075F07CB46A38202A33082029F300E0603551D0F0101FF040403020780301D0603551D250416301406082B0601050507030106082B06010505070302300C0603551D130101FF04023000301D0603551D0E04160414D3EE70A4334C354C8E18D010049F1351A1E387D6301F0603551D23041830168014142EB317B75856CBAE500940E61FAF9D8B14C2C6305506082B0601050507010104493047302106082B060105050730018615687474703A2F2F72332E6F2E6C656E63722E6F7267302206082B060105050730028616687474703A2F2F72332E692E6C656E63722E6F72672F3081AB0603551D110481A33081A08212616C7068612E616D656E697479706A2E696E820C616D656E697479706A2E696E8211626574612E616D656E697479706A2E696E8211706173742E616D656E697479706A2E696E82167777772E616C7068612E616D656E697479706A2E696E82107777772E616D656E697479706A2E696E82157777772E626574612E616D656E697479706A2E696E82157777772E706173742E616D656E697479706A2E696E30130603551D20040C300A3008060667810C01020130820104060A2B06010401D6790204020481F50481F200F000760048B0E36BDAA647340FE56A02FA9D30EB1C5201CB56DD2C81D9BBBFAB39D884730000018F66C9E4E90000040300473045022100E58A66335755B4E5BB487DBF495107A62F53743BF58F5F9231B89AC350ABA8DE02207FEE94C57922D2EE44CCAFCFADEA7643C7B9EB1A87390D50D7B59496B1F2694F007600DFE156EBAA05AFB59C0F86718DA8C0324EAE56D96EA7F5A56A01D1C13BBE525C0000018F66C9E6000000040300473045022100E73F36373B8CB8C3CA97BCF696D842B1219990DBCEE152876096CC7EB17008060220339328B5F9A7EF424BCAC5DFC8CCD09662E868761B0A07D38A0493A9486DDA46300D06092A864886F70D01010B050003820101009860DE8AF966E5A495C1DD50E9A1AC4907FADA883E66E01D18AF86F448574144D69CFCDF9D071C414D28B3956FB60E4A94E23D0D8BB0EBB9DC29A9958C7BDA524D1B6722051D02CF53AA9C0CB3352E0AB4E80F321B05DC58C88FB87036CCA5D26D45C24B054BC1AE9DFC6FAA05A7784BB37E15AEE4BE4B25C621C9C2CE126349F50830CE75542CB23BEA9B2D659118FC73DB7D6507AA64B739DF949B42965A8F68E1A27CB05AEE2B7623B721B8C5B4D06B99E0C0F2B6A991B56BBBD3828ACBA8E2BAAA7E73BFA37BA2FE07ADE656BCB57199568439B8321B37C2927693CC63CCE3E21C7A86080BE32D9B57931D72D53D98D528BADA5075886C7DDFDB9CAD8845',
                input_format=Formats.DER,
            ),
            #
            Data(
                remarks='Der; Hex; Certificate; CI; GSMA NIST CI Cert (SGP.26_v1.x)',
                input_data=r'30820250308201F7A003020102020900B874F3ABFA6C44D3300A06082A8648CE3D04030230443110300E06035504030C07546573742043493111300F060355040B0C0854455354434552543110300E060355040A0C0752535054455354310B30090603550406130249543020170D3230303430313038323735315A180F32303535303430313038323735315A30443110300E06035504030C07546573742043493111300F060355040B0C0854455354434552543110300E060355040A0C0752535054455354310B30090603550406130249543059301306072A8648CE3D020106082A8648CE3D03010703420004940657A673DC288F89D52EA8A47704992791F9C34B0036E633E2D0CBA9454D65DB32EB17981799D2F24388EE2B95C1094546C97901CEAEBA9650919A2E20D229A381CF3081CC301D0603551D0E04160414F54172BDF98A95D65CBEB88A38A1C11D800A85C3300F0603551D130101FF040530030101FF30170603551D200101FF040D300B3009060767811201020100300E0603551D0F0101FF040403020106300E0603551D1104073005880388370130610603551D1F045A3058302AA028A0268624687474703A2F2F63692E746573742E6578616D706C652E636F6D2F43524C2D412E63726C302AA028A0268624687474703A2F2F63692E746573742E6578616D706C652E636F6D2F43524C2D422E63726C300A06082A8648CE3D0403020347003044022052756AAFC2020A6CECBF2E5F3C20892510FF29751D298BD3B015D9605A4FE67D022057982836E4D205DDD2E6C3C1B455937F6B6E493B602FD1B66C357489A935F76B',
                input_format=Formats.DER,
            ),
            #
        ]
        super().set_data_pool(data_pool)
