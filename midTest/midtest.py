# You have to 5:30pm to complete the following Test.
# Start now. 

# Item 1
# Write a class that Models a Human. 
# The class should depict the head, shoulders (left and right), legs (left and right), reproductive organs (fe/male)
# As a mininum, there should be 3 methods that return body parts, sets body parts and returns a message about the class. 
# Instantiate the class with the variable naming convention of lst_instantiation, 2nd and so forth - there should be 3 instantiations. 
class Human:
    def left_shoulder(self):
        print("left_shoulder")

    def right_shoulder(self):
        print("right_shoulder")




# Item 2
# Write a base class with a few properties for a class that will inherit from it. 
from abc import ABC , abstractmethod
class  Helicopter
    def fly(self):
    print("Fly Away")
    
class AirPlane
    def fly(self):
        print("Up up and away")

class soFLy(Helicopter , Airplane):
    pass
# Item 3 What is duck typing? 
#Not needing a type in order to invoke an existing method on an object



# Write 4 try and except statements on Syntax Error, Value Error, Type Error, Attribute Error
                 try:
                 age = int(input("What is your age? : "))
                 except ValueError:
                 print("You have to enter a number")
                 else: 
                 print("Thank you")


                 try:
                 age = int(input("What is your age : "))
                 except SyntaxError , ZeroDivisionError:
                 print("You cant enter any special characters")
                 print("You must be 18 or older")
                 else:
                 print("Thank you")

                 try:
                 pick1 = input("please choose G for go, or Q for quit").lower()
                 except TypeError:
                 print("Please choose G or Q")
                 else:
                 print("Thank you for your input")



# Write 5 functions depicting and returning *args and **kwargs 



                 def brandon(**user)
                 print(user)
                print(name=Malanie , place=Orlando)


# Write 2 functions that returns and integer to another function.

# Write 2 functions that have default arguments.

# Write 3 lambda functions. 
                 x = lambda a, b : a + b
                 print(x(5,6))

                 x = lambda c, d, e : c * d - e
                 print(x(5, 5, 7))

                x = lambda 

# Use the filter function to filter from a list that contains the integer 5 (should be excluded)

# What is a Stack? A container of objects that are inserted and popped according for first in first out (LIFO) the first item you take out

# What is a queue? A container of objects that are inserted and removed according to FIFO (First In First Out) the recently added is the first removed


# Write 3 list comprehensions. 
store_products = [
    ("Ceiba Macho" , 21),
    ("Makuto" , 321),
    ("Cleanse" , 121),
]

prices = [item[1] for item in store_products]
price2 = [item[2] for item in store_products]
price3 = [item[3] for item in store_products]







# Write 3 for-loops over a list. 
seasons = ["Winter" , "Summer", "Spring" , "Fall"]
for elements in seaons:
    print(seasons)

fish = ['bass' , 'shellcrackers' , 'bluegill' , 'mullet']
for species in enumerate(fish):
    print(species)

gatekeeps = ['Lucero Mundo' , 'Esu' , 'Papa Legba' , 'Elegua']
for communication in gatekeeps:
     print(communication + "The gatekeepers are the keepers and holders of Ase")



# Write 3 for-loops over a dictionary. 
bakulu_secrecy = {"Owner" : "Brandon" , "Location" : "Online" , "Tradition" : "Palo Mayombe"}
for k, v in bakulu_secrecy.items():
    print(k, v)

bakulu_secrecy = {"Owner" : "Brandon" , "Location" : "Online" , "Tradition" : "Palo Mayombe"}
for value in bakulu_secrecy.items():
    print("The value for this dictionary" + value)


bakulu_secrecy = {"Owner" : "Brandon" , "Location" : "Online" , "Tradition" : "Palo Mayombe"}
for key in bakulu_secrecy.items():
    print("They key for this dictionary is" + key)


# Write 3 for-loops over a Tuple.
 my_tup = ("Audi" , "Range Rover" , "McCLaren")
 for item in my_tup:
     print(item)

numbers = (1, 3, 7, 5)
sum = 0
for num in numbers:
    sum = sum + num
    print(num)
print("The sum is" + str(sum))

spirit_tups = ("Watariamba" , "Chola", "Nkuyo" , "Nsasi")
for item in enumerate(spirit_tups):
    print(item)



# Write a for-loop over a string. 

my_name = "Brandon Antoine Brown"
my_name2 = "Tata Vence Batalla"

for char in my_name:
    if my_name == my_name2:
        print("It is the same")
    else:
    print("It is not the same")
print(char)


# What is the difference between an Array and a List? 
# Arrays need to be declared because they are not apart of Pythons syntax and list do no have to be declared because they are apart of Python syntax

# Write 3 dictionary comprehensions. 
values = {a: a + 3 for a in range(5)}
print(values)



# Unpack 2 tuples. 
names = ("Brayden" , "Druyyd", "BJ", "Antoine")
child3, child4, child1, child2 = names
print(names)

movie_data = ("Friday" , "Ice Cube" , 1995)
name_of_movie, starring, year_released = movie_data
print(movie_data)

people = ("Whoppie Goldberg" , "Oprah Winfrey", "Jasmine Sullivan")
print(*people)

