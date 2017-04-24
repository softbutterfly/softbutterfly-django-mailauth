from setuptools import setup


setup(
    name='softbutterfly-django-mailauth',
    version='1.0.0',
    description='A drop-in module for users indentified by email.',
    author='SoftButterfly',
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
    zip_safe=False,
    keywords=['softbutterfly', 'django', 'auth', 'mail as username'],
    packages=[
        'softbutterfly.mailauth',
    ],
    include_package_data=True,
    install_requires=[
        'django',
    ],
)
