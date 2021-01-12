from model.contact import Contact
import random
import string
import jsonpickle
import os.path
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
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", mobilephone="")] + [
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middlename", 15), lastname=random_string("lastname", 15),
            address=random_string("address", 15), address2=random_string("address2", 15),
            email=random_string("1@1.", 10), email2=random_string("2@2.", 15), email3=random_string("email", 20),
            homephone=random_string("+7", 10), mobilephone=random_string("7", 10), workphone=random_string("8", 10), secondaryphone=random_string("7000", 10))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))