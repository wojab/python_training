from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
     symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
     return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

testdata = [Contact(firstname= "", lastname = "")] + [
     Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20 ),
             homephone = random_string("homephone", 6),mobilephone=random_string("mobilephone", 6),
             workphone=random_string("workphone", 6),secondaryphone=random_string("secondaryphone", 6))
     for i in range(1)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)






# def test_add_contact(app):
#     old_contacts = app.contact.get_contacts_list()
#     contact = Contact(firstname="wojtek", lastname="wojtasikk", homephone="123456789", mobilephone="987654321", workphone="5647382910", secondaryphone="546123512")
#     app.contact.create(contact)
#     assert len(old_contacts) + 1 == app.contact.count()
#     new_contacts = app.contact.get_contacts_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    # app.contact.create(Contact(firstname="wojtek", middlename="marek", lastname="wojtasik", nickname="nico",
    #                           title="newone", company="qa", address="Poland", home="-", mobile="-", work="-",
    #                           fax="-",
    #                           email="test@test.pl", email3="-", email2="-", homepage="-", byear="1980",
    #                           ayear="1990", address2="Poland, lodz"))

