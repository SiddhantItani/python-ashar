""" create a variable 
name(string)
contact(interger)
address(string)
age(float) """


""" name = "Siddhant Itani"
contact = 9808110679
address = "chabehil"
age = 23.11
print(type(name))
print(type(contact))
print(type(address))
print(type(age))

print(f"my name is {name}. my contack number is {contact}. my address is {address}. and my age is {age}\n"*10)
print(name[::-1]) """


""" a = int(input("Enter the number"))
b = int(input("Enter the number"))
sum = a + b
print(f"Sum of a and b is {sum}")
diff = a - b
print(f"diff of a and b is {diff}")
multy = a * b
print(f"multy of a and b is {multy}")
Divide = a / b
print(f"Divide of a and b is {Divide}")
 """

""" a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = a + b
print(f"c = {c}") """


""" name = "Siddhant Itani"
contact = 9808110679
address = "chabehil"
age = 23.11


c=(f"my name is {name}. my contact number is {contact}. my address is {address}. and my age is {age}")

print(c[::-1])
c.length()
 """




# def sum(a,b):
#     print(a+b)

# def subtract(a,b):
#     print(a-b)

# def divide(a,b):
#     print(a/b)

# def multiply(a,b):
#     print(a*b)

# while True:
#     operation = input("Enter the operation +,-,/,*: ")
#     a = int(input("Enter the postive number"))
#     b = int(input("Enter the postive number"))

#     if operation == "+":
#         sum(a,b)
#     elif operation == "-":
#         subtract(a,b)
#     elif operation == "/":
#         divide(a,b)
#     elif operation == "*":
#         multiply(a,b)

#     else:
#         print("unknown operation")


import random

def main():
    print("Welcome to the Guess the Number game!")
    target_number = random.randint(1, 10)
    attempts = 0
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts.")
            break


main()

    