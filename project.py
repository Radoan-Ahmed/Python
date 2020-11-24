import json
def read_info_from_file():

    try:
        file = open("contacts.json","r")
        file_info_as_text = file.read()
        info = json.loads(file_info_as_text)
        file.close()

        return info
    except:
        return []

def write_info_to_file(info):
    file = open("contacts.json","w+")
    json_text = json.dumps(info,indent = 4)
    file.writelines(json_text)
    file.close()

def add_info(fulName,id,course,status):
    info_array = read_info_from_file()
    newContact = dict()
    newContact['fulName'] = fulName
    newContact['id'] = id
    newContact['course'] = course
    newContact['status'] = status
    info_array.append(newContact)
    write_info_to_file(info_array)

def search_info(query):
    info_array = read_info_from_file()
    for info in info_array:
        if info.get("fulName") == query or info.get("id") == query:
            return info.get("status")
    return None

def view():
    file = open("contacts.json", "r")
    file_info_as_text = file.read()
    info = json.loads(file_info_as_text)
    lenth = len(info)
    for data in info:
        name = data['fulName']
        id = data['id']
        course = data['course']
        status = data['status']

        print("Student Name:", name)
        print("Student Id:",id)
        print("Courses:",course)
        print("Status:",status)
        print("....................")
        print("....................")
    print(lenth)



def delete(delvalue):
    info_array = read_info_from_file()
    arry = []
    for info in info_array:
        if info.get('fulName')==delvalue:
            pass
        else:
            arry.append(info)
    write_info_to_file(arry)



while True:
    print("1.Add Contact")
    print("2.Search Contact")
    print("4.view data")
    print("5.Delete data")
    print("3.For exit")
    choice = int(input())

    if choice == 1:
        fname = str(input("Enter Student Name:"))
        id = str(input("Enter Student Id:"))
        course = str(input("Enter Course:"))
        status = str(input("Enter Status:"))
        add_info(fname,id,course,status)
        print("Information Added\n")

    elif choice == 2:
        query = str(input())
        number = search_info(query)
        print("Status of {} is : {}\n".format(query,number) if number is not None else "Contact Not Found\n")

    elif choice == 4:
        view()

    elif choice == 3:
        exit()

    elif choice == 5:
        value = str(input("Enter Student Name to delete his\her information:"))
        delete(value)


