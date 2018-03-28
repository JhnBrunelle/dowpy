from setuptools import setup

setup(name='dowpy',
      version='0.1',
      description='Module for downloading HTTP(s) files efficiently',
      url='http://github.com/jhnbrunelle/dowpy',
      author='JohnBrunelle',
      author_email='devjohnb@gmail.com',
      license='MIT',
      packages=['dowpy'],
      install_requires=['requests'],
      zip_safe=False)