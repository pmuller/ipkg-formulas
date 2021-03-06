from ipkg.build import Formula, File


class pkgconfig(Formula):

    name = 'pkg-config'
    version = '0.28'
    homepage = 'http://pkgconfig.freedesktop.org'
    sources = File('http://pkgconfig.freedesktop.org/releases/pkg-config-0.28.tar.gz',
                   sha256='6b6eb31c6ec4421174578652c7e141fdaae2dabad1021f420d8713206ac1f845')
    configure_args = ('--prefix=%(prefix)s',
                      '--disable-debug',
                      '--disable-host-tool',
                      '--with-internal-glib')
