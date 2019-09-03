import sys
from twaddr import addrdata
from setuptools.command.install import install


class twAddr_install(install):
    def run(self):
        print('Building Addr ... ')
        sys.stdout.flush()
        twAddr.addrdata.createDB()
        install.run(self)

from setuptools import setup

setup(
    name = 'twAddr',
    packages = ['twaddr'],
    #scripts = ['runner'],
    version = '1.0.6',
    description = 'Taiwan address related services',
    author = 'Ailan',
    author_email = 'karta2599434@gmail.com',
    keywords = ['tw', 'addr'],
    classifiers = [],
    url = 'https://github.com/ailan12345/twAddr',

    package_data = {'zipcode': ['*.csv']},
    cmdclass = {'install': twAddr_install},
)
