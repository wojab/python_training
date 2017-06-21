from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="NowyKontakt", lastname="NowyKontaktLastname"))

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Nowa_grupa"))

    old_contacts = db.get_contacts_list()
    old_contacts_in_groups = db.get_contacts_in_groups_list()
    contact = random.choice(old_contacts)
    app.contact.add_contact_to_group(contact.id)
    new_contacts_in_groups = db.get_contacts_in_groups_list()
    old_contacts_in_groups.append(contact)
    assert sorted(old_contacts_in_groups, key=Contact.id_or_max) == sorted(new_contacts_in_groups, key=Contact.id_or_max)







