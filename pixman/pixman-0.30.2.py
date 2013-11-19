from ipkg.build import Formula, File


class pixman(Formula):

    name = 'pixman'
    version = '0.30.2'
    sources = File('http://cairographics.org/releases/pixman-0.30.2.tar.gz',
                   sha256='bd988920ccd742310ddf5b363c7b278f11d69a3405a09d542162c84b46bff6e9')
