import os
from subprocess import check_output

from setuptools import setup

# ref: http://blogs.nopcode.org/brainstorm/2013/05/20/pragmatic-python-versioning-via-setuptools-and-git-tags/
# Fetch version from git tags, and write to version.py.
# Also, when git is not available (PyPi package), use stored version.py.
version_py = os.path.join(os.path.dirname(__file__), 'version.py')

try:
    # This will not generate PEP440 compliant version strings for any commit
    # that is not on the tag itself. setuptools/dist will give a warning.
    # Still, this is good enough for now. A (big) alternative would be
    # gh:warner/python-versioneer
    version_git = check_output(["git", "describe", "--tags"]).rstrip().decode('ascii')
except:
    try:
        version_git = open(version_py).read().strip().split('=')[-1].replace('\'', '').strip()
    except:
        version_git = '0.0.0'

version_msg = "# Do not edit this file, pipeline versioning is governed by git tags"
open(version_py, 'w').write(version_msg + os.linesep + "__version__ = '" + str(version_git) + "'\n")

setup(
    name="openqa_review",
    version="{ver}".format(ver=version_git),
    install_requires=[
        "beautifulsoup4",
        # there is also a new version 'configparser2' to resolve the name ambuigity but that package might not be available everywhere
        "configparser",
        "future",
        "sortedcontainers",
        "humanfriendly",
        "requests",
        "PyYAML",
        "pika",
        "certifi",
    ],
    tests_require=[
        "pytest-mock",
    ],
    author="Oliver kurz",
    author_email="okurz@suse.com",
    description="review helper script for openQA",
    license="MIT",
    keywords="openQA webscraping script helper review",
    url="https://github.com/okurz/openqa_review",
    packages=['openqa_review'],
    py_modules=['version'],
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'console_scripts': ['openqa-review=openqa_review.openqa_review:main',
                            'tumblesle-release=openqa_review.tumblesle_release:main'],
    },
    scripts=['bin/openqa-review-sles-ha', 'bin/openqa-review-daily-email'],
)
