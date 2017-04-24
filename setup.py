from setuptools import setup
from setuptools import find_packages


PACKAGE_NAME = 'softbutterfly-django-mailauth'
PACKAGE_VERSION = '3.14.19'
PACKAGE_LIST = find_packages()
REQUERIMENTS = [
    'django',
]
KEYWORDS = [
    'softbutterfly',
    'django',
    'auth',
    'mail as username'
]


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='A drop-in module for users indentified by email.',
    author='SoftButterfly',
    author_email='dev@softbutterfly.io',
    license='BSD',
    url='https://github.com/softbutterfly/{0}'.format(PACKAGE_NAME),
    download_url='https://github.com/softbutterfly/{0}/tarball/{1}'.format(PACKAGE_NAME, PACKAGE_VERSION),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
    include_package_data=True,
    keywords=KEYWORDS,
    packages=PACKAGE_LIST,
    install_requires=REQUERIMENTS,
)
