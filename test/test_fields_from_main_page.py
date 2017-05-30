import re

def test_phones_on_my_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contacts_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def test_emails_on_my_page(app):
    emails_from_home_page = app.contact.get_contacts_list()[0]
    emails_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert emails_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(emails_from_edit_page)

def test_names_on_my_page(app):
    names_from_view_page = app.contact.get_contacts_from_view_page(0)
    names_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert names_from_view_page.firstname == names_from_edit_page.firstname

def test_addresses_on_my_page(app):
    addresses_from_home_page = app.contact.get_contacts_list()[0]
    addresses_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert addresses_from_home_page.all_addresses_from_home_page == merge_addresses_like_on_home_page(addresses_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), [contact.email, contact.email2, contact.email3])))

def merge_addresses_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None,[contact.address]))
