""" A dictionary is very similar to an object literal in JS
    - "A collection which is unordered ,  changeable , and indexed. No duplicate members 
"""

""" Create dictionary - MOST COMMON WAY """
person = {
    'first_name' : "John",
    'last_name' : "Doe",
    'age' : 30
}
# print(person , type(person)) ## prints {'first_name': 'John', 'last_name': 'Doe', 'age': 30} <class 'dict'>

""" Create dictionary using constructor """
# person2 = dict(first_name = "Sara" , last_name = "Williams")

""" Get Value """
# print(person['first_name']) ## MORE COMMON WAY
# print(person.get('last_name'))

""" Addd value """
# person['phone'] = '555-555-5555'
# print(person)

""" Get Dictionary keys """
# print(person.keys())

""" Get Dictionary Items """
# print(person.items())

""" Copy a dictionary """
# person2 = person.copy()
# person2['city'] = "Boston"
# print(person2)

""" Remove item from dictionary """
# del(person["age"])
# print(person)

""" Remove item with pop """
# person.pop("age")
# print(person)

""" Clear dictionary """
# person.clear()
# print(person)

""" Get length """
# print(len(person))

""" Similar to JS where you'll have an array of objects, WE CAN ALSO HAVE A LIST OF DICTIONARIES """
people = [
    {'name' : "Martha" , 'age' : 30},
    {'name' : "Peter" , 'age' : 21}
]
print(people) ## prints array of dictionaries
print(people[1]['name']) ## prints peter , the dictionary at place 1 and the value we want to print

