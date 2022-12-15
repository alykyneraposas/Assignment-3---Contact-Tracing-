contact_details = {}

print("Menu")
print("_________________")
print("1. ADD CONTACTS")
print("_________________")
print("2. SEARCH")
print("_________________")
print("3. EDIT CONTACT")
print("_________________")
print("4. EXIT")
print("_________________")

user_select = int(input("What do you want to do? (1-4)"))

while True:
    if user_select == 1:
        Name = input("Enter Full name:")
        Age = input("Enter Age:")
        Phone = input("Enter Phone number:")
        Address = input("Enter Adress: ")
        contact_details[Name] = Name
        contact_details[Name] = Age
        contact_details[Name] = Phone
        contact_details[Name] = Address
        print("Contact information save!")
        user_select = int(input("What do you want to do? (1-4)"))
    if  user_select == 2:
        search_name = input("Enter the contact name:")
        print()
    
        if search_name in contact_details:
            print( "Name:", Name)
            print ("Age:", Age)
            print ("Phone number:", Phone)
            print ("Adress:", Address)
            user_select = int(input("What do you want to do? (1-4)"))
        else:
            print("Name doesn't exist") 
            print("If contact details is edited try to input the old names.")
            user_pick = int(input("What do you want to do? (1-3)"))
    if user_select == 3:
        edit = input("Enter the contact to be edited:")
        if edit in contact_details:
            Name = input("Enter Full Name:")
            contact_details[edit] = Name
            Age = input("Enter Age:")
            contact_details[edit] = Age
            Phone = input("Enter Phone number:")
            contact_details[edit] = Phone
            Address = input("Enter Address:")
            contact_details[edit] = Address
            print("Contact updated!!")
            user_select = int(input("What do you want to do? (1-4)"))
        else:
            print("Name doesn't exist")  
            user_select = int(input("What do you want to do? (1-4)"))
    if user_select == 4:
        exit = input ("Exit (Yes or No)")
        if exit == "Yes":
            break
        elif exit == "No":
         user_select = int(input("What do you want to do? (1-4)"))
