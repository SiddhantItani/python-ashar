# fruits=['apple','banana','orange','mango']
# for fruit in fruits:
#     print(fruit)

#vegtable list
#print each of them using loop

#vegetables=['carrot','potato','raddish','cabbage','basil','pumpkin']
# for vegetable in vegetables:
#     print(f"vegetable name is {vegetable}") # f-string = formet string

# vegetables=['carrot','potato','cabbage','basil','pumpkin']
# # for vegetable in vegetables:
# #     print(vegetable) 

# i = 0
# while vegetables[i]:
#     print(vegetables[i])
#     i+=1


# fruit="banana"
# for char in fruit:
#     print(char)

# vegetables=['carrot','potato','cabbage','basil','pumpkin']
# a = input("enter the vegetables name:  ")
# for veg in vegetables:
    
#     if veg == "a":
#         print('found')
#         break


# print(list(range(1,11)))

# for i in range(1,11):
#     print(i)
    
# for i in range(1,11,2):
#     print(i)

# user list
# 10 user email
# user input email
# print(found)


""" user_list=[
    'abc@gmail.com','bcd@gmail.com','cde@gmail.com','def@gamil.com','efg@gmail.com','fgh@gmail.com','ghi@gmail.com','hij@gmail.com',
    'ijk@gmail.com','jkl@gmail.com'
]
email =input("Enter your email: ")
for emails in user_list:
    
    if emails == email:
        print('found')
        break
 """

# email_list=['a@xyz.com','b@xyz.com','c@xyz.com','d@xyz.com','e@xyz.com','f@xyz.com','g@xyz.com','h@xyz.com','i@xyz.com','j@xyz.com']

# email_user=input('Enter the Email Address:')
# for email in email_list:
#             if email==email_user:
#                     print('found')
#                     break
#             else:
#                     print('not found')
       
user_list=['abc@gmail.com','bcd@gmail.com','cde@gmail.com','def@gamil.com','efg@gmail.com','fgh@gmail.com','ghi@gmail.com','hij@gmail.com',
    'ijk@gmail.com','jkl@gmail.com']
email=input('Enter your email: ')

for e in user_list:
    if e==email:
        print("Found")
        break
else:
    print("Not Found")