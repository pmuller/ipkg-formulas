from ipkg.build import Formula, File
from ipkg.platforms import Platform


class openssl(Formula):

    name = 'openssl'
    version = '1.0.1e'
    homepage = 'http://openssl.org'
    sources = File('http://openssl.org/source/openssl-1.0.1e.tar.gz',
                   sha256='f74f15e8c8ff11aa3d5bb5f276d202ec18d7246e95f961db76054199c69c1ae3')
    envvars = {'OPENSSL_CONF': '%(prefix)s/ssl/openssl.cnf'}

    def install(self):
        environment = self.environment
        command = ['perl', './Configure', '--prefix=%s' % environment.prefix,
                   'zlib-dynamic', 'shared']
        if Platform.current().os_name == 'osx':
            command.append('darwin64-x86_64-cc')
        self.run_command(command)
        self.run_make()
        self.run_make(['install',
                       'MANDIR=%(man)s' % environment.directories,
                       'MANSUFFIX=ssl'])
