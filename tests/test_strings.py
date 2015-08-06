# Copyright 2015 SolidBuilds.com. All rights reserved.
#
# Authors: Ling Thio <ling.thio@gmail.com>

from __future__ import print_function
from sqlalchemy_boolean_search import parse_boolean_search
from .models import Record


def add_records(db, records):
    for record in records:
        db.session.add(record)
    db.session.commit()


def delete_records(db, records):
    for record in records:
        db.session.delete(record)
    db.session.commit()


def test_strings(db):
    all_records = [
        Record(string='abc'),
        Record(string='abcx'),
        Record(string='xabc'),
        Record(string='xabcx'),
    ]
    add_records(db, all_records)

    expression = parse_boolean_search('string==abc')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 1
    for record in records:
        assert record.string == 'abc'

    expression = parse_boolean_search('string!=abc')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 3
    for record in records:
        assert record.string != 'abc'

    expression = parse_boolean_search('not string==abc')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 3
    for record in records:
        assert record.string != 'abc'

    expression = parse_boolean_search('string<xabc')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 2
    for record in records:
        assert record.string < 'xabc'

    expression = parse_boolean_search('string<=xabc')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 3
    for record in records:
        assert record.string <= 'xabc'

    expression = parse_boolean_search('string>xabc')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 1
    for record in records:
        assert record.string > 'xabc'

    expression = parse_boolean_search('string>=xabc')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 2
    for record in records:
        assert record.string >= 'xabc'

    expression = parse_boolean_search('string=abc')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 4
    for record in records:
        assert 'abc' in record.string

    expression = parse_boolean_search('string=*x and string=x*')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 1
    for record in records:
        assert record.string[0:1] == 'x' and record.string[-1:] == 'x'

    expression = parse_boolean_search('string=*x or string=x*')
    records = Record.query.filter(expression.filter(Record)).all()
    assert len(records) == 3
    for record in records:
        assert record.string[0:1] == 'x' or record.string[-1:] == 'x'

    delete_records(db, all_records)
