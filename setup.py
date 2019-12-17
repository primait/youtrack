#!/usr/bin/env python

import os
from setuptools import setup
from youtrack import config

version = config.__version__
develop_status = '5 - Production/Stable'

try:
    import pypandoc

    print("Converting README...")
    long_description = pypandoc.convert_file('README.md', 'rst')
    if branch:
        long_description = long_description.replace('youtrack.svg?branch=master',
                                                    'youtrack.svg?branch={}'.format(branch))
    links = min((long_description.find('\n.. |build'),
                 long_description.find('\n.. |codacy'),
                 long_description.find('\n.. |pypi'),
                 long_description.find('\n.. |license'),
                 ))
    if links >= 0:
        long_description = '{}\n{}'.format(
            long_description[:links],
            long_description[links:].replace('\n', '').replace('.. |', '\n.. |'),
        )  # .replace('\r\n', '\n')


except (IOError, ImportError, OSError):
    print("Pandoc not found. Long_description conversion failure.")
    with open('README.md', encoding="utf-8") as f:
        long_description = f.read()
else:
    print("Saving README.rst...")
    try:
        if len(long_description) > 0:
            with open('README.rst', 'w', encoding="utf-8") as f:
                f.write(long_description)
            if travis:
                os.remove('README.md')
    except Exception as e:
        print("  failed!")

setup(
    name='prima-youtrack',
    version=version,
    license='MIT License',
    description='Prima.it YouTrack Python 3 Client Library',
    long_description='Documentation: https://github.com/primait/youtrack',
    author='Prima.it',
    author_email='devops@prima.it',
    url='https://github.com/primait/youtrack',
    download_url='https://github.com/primait/youtrack',
    classifiers=[
        'Development Status :: {}'.format(develop_status),
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=[
        'tracker',
        'youtrack',
    ],
    packages=[
        'youtrack',
    ],
    install_requires=[
        'httplib2',
    ],
    setup_requires=[
    ],
    tests_require=[
        'pytest',
        'PyHamcrest',
    ],
    zip_safe=True,
    package_data={
        '': [
            '../LICENSE',
            # '../README.*',
        ],
    },
)
