from model.contact import Contact
from random import randrange

def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="deltest_firstname", lastname="deltest_last_name"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    # old_contacts[index:index+1] = []
    # assert old_contacts == new_contacts

  # app.contact.create(Contact(firstname="test2", middlename="test", lastname="test", nickname="test",
        #                       title="newone", company="qa", address="Poland", home="-", mobile="-", work="-",
        #                       fax="-",
        #                       email="test@test.pl", email3="-", email2="-", homepage="-", byear="1980",
        #                       ayear="1990", address2="Poland, lodz"))