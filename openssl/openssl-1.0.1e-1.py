class OpenSSL(Formula):

    name = 'openssl'
    version = '1.0.1e'
    revision = 1
    homepage = 'http://openssl.org'
    sources = File('http://openssl.org/source/openssl-1.0.1e.tar.gz',
                   sha256='f74f15e8c8ff11aa3d5bb5f276d202ec18d7246e95f961db76054199c69c1ae3')
    # TODO: implement envvars
    envvars = {
        'RANDFILE': '%(env_dir)s/ssl/rnd',
        'OPENSSL_CONF': '%(env_dir)/ssl/openssl.cnf',
    }

    def install(self):
        args = ['./Configure', '--prefix=%s' % self.env.prefix, 'zlib-dynamic', 'shared']
        if self.env.os_name == 'osx':
            args.append('darwin64-x86_64-cc')
        self.run_command('perl', args)
        self.run_make()
        self.run_make(['install',
                       'MANDIR=%(man)s' % self.env.directories,
                       'MANSUFFIX=ssl'])
