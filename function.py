# def hello_world():
#     print("hello World!") # this void type function


# hello_world()

# void type

# def sum():
#     print(1+2)

# sum()

# Return type:

# def sum():
#     return 3 + 4 

# addition = sum()
# print(addition)

# def sum(a,b):
#     return f"The sum of two number {a} + {b} is {a+b}"

# addition = sum(2,4)
# print(addition)



#task create a calculator
#user input /,+,*,-
#add
#divide
#multiply
#subtract
#user input /,+,*,-
#user input positive integer / float number
#if user select add print only
#loop ,multiple time
#using function

# def divide(a,b):
#     print(a/b)
# divide(1,2)
# divide(b=2,a=1)


class Calculator:
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
        
    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b


cal = Calculator()

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")
    
    ch = int(input("Select operation: "))
    
    
    if ch in (1, 2, 3, 4, 5):
        
        
        if(ch == 5):
            break
        
              
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        if(ch == 1):
            print(a, "+", b, "=", cal.add(a, b))
        elif(ch == 2):
            print(a, "-", b, "=", cal.subtract(a, b))
        elif(ch == 3):
            print(a, "*", b, "=", cal.multiply(a, b))
        elif(ch == 4):
            print(a, "/", b, "=", cal.divide(a, b))
    
    else:
        print("Invalid Input")