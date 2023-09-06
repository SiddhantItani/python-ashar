# #create a list user_list
# #collection of dictinory multiple user
# #username, password
# #user input username ra password
# #if the username and password exist or
# #user name ra password valid print you have been login
# #successfully else invalid credentials.

# # is_login=False
# # def login():
# #      global is_login
# #      user_list=[ 
# #           {'username':'admin', 'password':'admin'},
# #                {'username':'xyz', 'password':'xyz'},
# #                {'username':'abc', 'password':'abc'},
# #                {'username':'mno', 'password':'mno'},
# #      ]
# #      username=input("Enter the username: ")
# #      password=input("Enter the password: ")

     

# #      for user in user_list:
# #           if user["username"] == username and user["password"] == password:   
# #                is_login= True
# #                break
# # login()
# # if is_login:
# #     print("Successfully you have been login.")

# # else:
# #      print("Invalid credentials.")



# # user_list=[ 
# #      {'username':'admin', 'password':'admin'},
# #           {'username':'xyz', 'password':'xyz'},
# #           {'username':'abc', 'password':'abc'},
# #           {'username':'mno', 'password':'mno'},
# #  ]
# # username=input("Enter the username: ")
# # password=input("Enter the password: ")

# # for user in user_list:
# #      if user["username"] == username and user["password"] == password:   
# #           print("You have been login successfully.")
# #           break
# #      else:
# #           print("Invalid credentials.")


     



# # def register(my_list,username, password):
# #         if username in my_list:
# #              return False
# #         else:
# #              my_list[username]= password
# #              return True
        
        

# # def login(my_list,username, password):
# #         if username in my_list and my_list[username]== password:
# #               return True
# #         else:
# #               return False


# # user_list={}
     
# # while True:
# #           print("1. Register")
# #           print("2. Login")
# #           print("3. Exit")
# #           choice = input("Select an option: ")

# #           if choice == "1":
# #                username = input("Enter your username: ")
# #                password = input("Enter your password: ")
# #                if register(user_list, username, password):
# #                     print("Registration successful.")
# #                else:
# #                     print("Username already exists.")

# #           elif choice == "2":
# #                username = input("Enter your username: ")
# #                password = input("Enter your password: ")
# #                if login(user_list,username, password):
# #                     print("Login successful.")
# #                     print(user_list)
# #                else:
# #                     print("Login failed. Invalid username or password.")

# #           elif choice == "3":
# #                break

# #           else:
# #                print("Invalid choice. Please select again.")



# # user_list=[]

# # username=input("enter the username: ")
# # password=input("Enter the password: ")

# # user={
# #     'username':username,
# #     'password':password,
# # }

# # def register(username,password):
# #     user={
# #     'username':username,
# #     'password':password,
# #      }
# #     user_list.append(user)

# # def display_userL():
# #     for user in user_list:
# #         print(f"{username}|{password}")

# # username=input("enter the username: ")
# # password=input("Enter the password: ")
# #  while=True
   



# # #Addition
# # #Subtraction
# # #Multiplication
# # #Division

# # print("The simple calculator which holds the features of addition, subraction, multiplicationa and division:")
# # print("1:Addition")
# # print("2:Subtraction")
# # print("3:Multiplication")
# # print("4:Division")

# # operation = input()
# # if operation == "1":
# #     num1=input("enter the first number: ")
# #     num2=input("enter the second number: ")
# #     print("The sum of two number is " + str(int(num1) + int(num2)))
# # elif operation == "2":
# #     num1 = input("enter the first number: ")
# #     num2 = input("enter the second number: ")
# #     print("The differnce of two number is " + str(int(num1) - int(num2)))
# # elif operation == "3":
# #     num1 = input("enter the first number: ")
# #     num2 = input("enter the second number: ")
# #     print("The product of two number is " + str(int(num1) * int(num2)))
# # elif operation == "4":
# #     num1 = input("enter the first number: ")
# #     num2 = input("enter the second number: ")
# #     print("The quotient of two number is " + str(int(num1) / int(num2)))
# # else:
# #     print("it is invalid entry a calculator cannot calcualte")

# #Calculator
# #Addition
# #Subtraction
# #Multiplication
# #Division

# print("The simple calculator which holds the features of addition, subtraction, multiplication and division:")
# print("1:Addition")
# print("2:Subtraction")
# print("3:Multiplication")
# print("4:Division")

# operation = input()
# if operation == "1":
#     num1=input("enter the first number: ")
#     num2=input("enter the second number: ")
#     print("The sum of two number is " + str(int(num1) + int(num2)))
# elif operation == "2":
#     num1 = input("enter the first number: ")
#     num2 = input("enter the second number: ")
#     print("The differnce of two number is " + str(int(num1) - int(num2)))
# elif operation == "3":
#     num1 = input("enter the first number: ")
#     num2 = input("enter the second number: ")
#     print("The product of two number is " + str(int(num1) * int(num2)))
# elif operation == "4":
#     num1 = input("enter the first number: ")
#     num2 = input("enter the second number: ")
#     print("The quotient of two number is " + str(int(num1) / int(num2)))
# else:
#     print("it is invalid entry a calculator cannot calcualte")


#simple contact book
class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone Number: {contact.phone_number}")
            
            print("-" * 20)

    def search_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)
        return found_contacts


contact_book = ContactBook()

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        
        contact = Contact(name, phone_number, )
        contact_book.add_contact(contact)
        print("Contact added successfully!")
        print("-"* 20)

    elif choice == "2":
        contact_book.view_contacts()

    elif choice == "3":
        search_name = input("Enter the name: ")
        search_results = contact_book.search_contact(search_name)
        if search_results:
            print("Search Results:")
            for result in search_results:
                print(f"Name: {result.name}")
                print(f"Phone Number: {result.phone_number}")
                
                print("-" * 20)
        else:
            print("No matching contacts found.")
            

    elif choice == "4":
        print("Exiting Contact Book.")
        print("-"* 20)
        break

    else:
        print("Invalid choice. Please choose a valid option.")
        print("-"* 20)
