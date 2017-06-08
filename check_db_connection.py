# import pymysql.cursors
#
# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()

from  fixture.db import DbFixture


db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    contacts = db.get_group_list()
    for group in contacts:
        print(contacts)
    print(len(contacts))
finally:
    db.destroy()