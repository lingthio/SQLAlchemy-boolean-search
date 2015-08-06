# SQLAlchemy-boolean-search
SQLAlchemy-boolean-search translates a boolean search string such as:

    "field1=*something* and not (field2==1 or parent.field3<=10.0)"

into its corresponding SQLAlchemy query filter:

    and_(DataModel.field1.ilike('%something%'),
         not_(or_(DataModel.field2.__eq__(2),
                  DataModel.parent.field3.__le__(10.0))))

Relationship field names such as 'parent.grandparent.name' are accepted.

The code is stable, is used in production, and enjoys a test coverage of 100%.

## Documentation
[SQLAlchemy-boolean-search documentation](http://sqlalchemy-boolean-search.readthedocs.org/)

## Authors
* Ling Thio - ling.thio [at] gmail.com

## Acknowledgements
This project would not be possible without the use of the following amazing offerings:

* [Flask](http://flask.pocoo.org/)
* [SQLAlchemy](http://www.sqlalchemy.org/)
* [pyparsing](https://pyparsing.wikispaces.com/)

## Alternative modules
* [SQLAlchemy-Searchable](https://sqlalchemy-searchable.readthedocs.org/)
  adds full text searching and relies on PostgreSQL vectors and triggers.
* [sqlalchemy-elasticquery](https://github.com/loverajoel/sqlalchemy-elasticquery)

