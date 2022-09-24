

def save_projects(message):
    try:
        object = open("project_data.txt", "a")
    except:
        print("there is an error while creating project")
        return False
    else:
        object.write(f"{message}\n")
        return True

def get_data():
    try:
        object = open("project_data.txt",)
    except Exception as e:
        print("ERROR , plz try again")
        return False
    else:
        projects = object.readline()
        object.close()
        return projects


def save_user_data(message):
    try:
        object = open("userdata.txt", "a")
    except:
        print("there is an error while creating project")
        return False
    else:
        object.write(f"{message}\n")
        return True


def write_project_list_to_file(projectlist):
    try:
        projobj = open("project_data.txt", "w")
    except Exception as e:
        print("error happend wile opennig the file!!!")
        return False
    else:
        projobj.writelines(projectlist)
        projobj.close()
        return True

