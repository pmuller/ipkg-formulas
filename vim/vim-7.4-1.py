class Vim(Formula):

    name = 'vim'
    version = '7.4'
    revision = 1
    homepage = 'http://vim.org'
    sources = File('http://ftp.vim.org/pub/vim/unix/vim-7.4.tar.bz2',
                   md5='607e135c559be642f210094ad023dc65')
    dependencies = ('python',)
    configure_args = ('--prefix=%(prefix)s',
                      '--enable-pythoninterp',
                      '--enable-multibyte',
                      '--with-tlib=ncurses',
                      '--enable-cscope',
                      '--with-features=huge',
                      '--with-compiledby=ipkg')
    envvars = {'VIMRUNTIME': '%(prefix)s/share/vim/vim74'}
