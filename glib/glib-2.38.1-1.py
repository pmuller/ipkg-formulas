class glib(Formula):

    name = 'glib'
    version = '2.38.1'
    revision = 1
    homepage = 'http://developer.gnome.org/glib/'
    sources = File('http://ftp.gnome.org/pub/gnome/sources/glib/2.38/glib-2.38.1.tar.xz',
                    sha256='01906c62ac666d2ab3183cc07261b2536fab7b211c6129ab66b119c2af56d159')
    dependencies = ('pkg-config', 'gettext', 'libffi', 'xz')
    configure_args = Formula.configure_args + [
        '--disable-maintainer-mode',
        '--disable-dependency-tracking',
        '--disable-silent-rules',
        '--disable-dtrace',
        '--disable-modular-tests',
        '--disable-libelf',
    ]
