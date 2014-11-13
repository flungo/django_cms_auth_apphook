from distutils.core import setup
from cms.utils.plugins import downcast_plugins

VERSION = '1.0.0'
GIT_URL = 'https://github.com/flungo/django_cms_auth_apphook'

setup(
    name='django_cms_auth_apphook',
    version=VERSION,
    packages=['auth_apphook'],
    url=GIT_URL,
    download_url= GIT_URL + "/tarball/" + VERSION + ".tar.gz",
    license='MIT',
    author='Fabrizio Lungo',
    author_email='fab@lungo.co.uk',
    description='App hook to make integration with the standard Django Auth Library easier. Also includes templates for all auth views.'
)
