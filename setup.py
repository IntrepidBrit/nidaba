from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='nidaba',
    packages=find_packages(),
    url='http://sopython.com/pages/nidaba',
    license='BSD',
    author='Keiron Pizzey',
    author_email='ffisegydd@sopython.com',
    description='Machine learning library for studying Stack Overflow data.',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 1 - Planning',

        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',

        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',

        'Topic :: Internet',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
