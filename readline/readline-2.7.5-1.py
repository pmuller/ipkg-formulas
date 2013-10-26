class Readline(Formula):

    name = 'readline'
    version = '6.2'
    revision = 1
    homepage = 'http://tiswww.case.edu/php/chet/readline/rltop.html'
    sources = File('http://ftpmirror.gnu.org/readline/readline-6.2.tar.gz',
                   sha256='79a696070a058c233c72dd6ac697021cc64abd5ed51e59db867d66d196a89381')
    patches = (
        File('http://ftp.igh.cnrs.fr/pub/gnu/readline/readline-6.2-patches/readline62-001',
             md5='83287d52a482f790dfb30ec0a8746669'),
        File('http://ftp.igh.cnrs.fr/pub/gnu/readline/readline-6.2-patches/readline62-002',
             md5='0665020ea118e8434bd145fb71f452cc'),
        File('http://ftp.igh.cnrs.fr/pub/gnu/readline/readline-6.2-patches/readline62-003',
             md5='c9d5d79718856e711667dede87cb7622'),
        File('http://ftp.igh.cnrs.fr/pub/gnu/readline/readline-6.2-patches/readline62-004',
             md5='c08e787f50579ce301075c523fa660a4')
    )
    configure_args = ('--prefix=%(env_dir)s',
                      '--mandir=%(man_dir)s',
                      '--enable-multibyte')
