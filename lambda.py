# Normal function:

# def x(a):
#     return a + 10

# print(x(5))

#---------------------------------------------

#lambda Function:
# x = lambda a : a + 10
# print(x(5))

#-----------------------------------------------

# a = int(input("Enter the number"))
# b = int(input("Enter the number"))

# x = lambda a, b : a * b
# print(x(a,b))

#-----------------------------------------------

# def myfunction(n):
#     return lambda x: x*n
# myDouble=myfunction(2)
# print(myDouble(2))
# print(myDouble(8))

#------------------------------------------------

# def myfunction(n):
#     return lambda x: x*n
# myDouble=myfunction(3)
# print(myDouble(9))
# print(myDouble(4))

# #------------------------------------------------------

# def myfunction(n):
#     return lambda x: x*n
# myDouble=myfunction(4)
# print(myDouble(7))
# print(myDouble(6))

#--------------------------------------------------

def myfunction(b):
    return lambda y: y*b
fifth=myfunction(5)
print(fifth(4))

#----------------------------------------

def myfunction(c):
    return lambda z: z * c
sixth=myfunction(6)
print(sixth(6))

#----------------------------------------