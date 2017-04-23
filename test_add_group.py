from group import Group
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture=Application()
    request.addfinalazer(fixture.destroy())
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="testowa", header="test", footer="test"))
    app.logout()

def test_add_empty_group(app):
    app.login( username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

