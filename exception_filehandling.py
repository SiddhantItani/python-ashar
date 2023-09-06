
while True:
    try:
        a=int(input("Enter the number: "))
        b=int(input("Enter the number: "))

        print(a/b)
    except ZeroDivisionError:
        print("number can't be divisible by zero")
    except ValueError:
        print("Invalid input. insert only integer value.")
    except:
        print("something went wrong")