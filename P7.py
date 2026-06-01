system={}

while True:
    print("STUDENT RECORD DATABASE SERVER")
    print("Press 1 to Add New Student")
    print("Press 2 to View A Students")
    print("Press 3 to Delete Student Info")
    print("Press 4 to exit")

    button=int(input("Press either 1,2,3,4: "))

    if button==1:
        Name=input("Enter Name:  ")
        Roll=int(input("Enter Roll NO: "))
        Gender=input("Enter Gender(Male/Female): ")
        Age=int(input("Enter Age: "))
        system[Roll]={"Name": Name, "Gender": Gender, "Age": Age}
        print(f"{Name} was added into the database.")

    elif button==2:
        Roll=int(input("Enter Roll NO: "))
        if Roll in system:
            print(f"NAME: {system[Roll]['Name']}")
            print(f"Roll NO: {Roll}")
            print(f"Gender: {system[Roll]['Gender']}")
            print(f"Age: {system[Roll]['Age']}")
        else:
            print("NO STUDENT FOUND")

    elif button==3:
        Roll=int(input("Enter Roll NO: "))
        if Roll in system:
            del system[Roll]
            print("DATABASE UPDATED.")
        else:
            print("NO STUDENT FOUND.")

    elif button==4:
        Sure=int(input("Do you really want to exit? 0-NO,1-YES: "))
        if Sure==0:
            print("Back to Menu")
        elif Sure==1:
            print("EXIT")