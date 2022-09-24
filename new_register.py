import re
from handlingproject import *
def askfornum(message):
    num = input(message)
    try:
        num = int(num)
    except:
        return askfornum(message)
    else:
        return str(num)

def askforstr(message):
    mystr = input(message)
    if mystr.isspace() or not mystr:
        return askforstr(message)
    return mystr

def v_mail():
    email = input("Enter mail: ")
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        return email
    else:
        print("invalid mail , plz try again")
        return v_mail()

def v_password():
    pass1 = input("Password")
    pass2 = input("confirm_password")
    if pass1 == pass2:
        return pass1
    else:
        print("not the same password , plz try again ")
        return v_password()
def user_data():
    first_name = askforstr("First name : ")
    last_name = askforstr("Last name : ")
    email = v_mail()
    password = v_password()
    mobile_phone = askfornum("Mobile phone : ")
    return str(email), str(password), first_name, last_name,  str(mobile_phone)

def store_data():
    create = list(user_data())

    new_added = ":".join(create)

    add = save_user_data(new_added)
    if add:
        print("--ur created successfully---")
    else:
        print("there is an error, plz try again")
        return store_data()
