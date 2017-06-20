from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="NowyKontakt", lastname="NowyKontaktLastname"))

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Nowa_grupa"))

    old_contacts = db.get_contacts_in_groups_list()
    contact = random.choice(old_contacts)
    print(contact.id)
    app.contact.del_first_contact_from_group(contact.id)
    new_contacts = db.get_contacts_in_groups_list()
    old_contacts.remove(contact)
    print(old_contacts)
    print("tererere")
    print(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



