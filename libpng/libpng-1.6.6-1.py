from ipkg.build import Formula, File


class libpng(Formula):

    name = 'libpng'
    version = '1.6.6'
    homepage = 'http://www.libpng.org/pub/png/libpng.html'
    sources = File('http://download.sourceforge.net/libpng/libpng-1.6.6.tar.gz',
                   md5='2d8ec4b8251e0a343abda7d38594d557')
