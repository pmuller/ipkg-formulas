from ipkg.build import Formula, File


class cairo(Formula):

    name = 'cairo'
    version = '1.12.16'
    sources = File('http://cairographics.org/releases/cairo-1.12.16.tar.xz',
                   sha256='2505959eb3f1de3e1841023b61585bfd35684b9733c7b6a3643f4f4cbde6d846')
    dependencies = ('pkg-config', 'pixman', 'xz', 'freetype', 'glib')
