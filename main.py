from createProject import *

def menu():
    choice = input("plz choose your option: \n 1) list all projects \n 2) create  \n 3) Edit project \n 4) delete project \n 5) search for project \n")
    if choice == "1":
        print("all project")
        view()
    elif choice == "2":
        print("create new project")
        createproject()
    elif choice == "3":
        print("modify project ")
    elif choice == "4":
        print("you choose delete option")
        delete_project()
    elif choice == "5":
        print("search for project")
    else:
        print("error")

