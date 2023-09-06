# def star(func):
#     def wrapper():
#         print('*'* 20)
#         func()
#         print('*'*20)
#     return wrapper

# @star
# def name():
#     print("hello")
# @star
# def age():
#     print("age")

# star(name)()
# name()
# age()


#task
###############
#***************
#name
#************
##############

def hash(func):
    def wrapper():
        print("#"*10)
        
        func()
        
        print("#"*10)
    return wrapper

def star(funt):
    def wrapper():
        print("*"*10)
        funt()
        print("*"*10)
    return wrapper



# @hash
# @star
def name():
    print("Name")

# @star
def age():
    print("Age")

# name()
# print("-"*30)
# age()

# star(omen(name()))
hash(star(name))()