# Copyright 2015 SolidBuilds.com. All rights reserved.
#
# Authors: Ling Thio <ling.thio@gmail.com>

from __future__ import print_function
import pyparsing as pp
from pyparsing import ParseException  # explicit export
from sqlalchemy import func
from sqlalchemy.sql import or_, and_, not_, sqltypes


# ***** Define the expression element classes *****

class Condition(object):
    def __init__(self, data):
        self.name = data[0][0]
        self.op = data[0][1]
        self.value = data[0][2]

    def filter(self, DataModelClass):
        condition = None
        if hasattr(DataModelClass, self.name):
            # Prepare field and value
            field = getattr(DataModelClass, self.name)
            lower_field = func.lower(field)
            value = self.value
            lower_value = func.lower(value)
            if field.type.python_type == float:
                try:
                    value = float(value)
                    lower_field = field
                    lower_value = value
                except:
                    pass
            elif field.type.python_type == int:
                try:
                    value = int(value)
                    lower_field = field
                    lower_value = value
                except:
                    pass

            # Return SQLAlchemy condition based on operator value
            if self.op == '==':
                condition = lower_field.__eq__(lower_value)
            elif self.op == '<':
                condition = lower_field.__lt__(lower_value)
            elif self.op == '<=':
                condition = lower_field.__le__(lower_value)
            elif self.op == '>':
                condition = lower_field.__gt__(lower_value)
            elif self.op == '>=':
                condition = lower_field.__ge__(lower_value)
            elif self.op == '!=':
                condition = lower_field.__ne__(lower_value)
            elif self.op == '=':
                field = getattr(DataModelClass, self.name)
                value = self.value
                if value.find('*') >= 0:
                    value = value.replace('*', '%')
                    condition = field.ilike(value)
                else:
                    condition = field.ilike('%' + value + '%')
            else:
                raise ValueError("Operator '%(operator)s' not supported." % dict(operator=self.op))
        else:
            raise NameError("Field '%(field_name)s' does not exist."
                            % dict(field_name=self.name))

        return condition

    def __repr__(self):
        return self.name + self.op + self.value


class BoolNot(object):
    def __init__(self, data):
        self.condition = data[0][1]

    def filter(self, DataModelClass):
        return not_(self.condition.filter(DataModelClass))

    def __repr__(self):
        return 'NOT: ' + repr(self.condition)


class BoolAnd(object):
    def __init__(self, data):
        self.conditions = [condition for condition in data[0] if condition and condition != 'and']

    def filter(self, DataModelClass):
        sql_conditions = [condition.filter(DataModelClass) for condition in self.conditions]
        return and_(*sql_conditions)  # * converts list to argument sequence

    def __repr__(self):
        return 'AND[' + ', '.join([repr(condition) for condition in self.conditions]) + ']'


class BoolOr(object):
    def __init__(self, data):
        self.conditions = [condition for condition in data[0] if condition and condition != 'or']

    def filter(self, DataModelClass):
        sql_conditions = [condition.filter(DataModelClass) for condition in self.conditions]
        return or_(*sql_conditions)  # * converts list to argument sequence

    def __repr__(self):
        return 'OR[' + ', '.join([repr(condition) for condition in self.conditions]) + ']'

# ***** Define the boolean condition expressions *****

# Define expression elements
number = pp.Regex(r"[+-]?\d+(:?\.\d*)?(:?[eE][+-]?\d+)?")
identifier = pp.Word(pp.alphas + '_', pp.alphanums + '_')
name = pp.Word(pp.alphas + '_', pp.alphanums + '_')
operator = pp.Regex("==|!=|<=|>=|<|>|=")
value = pp.Word(pp.alphanums + '_.*') | pp.QuotedString('"') | number
condition = pp.Group(name + operator + value)
condition.setParseAction(Condition)

# Define the expression
expression = pp.operatorPrecedence(condition, [
    (pp.CaselessLiteral("not"), 1, pp.opAssoc.RIGHT, BoolNot),
    (pp.CaselessLiteral("and"), 2, pp.opAssoc.LEFT, BoolAnd),
    (pp.CaselessLiteral("or"), 2, pp.opAssoc.LEFT, BoolOr),
])


def parse_boolean_search(boolean_search):
    return expression.parseString(boolean_search)[0]

