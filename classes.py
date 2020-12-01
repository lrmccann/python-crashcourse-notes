""" A class is like a blueprint for creating an object. An object has properties and methods (functions)
    associated with it. ALMOST EVERYTHING IN PYTHON IS AN OBJECT """

## Create a class ##
class User:
    ## Constructor ##
    def __init__(self , name , email , age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name}. I am {self.age} years old.'

    def has_birthday(self):
        self.age += 1


## EXTENDS CLASS ##
class Customer(User):
    ## Constructor ##
    def __init__(self , name , email , age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self , balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name}. I am {self.age} years old. My balance is {self.balance}'

## Initalize User Object ##
brad = User('Brad Traversy' , "Brad@gmail.com" , 37)

## Initalize Customer Object ##
janet = Customer('Janet Johnson' , "Janet@yahoo.com" , 25)

janet.set_balance(500)
print(janet.greeting())

## Access properties
# print(brad.name)

## add year to age via has_birthday function ##
brad.has_birthday()

## print greeting function ##
print(brad.greeting())