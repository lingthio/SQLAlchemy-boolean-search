"""
SQLAlchemy-boolean-search
==========

.. image:: https://img.shields.io/pypi/v/SQLAlchemy-boolean-search.svg
    :target: https://pypi.python.org/pypi/SQLAlchemy-boolean-search

.. image:: https://img.shields.io/travis/lingthio/SQLAlchemy-boolean-search.svg
    :target: https://travis-ci.org/lingthio/SQLAlchemy-boolean-search

.. image:: https://img.shields.io/pypi/dm/SQLAlchemy-boolean-search.svg
    :target: https://pypi.python.org/pypi/SQLAlchemy-boolean-search

.. image:: https://img.shields.io/pypi/l/SQLAlchemy-boolean-search.svg
    :target: https://pypi.python.org/pypi/SQLAlchemy-boolean-search

Boolean search expression parser for SQLAlchemy
-----------------------------------------------

Documentation
-------------
`SQLAlchemy-boolean-search Documentation <https://pythonhosted.org/SQLAlchemy-boolean-search/>`_

Revision History
----------------
`SQLAlchemy-boolean-search Revision History <http://pythonhosted.org//SQLAlchemy-boolean-search/index.html#revision-history>`_

Contact Information
-------------------
Ling Thio - ling.thio [at] gmail.com

Acknowledgements
----------------
This project would not be possible without the use of the following amazing offerings:

* `Flask <http://flask.pocoo.org/>`_
* `SQLAlchemy <http://www.sqlalchemy.org/>`_ and `Flask-SQLAlchemy <http://pythonhosted.org/Flask-SQLAlchemy/>`_

Alternative Flask extensions
----------------------------
"""

from __future__ import print_function
from setuptools import setup

setup(
    name='SQLAlchemy-boolean-search',
    version='0.1',
    url='http://github.com/lingthio/SQLAlchemy-boolean-search',
    license='BSD License',
    author='Ling Thio',
    author_email='ling.thio@gmail.com',
    description='Boolean search expression parser for SQLAlchemy',
    long_description=__doc__,
    keywords='Boolean search Flask SQLAlchemy',
    py_modules=['sqlalchemy_boolean_search'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
        'Flask',
        'pyparsing',
    ],
    test_suite="flask_user.tests.run_tests",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
