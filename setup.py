from distutils.core import setup

setup(
    name = 'twAddr',
    packages = ['zipcode'],
    #scripts = ['runner'],
    version = '1.0.1',
    description = 'Taiwan address related services',
    author = 'Ailan',
    author_email = 'karta2599434@gmail.com',
    keywords = ['tw', 'addr'],
    classifiers = [],
    url = 'https://github.com/ailan12345/twAddr',

    package_data = {'zipcode': ['*.xls']},

)
