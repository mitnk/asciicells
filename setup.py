# via: https://github.com/pypa/sampleproject/blob/master/setup.py
from setuptools import setup

DESC = """
Home Page: https://github.com/mitnk/asciicells

Install
::

    $ pip install asciicells


High level usages
-----------------

After installed, an executable ``asciicells`` would available for use.
If not, please replace following examples with ``python -m asciicells``.

::

    $ asciicells -f demo.csv

    +-----+---------+-----------+
    | No. | sample  | name      |
    |     |         |           |
    | 1   | a,b,c   | lettes    |
    |     |         |           |
    | 2   | + - x / | operators |
    +-----+---------+-----------+

With header:

::

    $ asciicells -f demo.csv -H

    +-----+---------+-----------+
    | No. | sample  | name      |
    +-----+---------+-----------+
    | 1   | a,b,c   | lettes    |
    |     |         |           |
    | 2   | + - x / | operators |
    +-----+---------+-----------+

Also support TSV: `asciicells -f demo.tsv -t -H`


Low level usages
----------------

::

    >>> import asciicells
    >>> ac = asciicells.AsciiCells()
    >>> L = [['a', 'b'], ['1', '2']]
    >>> print(ac.render(L))
    +---+---+
    | a | b |
    |   |   |
    | 1 | 2 |
    +---+---+

More information: https://github.com/mitnk/asciicells
"""

setup(
    name='asciicells',
    version='0.9.2',

    description='A Simple ASCII Table Generator',
    long_description=DESC,

    url='https://github.com/mitnk/asciicells',
    author='mitnk',
    author_email='w@mitnk.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='ascii table generator',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["asciicells"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=['peppercorn'],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'asciicells=asciicells:main',
        ],
    },
)
