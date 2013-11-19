from ipkg.build import Formula, File


class python(Formula):

    name = 'python'
    version = '2.7.5'
    homepage = 'http://www.python.org'
    sources = File('http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2',
                   sha1='6cfada1a739544a6fa7f2601b500fba02229656b')
    dependencies = ('pkg-config', 'readline', 'sqlite', 'gdbm', 'openssl')
    configure_args = ('--prefix=%(prefix)s',
                      '--enable-ipv6',
                      '--datarootdir=%(share)s',
                      '--datadir=%(share)s')

    setuptools = File('https://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.6.tar.gz',
                      sha1='4a8863e8196704759a5800afbcf33a94b802ac88')
    pip = File('https://pypi.python.org/packages/source/p/pip/pip-1.4.1.tar.gz',
               sha1='9766254c7909af6d04739b4a7732cc29e9a48cb0')

    def install(self):
        self.run_configure()
        self.run_make()
        self.run_make('install')
        self.install_python_package('setuptools', self.setuptools)
        self.install_python_package('pip', self.pip)

    def install_python_package(self, name, package):
        self.log.info('Adding python package: %s', name)
        self.run_python('setup.py install', cwd=self.unarchive(package))
