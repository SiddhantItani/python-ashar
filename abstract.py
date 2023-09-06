from abc import ABC,abstractmethod

class computer(ABC):

    @abstractmethod
    def process(self):
        pass
    def run(self,name):
        self.process(name)


class laptop(computer):
    def process(self,name):
        print(f"{name} is running on laptop")


class mobile(computer):
    def process(self,name):
        print(f"{name} is running on mobile")

Laptop=laptop()
Laptop.run("chrome")
Laptop.run("pubg")
Laptop.run("music player")
Laptop.run("vs code")

Mobile=mobile()
Mobile.run("pubg")


