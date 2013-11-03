from ipkg.build import Formula, File


class libffi(Formula):

    name = 'libffi'
    version = '3.0.13'
    homepage = 'http://sourceware.org/libffi/'
    sources = File('http://mirrors.kernel.org/sources.redhat.com/libffi/libffi-3.0.13.tar.gz',
                   sha1='f5230890dc0be42fb5c58fbf793da253155de106')
    configure_args = Formula.configure_args + ['--disable-debug']
