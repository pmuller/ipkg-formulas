from ipkg.build import Formula, File


class freetype(Formula):

    name = 'freetype'
    version = '2.5.0.1'
    sources = File('http://downloads.sf.net/project/freetype/freetype2/2.5.0/freetype-2.5.0.1.tar.gz',
                   sha1='2d539b375688466a8e7dcc4260ab21003faab08c')
    dependencies = ('libpng',)
