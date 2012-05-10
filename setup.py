import sys

extra = {}
if sys.version_info >= (3, 0):
    extra.update(use_2to3=True)

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from distutils.core import setup, find_packages, Command

setup(name='anyserializer',
      version='0.0.1',
      description='Next Generation Python Packaging Index',
      long_description=open('README.rst').read(),
      data_files=[('', ['README.rst'])],
      url='https://github.com/crateio/crate-site',
      license='BSD',
      packages=find_packages(),
      zip_safe=False,
      platforms=["any"],
      **extra
)
