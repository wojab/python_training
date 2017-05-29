import re

# def test_addresses_on_my_page(app):
#     address_from_view_page = app.contact.get_contacts_from_view_page(0)
#     address_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert address_from_view_page.address == address_from_edit_page.address

# def test_names_on_my_page(app):
#     names_from_view_page = app.contact.get_contacts_from_view_page(0)
#     names_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert names_from_view_page.firstname == names_from_edit_page.firstname


 #   assert addresses_from_home_page.all_addresses_from_home_page == merge_emails_like_on_home_page(addresses_from_edit_page)



s = "adam marek danuta"
m = re.search("(.*)", s)
print (m)
print(m.group())


