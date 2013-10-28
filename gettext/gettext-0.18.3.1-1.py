class gettext(Formula):

    name = 'gettext'
    version = '0.18.3.1'
    revision = 1
    homepage = 'http://www.gnu.org/software/gettext/'
    sources = File('http://ftpmirror.gnu.org/gettext/gettext-0.18.3.1.tar.gz',
                   sha256='0d8f9a33531b77776b3dc473e7940019ca19bfca5b4c06db6e96065eeb07245d')
    configure_args = Formula.configure_args + ['--disable-debug']
