import urllib

from python_helpers.ph_util import PhUtil

from cert_play.main.convert.converter import clean_and_pre_access_url_data


def compare_urlparse_urlsplit(input_data):
    urlparse_data = urllib.parse.urlparse(input_data)
    urlsplit_data = urllib.parse.urlsplit(input_data)
    # print(f'urlparse_data: {urlparse_data}')
    # print(f'urlsplit_data: {urlsplit_data}')
    if urlparse_data.scheme != urlsplit_data.scheme:
        print(f'scheme is different for {input_data}')
    if urlparse_data.netloc != urlsplit_data.netloc:
        print(f'netloc is different for {input_data}')
    if urlparse_data.path != urlsplit_data.path:
        print(f'path is different for {input_data}')
    if urlparse_data.query != urlsplit_data.query:
        print(f'query is different for {input_data}')
    if urlparse_data.fragment != urlsplit_data.fragment:
        print(f'fragment is different for {input_data}')
    if urlparse_data.params:
        print(f'params is available for {input_data}')
    if not urlparse_data.netloc:
        print(f'netloc is missing for {input_data}, urlparse_data is {urlparse_data}')


def get_urls_pool():
    url_pool_primary = [
        'https://www.amenitypj.in/',
        'https://www.cloudflare.com',
        'https://www.cloudflare.com/',
        'www.cloudflare.com/',
        'cloudflare.com/',
        'cloudflare.com',
    ]
    url_pool_testing = [
        'abcdefghijklmnopqrstuvwxyz',
        'https://www.xn--i1bj3fqcyde.xn--11b7cb3a6a.xn--h2brj9c/',
        'https://www.india.gov.in/',
        'scheme://netloc/path;parameters?query#fragment',
        'https://www.example.com/some_path?some_key=some_value',
        'http://foo.appspot.com/abc?def=ghi',
        'http://docs.python.org:80/3/library/urllib.parse.html?highlight=params#url-parsing',
        'https://example.tracker.com/?cid=9999&lp={escapedlpurl}',
        'https://example.tracker.com/?cid=9999&lp={escapedlpurl}%3Fsrc%3Dgoogle',
        'http://example.com?sid=1234567&src=google',
        'https://domain.com/t-shirts?color=black',
        'www.geeksforgeeks.com/article.php#hello',
        'http://example.com?productid=1234',
        'http://www.cwi.nl:80/%7Eguido/Python.html',
        '//www.cwi.nl:80/%7Eguido/Python.html',
        'www.cwi.nl/%7Eguido/Python.html',
        'help/Python.html',
        'amenitypj.in:443',
        'beta.amenitypj.in:443',
        'en.wikipedia.org/:443',
        'en.wikipedia.org/wiki/:443',
        'en.wikipedia.org/wiki/Main_Page:443',
        'en.wikipedia.org/wiki:443',
        'en.wikipedia.org:443',
        'http://www.ietf.org/rfc/rfc3986.txt',
        'https://en.wikipedia.org/wiki/Main_Page:443',
        'https://www.amenitypj.in/:443',
        'https://www.amenitypj.in:443',
        'wikipedia.org:443',
        'www.amenitypj.in/:443',
        'www.amenitypj.in/asn1Play:443',
        'www.amenitypj.in:443',
        'www.amenitypj.in:8080',
        'www.beta.amenitypj.in:443',
        'www.en.wikipedia.org:443',
        'www.wikipedia.org:443',
        'ftps://example.com',
        'google.com',
        'google.com.ua',
        'http://cloggedtubes.com/development/the_aihyperlinks_framework_or_how_adium_finds_links',
        'http://en.wikipedia.org/wiki/PC_Tools_%28Central_Point_Software%29',
        'http://en.wikipedia.org/wiki/PC_Tools_(Central_Point_Software)',
        'http://google.com.ua',
        'http://google.com/',
        'http://mail.google.com',
        'http://msdn.microsoft.com/en-us/library/aa752574%28VS.85%29.aspx',
        'http://msdn.microsoft.com/en-us/library/aa752574(VS.85).aspx',
        'http://oreilly.com/catalog/9780596528126/index.html',
        'http://subdomain.web-site.com/cgi-bin/perl.cgi?key1=value1&key2=value2e',
        'http://www.example1.com/test.html',
        'http://www.example1.com/test.html/a',
        'http://www.example2.com/test2.html',
        'http://www.example2.com/test2.html/a',
        'http://www.faqs.org/rfcs/rfc3696.html',
        'http://www.faqs.org/rfcs/rfc3987.html',
        'http://www.google.com',
        'http://www.google.com.ua',
        'http://www.google.com/codesearch?q=jeff',
        'https://autobahn-security.com/',
        'https://blog.codinghorror.com/the-problem-with-urls/',
        'https://docs.python.org/3.0/library/urllib.parse.html',
        'https://docs.python.org/3.7/library/urllib.parse.html#module-urllib.parse',
        'https://en.wikipedia.org/wiki/RegexBuddy',
        'https://example.com',
        'https://example.com/dir//',
        'https://example.com/dir/file.php?var=moo',
        'https://github.com/django/django/blob/main/django/core/validators.py#L74',
        'https://github.com/django/django/blob/main/django/forms/fields.py#L534',
        'https://google.com.ua/',
        'https://google.com/',
        'https://learn.microsoft.com/en-us/dotnet/api/system.uri?view=net-8.0&redirectedfrom=MSDN',
        'https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff650303(v=pandp.10)?redirectedfrom=MSDN',
        'https://mail.google.com',
        'https://mail.python.org/pipermail/python-list/2007-January/595436.html',
        'https://metacpan.org/dist/URI',
        'https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS',
        'https://pdw.ex-parrot.com/Mail-RFC822-Address.html',
        'https://pypi.org/project/rfc3987/',
        'https://regex101.com/r/HUNasA/2',
        'https://ruby-doc.org/stdlib-1.9.3/libdoc/uri/rdoc/URI.html',
        'https://slproweb.com/products/Win32OpenSSL.html',
        'https://stackoverflow.com/questions/827557/how-do-you-validate-a-url-with-a-regular-expression-in-python',
        'https://www.acooke.org/cute/LEPLOptimi0.html',
        'https://www.acooke.org/lepl',
        'https://www.acooke.org/lepl/rfc3696.html',
        'https://www.akto.io/tools/url-regex-Python-tester',
        'https://www.debuggex.com/r/NmFIiM9vZwKdYEKZ',
        'https://www.freecodecamp.org/news/how-to-write-a-regular-expression-for-a-url/',
        'https://www.geeksforgeeks.org',
        'https://www.geeksforgeeks.org/check-if-an-url-is-valid-or-not-using-regular-expression/',
        'https://www.google.com',
        'https://www.google.com.ua',
        'https://www.google.com/',
        'https://www.google.com/somthing%22/somethingmore',
        'https://www.ietf.org/rfc/rfc3986.txt',
        'https://www.php.net/manual/en/function.parse-url.php',
        'https://www.regexbuddy.com/download.html',
        'mail.google.com',
        'mailto:somebody@google.com',
        'sftp://example.com',
        'somebody@google.com',
        'www.google.com',
        'www.google.com.ua',
        'www.url-with-querystring.com/?url=has-querystring',
        # shouldNotMatch
        'http://google',
        'https://google.c',
        'google',
        'google.',
        '.google',
        '.google.com',
        'goole.c',
        '...',
        'Google.com',
        'noprotocol.com',
        ' https://space-in-front.com',
        'https://invalid.0om',
        'https://invalid.-om',
        'https://invalid-single-letter-tld.c',
        'https://invalid-domain&char.com',
        'https://invalid:com',
        'https://not valid.com',
        'https://not,valid.com',
        'https://龠.c龠',
        'https://invalidαΒβΣσ.com',
        'notvalid://www.google.com',
        'http://missing-tld',
        'https://0.0.0.0missing-port',
        '0.0.0.0:0/missing-protocol',
        'https://256.255.255.255:0/is-above-max',
        'https://this.tld-is-64-characters-which-is-too-looooooooooooooooooooooooooong',
        'www..dr.google',
        'www:google.com',
        'https://www@.google.com',
        'https://www.google.com\'',
        'http://www.google.com/path',
        'http://www.google.com/?queryparam=123',
        'http://www.google.com/path?queryparam=123',
        'http/stackoverflow.com/',
        'h77ps://stackoverflow.com/',
        '//stackoverflow.com/',
        # shouldMatch
        'www.google.co.uk',
        'http://www.google.co.uk',
        'https://www.google.co.uk',
        'google.co.uk',
        'google.mu',
        'mes.intnet.mu',
        'cse.uom.ac.mu',
        'https://base.com/',
        'http://t.co',
        'https://www.google.com.ua/',
        'https://subdomains.as.deep.as.you.want.example.com',
        'https://sub.second_leveldomain_underscore.verylongtoplevedomain/nice',
        'https://domain-name.com/path-common-characters/ABCxyz01789',
        'http://domaîn-with-àccents.ca',
        'http://path-with-accents.com/àèìòùçÇßØøÅåÆæœ',
        'https://en.wikipedia.org/wiki/Möbius_strip',
        'http://www.😉.tld/emojis-🤖-in-👏-domain/-and-path-🚀/',
        'https://y.at/🚀🚀🚀',
        'https://hashtag.forpath#lets-go',
        ",http://special.com/all-special-characters-._~:/?#[]@!$&'() * +,;=',",
        'https://greek_with_diacritics.co/ΑαΒβΣσ/ςΤτϋΰήώΊΪΌΆΈΎΫΉΏᾶἀ',
        'https://el.wikipedia.org/wiki/Ποσειδώνας_(πλανήτης)',
        'http://cyrillic-and-extras.ru/АаБбВвЪъыӸӹЫЯЯяѶѷ',
        'https://ru.wikipedia.org/wiki/Заглавная_страница',
        'https://most-arabic.co/گچپژیلفقهموء-يجريبتج/',
        'https://urdu.co/حروفِ/',
        'https://nigerian.ni/ƁƊƎẸɓɗǝẹỊƘỌịƙọṢỤṣụ',
        'https://bengali.sports.co/স্পর্শঅনুনাসিকলসওষ্ঠ্যপফবভম/',
        'https://devenagri.cc/कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषस',
        'https://h.org/wiki/Wikipedia:关于中文维基百科/en',
        'https://zh.wikipedia.org/wiki/Wikipedia:关于中文维基百科/en',
        'http://others.kr/korean-안녕ㆅㅇㄹㅿㆍㅡㅣㅗㅑㅠㅕ/japanese-一龠ぁゔａｚＡＺ０９々〆〤ヶ',
        'https://龠.subdomain.com',
        'http://127.0.0.1:22/valid-ip',
        'http://127.00.00.01:22/ugly-but-still-works-with-modern-browsers',
        'http://0.0.0.0:0/is-min',
        'https://255.255.255.255:0/is-max',
        'https://this.tld-is-63-characters-wich-is-the-theoretical-limit-000000000000',
        #
    ]
    return url_pool_primary
    # return url_pool_primary + url_pool_testing


class Test:

    @classmethod
    def test_sample_data(cls):
        PhUtil.print_separator()

    @classmethod
    def test_all_versions(cls):
        PhUtil.print_separator()

    @classmethod
    def test_data(cls):
        for url in get_urls_pool():
            try:
                clean_and_pre_access_url_data(url)
                print(f'url {url} is accessible')
            except Exception as e:
                print(e)

    @classmethod
    def test_all(cls):
        cls.test_sample_data()
        cls.test_all_versions()
        cls.test_data()
