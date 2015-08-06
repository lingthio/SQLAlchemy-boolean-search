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


def test_others(db):
    # Create records
    all_records = [
        Record(integer=1),
        Record(float=1.0),
    ]
    add_records(db, all_records)

    # Test integer
    expression = parse_boolean_search('integer==1')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 1
    for record in records:
        assert record.integer == 1

    # Test float with float
    expression = parse_boolean_search('float==1.0')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 1
    for record in records:
        assert record.float == 1.0

    # Test float with integer
    expression = parse_boolean_search('float==1')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 1
    for record in records:
        assert record.float == 1.0

    # Delete records
    delete_records(db, all_records)
