import re

try:
    import setuptools
except ImportError:
    import distutils.core
    setup = distutils.core.setup
else:
    setup = setuptools.setup


setup(
    name='finix-wac',
    version=(re
             .compile(r".*__version__ = '(.*?)'", re.S)
             .match(open('wac.py').read())
             .group(1)),
    url='https://github.com/finix-payments/wac',
    license=open('LICENSE').read(),
    author='Finix',
    author_email='dev@finixpayments.com',
    description='Writing RESTful API clients.',
    long_description=(
        open('README.rst').read() + '\n\n' +
        open('HISTORY.rst').read()
    ),
    py_modules=['wac'],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    tests_require=[
        'mock>=0.8',
        'unittest2 >= 0.5.1',
    ],
    install_requires=[
        'certifi >= 0.0.8',  # force requests optional
        'chardet >= 1.0',  # force requests optional
        'simplejson >= 2.1',
        'iso8601',
        'requests >= 1.2.3'
    ],
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
