import io
from setuptools import setup

versionfile = 'ijroi/version.py'
exec(compile(open(versionfile, 'rb').read(), versionfile, 'exec'))

with io.open("README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='ijroi',
    version=__version__,
    url='https://github.com/tdsmith/ijroi',
    license='MIT',
    author='Tim D. Smith',
    author_email='ijroi@tim-smith.us',
    description='Reads ImageJ ROIs.',
    long_description=long_description,
    packages=['ijroi', 'ijroi.tests'],
    package_data={'ijroi.tests': ['fixtures/*']},
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=['numpy'],
)
