from model.contact import Contact
from model.group import Group
import random


def test_del_contact_from_group(app, db):

    if len(db.get_contacts_in_groups_list()) == 0:

        if len(db.get_contacts_list()) == 0:
            app.contact.create(Contact(firstname="NowyKontakt", lastname="NowyKontaktLastname"))

            if len(db.get_group_list()) == 0:
                app.group.create(Group(name="PowiazGrupa"))

        old_contacts = db.get_contacts_list()
        contact = random.choice(old_contacts)
        app.contact.add_contact_to_group(contact.id)

    old_contacts = db.get_contacts_in_groups_list()
    contact = random.choice(old_contacts)
    app.contact.del_contact_from_group(contact.id)
    new_contacts = db.get_contacts_in_groups_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





