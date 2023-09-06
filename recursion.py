# def hello():
#     print("hello")
#     hello()


# hello()


# def number(num=0):
#     print(num)
#     number(num+1)


# number()


def number(num=0):
    print(num)

    if num == 10:
        return
    number(num+1)

number()

#task
#range(start, end)
