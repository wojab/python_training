# -*- coding: utf-8 -*-
import pytest
from fixture.application2 import Application2
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy())
    return fixture

def test_test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="wojtek", middlename="marek", lastname="wojtasik", nickname="nico",
                                        title="newone", company="qa", address="Poland", home="-", mobile="-", work="-",
                                        fax="-",
                                        email="test@test.pl", email3="-", email2="-", homepage="-", byear="1980",
                                        ayear="1990", address2="Poland, lodz"))
    app.logout()
