from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
     getopt.usage()
     sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
            homephone=random_string("homephone", 6), mobilephone=random_string("mobilephone", 6),
            workphone=random_string("workphone", 6), secondaryphone=random_string("secondaryphone", 6))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent = 2))


    # jsonpickle.set_encoder_options("json", indent = 2)
    # out.write(jsonpickle.encode(testdata))



