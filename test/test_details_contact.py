
def test_details_of_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.details_of_first_contact()
    app.session.logout()