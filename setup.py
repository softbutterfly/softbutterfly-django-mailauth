from setuptools import setup
from setuptools import find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='softbutterfly-django-mailauth',

    version='0.0.0',

    description='A drop-in module for users indentified by email.',
    long_description=long_description,

    author='softbutterfly',
    author_email='dev@softbutterfly.io',

    license='BSD',

    url='https://github.com/softbutterfly/softbutterfly-django-mailauth',
    download_url='https://github.com/softbutterfly/softbutterfly-django-mailauth/tarball/1.0.0',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
    ],

    keywords=['softbutterfly', 'django', 'auth', 'mail as username'],

    zip_safe=True,

    packages=find_packages(),
    include_package_data=True,


    package_data={
        'softbutterfly': [
        ],
    },


    install_requires=[
        'django',
    ],
)
