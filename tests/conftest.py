import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.bike import Bike


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


# initialize 2 objects and put them in the database so that we can use them in the testing routes
@pytest.fixture
def two_bikes(app):
    bike1 = Bike(name="Speedy", price=1, size=6, type="racing")
    bike2 = Bike(name="Pokey", price=20, size=23, type="scrap")

    db.session.add(bike1)
    db.session.add(bike2)
    db.session.commit()

