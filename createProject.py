import time
import re
from main import *
import datetime
from handlingproject import *

def check(message):
    mail = input(message)

    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, mail)):
        return str(mail)
    else:
        print("invalid mail,try again")
        return check()

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

def generate_id():
    new_id = round(time.time())
    return new_id

#def detailsproject(message):
    # nam = askforstr("plz enter name of project")
    # id = input("plz enter id project")
    # description = askforstr("descripe your project")
    # return nam, id, description

# def valid_dat():
#      start_time = input("Start Date (mm/dd/yyyy) : ")
#      #end_time = input("End Date (mm/dd/yyyy) : ")
#      format = "%m-%d-%Y"
#
#      try:
#          res = datetime.datetime.strptime(start_time, format)
#          return res
#      except ValueError:
#          print("Incorrect data format, should be mm-dd-yyyy")
#          return valid_dat()



def projectcntaint():
    pro_id = generate_id()
    title = askforstr("plz enter title ur project")
    details = input("plz enter details project")
    totaltarget = int(input("plz enter total target"))
 #   dat = valid_dat()
    start_time = input("Start Date (mm/dd/yyyy) : ")
    end_time = input("End Date (mm/dd/yyyy) : ")
    # valid_date1 = datetime.datetime.strptime(start_time, '%m/%d/%Y')
    # valid_date2 = datetime.datetime.strptime(end_time, '%m/%d/%Y')
    # if valid_date1 and valid_date2:

    return title, details, str(totaltarget),  str(pro_id), start_time, end_time
    # else:
    #     print("invalid date, try again")
    #     return projectcntaint()

def createproject():
    print("--create project---")
    create = list(projectcntaint())

    create_new = ":".join(create)

    add = save_projects(create_new)
    if add:
        print("--ur created successfully---")

    else:
        print("there is an error, plz try again")
        return createproject()

def view():
    proj = get_data()
    if proj==False:
        print("no availble projects")
    else:
        print(proj)
#
# def delete_project():
#     view()
#     project_id=askfornum("plz enter id project")
#     print(project_id)





def search_project_by_id(project_id):
    allproject = save_projects(project_id)

    for project in allproject:
        myproject = project.strip("\n")
        myproject = myproject.split(":")

        if myproject[3] == project_id:
            project_index = allproject.index(project)

            print(f"Project is found at index {project_index}")
            return True, project_index

    else:
        print("Project is not found!!")
        return False

def delete_project_from_file(project_id):
    project_found = search_project_by_id(project_id)

    if project_found:
        project_index = project_found[1]

        allprojects = save_projects(project_id)
        del allprojects[project_index]


        deleted = write_project_list_to_file(allprojects)
        return deleted


def delete_project():
    view()
    project_id = askfornum("Please choose id of the book you want to delete: ")
    deleted = delete_project_from_file(project_id)

    if deleted:
        print("Project Deleted Successfully")