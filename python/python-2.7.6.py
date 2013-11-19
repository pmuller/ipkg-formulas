from ipkg.build import Formula, File


class python(Formula):

    name = 'python'
    version = '2.7.6'
    homepage = 'http://www.python.org'
    sources = File('http://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz',
                   md5='1d8728eb0dfcac72a0fd99c17ec7f386')
    dependencies = ('pkg-config', 'readline', 'sqlite', 'gdbm', 'openssl')
    configure_args = ('--prefix=%(prefix)s',
                      '--enable-ipv6',
                      '--datarootdir=%(share)s',
                      '--datadir=%(share)s')

    setuptools = File('https://pypi.python.org/packages/source/s/setuptools/setuptools-1.3.2.tar.gz',
                      md5='441f2e58c0599d31597622a7b9eb605f')
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
