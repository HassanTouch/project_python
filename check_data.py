import re
def check():
    name = input("user name: ")
    if name.isalpha():
        mail = input("Email: ")
        regx = regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if (re.search(regex, mail)):
            print("username is : ",name," \n" "Email: ",mail)
        else:
            print("invalid mail,try again")
            return check()
    else:
        print("invalid username plz try again")
check()