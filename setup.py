# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='fbone',
    version='0.1',
    url='https://github.com/imwilsonxu/fbone'
    description='Fbone is a Flask template/bootstrap/boilerplate application.',
    author='Wilson Xu',
    author_email='imwilsonxu@gmail.com',
    packages=['fbone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask-WTF',
        'Flask-Script',
        'Flask-Babel',
        'Flask-Testing',
        'Flask-Uploads',
        'Flask-Mail',
        'Flask-Cache',
        'Flask-Login',
        'nose',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)
