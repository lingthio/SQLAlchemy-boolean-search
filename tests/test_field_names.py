# Copyright 2015 SolidBuilds.com. All rights reserved.
#
# Authors: Ling Thio <ling.thio@gmail.com>

from __future__ import print_function
from sqlalchemy_boolean_search import parse_boolean_search
from .models import Record, Parent, GrandParent


def test_field_names(db):
    # Create records
    grandparent = GrandParent(name='GrandParent')
    parent = Parent(name='Parent', grandparent=grandparent)
    record = Record(string='Record', parent=parent)
    db.session.add(record)
    db.session.commit()

    # Test non-hierarchical name
    expression = parse_boolean_search('string==Record')
    record = Record.query.filter(expression.filter(Record)).first()
    assert record is not None
    assert record.string=='Record'

    # Test level-1 hierarchy name
    expression = parse_boolean_search('parent.name==Parent')
    record = Record.query.filter(expression.filter(Record)).first()
    assert record is not None
    assert record.string=='Record'

    # Test level-2 hierarchy name
    expression = parse_boolean_search('parent.grandparent.name==GrandParent')
    record = Record.query.filter(expression.filter(Record)).first()
    assert record is not None
    assert record.string=='Record'

    # Delete records
    db.session.delete(record)
    db.session.commit()
