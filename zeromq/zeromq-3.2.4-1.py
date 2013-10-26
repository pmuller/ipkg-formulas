class ZeroMQ(Formula):

    name = 'zeromq'
    version = '3.4'
    revision = 1
    homepage = 'http://www.zeromq.org/'
    sources = File('http://download.zeromq.org/zeromq-3.2.4.tar.gz',
                   sha1='08303259f08edd1faeac2e256f5be3899377135e')
    dependencies = ('pkg-config',)
