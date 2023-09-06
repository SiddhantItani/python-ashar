class person():
    def __init__(self,name,age,password) -> None:
        self.name= name
        self._age= age # protected variable
        self.__password= password # private variable

    def get_password(self):
        return self.__password
    
    def set_password(self,password):
        self.__password=password

Person=person("ram",18,1234)
print(Person.name)
print(Person._age)
# Person.set_password(3456)
print(Person.get_password())