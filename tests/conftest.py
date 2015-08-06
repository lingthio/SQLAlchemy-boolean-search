# Copyright 2015 SolidBuilds.com. All rights reserved.
#
# Authors: Ling Thio <ling.thio@gmail.com>

from flask import Flask
import os
import pytest
from flask_sqlalchemy import SQLAlchemy


the_app = Flask(__name__)               # The WSGI compliant web application object
the_db = SQLAlchemy(the_app)            # Setup Flask-SQLAlchemy

the_app.config.update(
    SECRET_KEY='KeepThisSecret',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.sqlite',
)

class Record(the_db.Model):
    __tablename__ = 'records'
    id = the_db.Column(the_db.Integer, primary_key=True)
    string = the_db.Column(the_db.String(255), nullable=False, server_default='')
    unicode = the_db.Column(the_db.Unicode(255), nullable=False, server_default=u'')
    boolean = the_db.Column(the_db.Boolean(), nullable=False, server_default='0')
    integer = the_db.Column(the_db.Integer(), nullable=False, server_default='0')
    float = the_db.Column(the_db.Float(), nullable=False, server_default='0.0')


@pytest.fixture(scope='session')
def app(request):
    # Establish an application context before running the tests.
    ctx = the_app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return the_app


@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database."""
    def teardown():
        the_db.drop_all()

    the_db.create_all()

    request.addfinalizer(teardown)
    return the_db


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session


