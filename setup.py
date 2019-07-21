import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='beautifurl',
    packages=['beautifurl'],
    package_data={
        'beautifurl': ['dictionaries/*']
    },
    install_requires=[
        'shuffled>=0.2'
    ],
    version='0.1.3',
    license='MIT',
    description='Generates beautiful urls similar to Gfycat.',
    long_description=README,
    url='https://github.com/hintofbasil/Python-Beautifurl',
    author='William Hutcheson',
    author_email='crabbybearnose@shadowmail.co.uk',
    test_suite="test",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)

