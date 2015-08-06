# Copyright 2015 SolidBuilds.com. All rights reserved.
#
# Authors: Ling Thio <ling.thio@gmail.com>

from __future__ import print_function
from sqlalchemy_boolean_search import parse_boolean_search, BooleanSearchException
from .models import Record


def add_records(db, records):
    for record in records:
        db.session.add(record)
    db.session.commit()


def delete_records(db, records):
    for record in records:
        db.session.delete(record)
    db.session.commit()


def test_exceptions(db):
    # Create records
    all_records = [
        Record(integer=1),
        Record(float=1.0),
    ]
    add_records(db, all_records)

    # Test invalid field name
    try:
        expression = parse_boolean_search('XYZ==text')
        records = Record.query.filter(expression.filter(Record)).all()
        assert False        # An exception should have skipped this statement
    except BooleanSearchException as e:
        # print(e)
        pass

    # Test invalid operator
    try:
        expression = parse_boolean_search('a:1')
        assert False        # An exception should have skipped this statement
    except BooleanSearchException as e:
        # print(e)
        pass

    # Test invalid integer
    try:
        expression = parse_boolean_search('integer==text')
        records = Record.query.filter(expression.filter(Record)).all()
        assert False        # An exception should have skipped this statement
    except BooleanSearchException as e:
        # print(e)
        pass

    # Test invalid float
    try:
        expression = parse_boolean_search('float==text')
        records = Record.query.filter(expression.filter(Record)).all()
        assert False        # An exception should have skipped this statement
    except BooleanSearchException as e:
        # print(e)
        pass

    # Delete records
    delete_records(db, all_records)
