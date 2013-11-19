from ipkg.build import Formula, File


class gdbm(Formula):

    name = 'gdbm'
    version = '1.10'
    homepage = 'http://www.gnu.org/software/gdbm/'
    sources = File('http://ftpmirror.gnu.org/gdbm/gdbm-1.10.tar.gz',
                   sha1='441201e9145f590ba613f8a1e952455d620e0860')
    configure_args = ('--prefix=%(prefix)s', '--mandir=%(man)s')
