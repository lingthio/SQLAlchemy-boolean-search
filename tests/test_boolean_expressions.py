# Copyright 2015 SolidBuilds.com. All rights reserved.
#
# Authors: Ling Thio <ling.thio@gmail.com>

from __future__ import print_function
from sqlalchemy_boolean_search import parse_boolean_search


def test_boolean_expressions():
    # Test precedence
    expression = parse_boolean_search('a=1 or b=2 or not c=3 and d=4 and e=5')
    assert repr(expression) == 'or_(a=1, b=2, and_(not_(c=3), d=4, e=5))'

    # Test parenthesis
    expression = parse_boolean_search('a=1 or not b=2 and c=3')
    assert repr(expression) == 'or_(a=1, and_(not_(b=2), c=3))'

    expression = parse_boolean_search('a=1 or not (b=2 and c=3)')
    assert repr(expression) == 'or_(a=1, not_(and_(b=2, c=3)))'

    expression = parse_boolean_search('(a=1 or not b=2) and c=3')
    assert repr(expression) == 'and_(or_(a=1, not_(b=2)), c=3)'

    # Test all operators
    expression = parse_boolean_search('a < 1 or a <= 1 or a = 1 or a == 1 or a >= 1 or a > 1 or a != 1')
    assert repr(expression) == 'or_(a<1, a<=1, a=1, a==1, a>=1, a>1, a!=1)'

    # Test example
    expression = parse_boolean_search('field1=*something* and not (field2==1 or field3<=10.0)')
    assert repr(expression) == 'and_(field1=*something*, not_(or_(field2==1, field3<=10.0)))'

