from setuptools import setup

versionfile = 'ijroi/version.py'
exec(compile(open(versionfile, 'rb').read(), versionfile, 'exec'))

setup(
    name='ijroi',
    version=__version__,
    url='https://github.com/tdsmith/ijroi',
    license='MIT',
    author='Tim D. Smith',
    author_email='ijroi@tim-smith.us',
    description='Reads ImageJ ROIs.',
    packages=['ijroi', 'ijroi.tests'],
    package_data={'ijroi.tests': ['fixtures/*']},
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ],
    install_requires = ['numpy'],
)
