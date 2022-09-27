import pytest
from main import app
from application.database import db
@pytest.fixture()
def client():
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()
    
    yield client  # this is where the testing happens!

    # Tear down
    ctx.pop()


@pytest.fixture()
def init_database():
    # Create the database and the database table
    db.create_all()

    yield db  # this is where the testing happens!

    # Tear down
    db.drop_all()


def test_no_articles_home():
    client = app.test_client()
    db.create_all()

    response = client.get('/')
    assert b"<title>All Articles</title>" in response.data
    assert not ( b"ratings-icon" in response.data )
