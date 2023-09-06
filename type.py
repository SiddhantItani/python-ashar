# def person(name, course):
#     print(name, course)

# person("sid" , "python")
# person(course="python", name="sid")

#task
#persons function args
#argument name parameter define
#print('my name is parameter value')

# def person(*name): #args
#     print(name[0],name[1],name[2])

# person('sid','ram','shyam')


#kwargs
#person()
#name= first name, last name
#age
#description about hobby
#course

#hello my name is <name> and my last name is <last_name>
#my age is <Age>
#<hobby)
#<i am studing <course>

# def person(name, course):
#     print(f'{name} studies {course}')

# person("ram", "django")

def person(**kwargs):
    # print(type(kwarge))
    print(f"{kwargs['name']} studies {kwargs['course']}")

person(name="ram",course= "django", institue= "mindrisers")