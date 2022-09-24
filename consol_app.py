from main import *
from registration import registartion
from handlingproject import *
from new_register import store_data
from login import  login_app
print("Please choose registration or login : \n 1) Registration \n 2) Login")
choise = input("If there is the first time to login my app choose Register : \n")

if choise == "1":
    store_data()
    print("welcom to my app , plz choose you want from menu")
    menu()


elif choise == "2":
    print("plz enter ur mail and password ")
    login_app()
    menu()
else:
    print("plz choose right option")


