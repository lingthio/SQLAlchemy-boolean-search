"""
SQLAlchemy-boolean-search
=========================
SQLAlchemy-boolean-search translates a boolean search string such as::

    "field1=*something* and not (field2==1 or parent.field3<=10.0)"

into its corresponding SQLAlchemy query filter::

    and_(DataModel.field1.ilike('%something%'),
         not_(or_(DataModel.field2.__eq__(2),
                  DataModel.parent.field3.__le__(10.0))))

Relationship field names such as 'parent.grandparent.name' are accepted.

The code is stable, is used in production, and enjoys a test coverage of 100%.

Documentation
-------------
`SQLAlchemy-boolean-search Documentation <http://sqlalchemy-boolean-search.readthedocs.org/>`_

Authors
-------
* Ling Thio - ling.thio [at] gmail.com

"""

from setuptools import setup

setup(
    name='SQLAlchemy-boolean-search',
    version='0.1.1',
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
