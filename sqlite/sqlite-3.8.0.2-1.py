class Sqlite(Formula):

    name = 'sqlite'
    version = '3.8.0.2'
    revision = 1
    homepage = 'http://sqlite.org'
    sources = File('http://sqlite.org/2013/sqlite-autoconf-3080002.tar.gz',
                   sha1='294c30e882a0d45877bce09afe72d08ccfc6b650')
    dependencies = ('readline',)
    configure_args = ('--prefix=%(prefix)s',
                      '--enable-dynamic-extensions')
