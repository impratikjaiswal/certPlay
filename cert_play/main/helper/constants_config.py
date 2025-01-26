from cert_play._git_info import GIT_SUMMARY
from cert_play._tool_name import TOOL_NAME
from cert_play._version import __version__


class ConfigConst:
    TOOL_VERSION = __version__.public()
    TOOL_VERSION_DETAILED = f'v{TOOL_VERSION}'
    TOOL_NAME = TOOL_NAME
    TOOL_TITLE = 'Cert Play'
    TOOL_GIT_SUMMARY = GIT_SUMMARY
    TOOL_DESCRIPTION = f'Generic Certificate Parser based on X.509 and related standards. Can fetch (& parse) TLS certificate(s) of any live website.'
    TOOL_META_DESCRIPTION = f'{TOOL_DESCRIPTION}'
    TOOL_META_KEYWORDS = f'{TOOL_TITLE}, Certificate Parser, certificate parser, cert, certificate, tls, transport layer security, tls certificate, ssl, x509, ssl certificate, openssl. certificate chain, all server certs, all certs'
    TOOL_URL = 'https://github.com/impratikjaiswal/certPlay'
    TOOL_URL_BUG_TRACKER = 'https://github.com/impratikjaiswal/certPlay/issues'
