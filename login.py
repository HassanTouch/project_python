from handlingproject import *
from main import *
from createProject import *
def login_app():

        print("----- Welcome----")
        email = check("Email: ")
        password = input("Password: ")

        try:
            loginfo = open("userdata.txt", "r")
        except Exception as e:
            print(" error happend while openning the file  ")
        else:

            credintials = loginfo.readlines()
            loginfo.close()

            for info in credintials:
                myinfo = info.strip("\n")
                myinfo = myinfo.split(":")

                if myinfo[0] == str(email) and myinfo[1] == str(password):
                    print("\n-----Welcome!!----\n")

                    return menu()


            else:
                print("Wrong e-mail or password!!")
                login_app()
