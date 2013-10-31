class Nginx(Formula):

    name = 'nginx'
    version = '1.4.3'
    revision = 1
    homepage = 'http://nginx.org/'
    sources = File('http://nginx.org/download/nginx-1.4.3.tar.gz',
                   sha1='8d0c34c84ce6dd8ba4442889e8f2599044c90930')
    dependencies = ('pcre',)
    configure_args = ('--prefix=%(prefix)s',
                      '--with-http_ssl_module',
                      '--with-pcre',
                      '--with-ipv6',
                      '--with-http_gzip_static_module')
