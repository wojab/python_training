import pytest
from fixture.application2 import Application2

@pytest.fixture(scope = "session")
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_del_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_first_contact()
    app.session.logout()