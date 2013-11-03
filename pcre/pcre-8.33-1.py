from ipkg.build import Formula, File


class pcre(Formula):

    name = 'pcre'
    version = '8.33'
    homepage = 'http://www.pcre.org/'
    sources = File('http://downloads.sourceforge.net/project/pcre/pcre/8.33/pcre-8.33.tar.bz2',
                   sha256='c603957a4966811c04af5f6048c71cfb4966ec93312d7b3118116ed9f3bc0478')
    configure_args = ('--prefix=%(prefix)s',
                      '--enable-utf8',
                      '--enable-unicode-properties',
                      '--enable-pcregrep-libz',
                      '--enable-pcregrep-libbz2',
                      '--enable-jit')
