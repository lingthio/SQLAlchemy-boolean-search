# Copyright 2015 SolidBuilds.com. All rights reserved.
#
# Authors: Ling Thio <ling.thio@gmail.com>

from .conftest import the_db as db


class GrandParent(db.Model):
    __tablename__ = 'grandparents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, server_default='')


class Parent(db.Model):
    __tablename__ = 'parents'
    id = db.Column(db.Integer, primary_key=True)
    grandparent_id = db.Column(db.Integer(), db.ForeignKey('grandparents.id', ondelete='CASCADE'))
    grandparent = db.relationship('GrandParent')
    name = db.Column(db.String(50), nullable=False, server_default='')


class Record(db.Model):
    __tablename__ = 'records'
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer(), db.ForeignKey('parents.id', ondelete='CASCADE'))
    parent = db.relationship('Parent')

    string = db.Column(db.String(50), nullable=False, server_default='')
    unicode = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    boolean = db.Column(db.Boolean(), nullable=False, server_default='0')
    integer = db.Column(db.Integer(), nullable=False, server_default='0')
    float = db.Column(db.Float(), nullable=False, server_default='0.0')


