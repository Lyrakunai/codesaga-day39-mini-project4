contacts_list = [
    {
        "name": "priya",
        "number": 24390818334
    },
    {
        "name": "anamika",
        "number": 42345594848
    },
    {
        "name": "sonam",
        "number": 29320947983
    }
]

print("This is contact list!")
print("here you can search contact/ view all contacts/ add new contact/ show total contacts/ delete contact!")
print("want to leave type (exit)!")
user = input("type as you want: ")
while  user != "exit": 
    if user != "delete contact" and user != "view all contacts" and user != "show total contacts" and user != "search contact" and user != "add new contact":
            print("invalid input")
            print("chosse valid optiton")

    if user == "view all contacts":
        if contacts_list == []:
            print("empty contact list")
        for k in contacts_list:
            print(k)
    

    if user == "show total contacts":
        s = len(contacts_list)
        print("total contacts -> ",s)

 
    if user == "add new contact": 
        name = input("enter name:")
        number = int(input("enter number:"))
        for k in contacts_list:
            if number == k["number"]:
                print("this contact already exit!")
                break
        else:
            new_contact = {
            "name": name,
            "number": number
                }
            contacts_list.append(new_contact)
            print("added successfully")
            s = input("if you want to see final look (type see): ")
            if s == "see":
                print(new_contact)
            else: 
                print("Thanks for adding new contact!")

    if user == "search contact":
        found = False
        search = input("enter contact name:")
        for s in contacts_list:
            if s["name"] == search:
                found = True
                print(s)
        else:
            if not found:
                print("not found!",search)

    if user == "delete contact":
        found = False
        a = input("enter contact name:")
        for j in contacts_list:
            if j["name"] == a:
                contacts_list.remove(j)
                print(contacts_list)
                print("delete successfully")
                found = True
        else:
            if not found:
                print(a,"is not in this contacts")

    print("-----------------------------------------------------------------------------------------------------")
    print("Try next....,🤗🤗🤗🤗🤗")
    print("here you can search contact/ view all contacts/ add new contact/ show total contacts/ delete contact!")
    print("want to leave type (exit)!")
    user = input("type as you want: ")