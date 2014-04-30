from distutils.core import setup
import os
import sys

version = open(os.path.join(os.path.dirname(__file__), 'green', 'VERSION')).read().strip()

setup(
    name = 'green',
    packages = ['green'],
    data_files = [('green', ['green/VERSION'])],
    version = version,
    install_requires = [
        'nose2',
        'python-termstyle'
        ],
    entry_points = {
        'console_scripts' : [
            'green = green:main',
            'green%d = green:main' % sys.version_info[:1],     # green2 or green3
            'green-%d.%d = green:main' % sys.version_info[:2], # green-3.4 etc.
            ],
    },
    description = 'A plugin for the "nose2" project that provides the colored, aligned, clean output that you deserve.  You can just run green (or green2 or green3, or green-X.X where X.X is your python version).  Alternatively, you can run "nose2 --green"',
    long_description = open('README.md').read(),
    author = 'Nathan Stocks',
    author_email = 'nathan.stocks@gmail.com',
    license = 'MIT',
    url = 'https://github.com/CleanCut/green',
    download_url = 'https://github.com/CleanCut/green/tarball/' + version,
    keywords = ['nose2', 'plugin', 'green', 'test', 'tests', 'trial', 'functional test', 'system test', 'unit test', 'unittest', 'color', 'tabular', 'clean', 'red', 'rednose'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities'],
)
