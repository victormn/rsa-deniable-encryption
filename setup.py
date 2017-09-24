"""Setup for deniable."""
import os
import codecs
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    """Return multiple read calls to different readable objects as a single
    string."""
    return codecs.open(os.path.join(HERE, *parts), 'r').read()

LONG_DESCRIPTION = read('README.rst')

setup(name='deniable',
      version='v0.4.1',
      description='Deniable encryption application of a RSA cryptosystem',
      long_description=LONG_DESCRIPTION,
      url='https://github.com/victormn/rsa-deniable-encryption',
      author='Victor Nunes',
      author_email='victor95nunes@gmail.com',
      tests_require=['pytest', 'pytest-cov'],
      install_requires=['pycrypto>=2.6.1'],
      license='MIT',
      entry_points={
          'console_scripts': [
              'deniablecollision = deniable.scripts.deniablecollision:main',
              'deniablekeys = deniable.scripts.deniablekeys:main',
              'deniablersa = deniable.scripts.deniablersa:main',
              ],
          },
      packages=['deniable', 'deniable.scripts'],
      zip_safe=False)
