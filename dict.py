"""
Dictionary -> Key : Value
each element in a dictionary has key and its value
for instance
students = {"name" : "Bekdaulet", "age" : 25, and etc}

in this case name and age are keys and Bekdaulet and 25 are values

and if i wanna to add new item in our dictionary
i just write

name of var["New Item] = "our value"
for example

i have dict houses

houses = {"Harry":"Gryffindor", "Draco": "Slytherin"}
and i just write
houses["Bekdaulet"] = "Gryffindor"


"""

houses = {"Harry":"Gryffindor", "Draco": "Slytherin","Yernazar": "Aitushny"}
houses["Hermione"] = "Gryffindor"
houses["Dimash"] = "Aitushny"

print(houses["Harry"])
print(houses["Draco"])
print(houses["Hermione"])
print(houses["Dimash"])