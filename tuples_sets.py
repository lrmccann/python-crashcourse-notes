""" A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    - Similar to a list but it is unchangeable """

""" Create a tuple - MOST COMMON WAY """
# fruits = ("Kiwi" , "Banana" , "Passion Fruit" , "Mango")

""" Use a constructor """
# fruits2 = tuple(("Kiwi" , "Banana" , "Passion Fruit" , "Mango"))
# print(fruits , fruits2)

""" Single value tuple needs a trailing comma or it is considered a string """
# fruits3 = ("Apples" , )
# print(fruits3 , type(fruits3))

""" Get Value """
# print(fruits[1])

""" CANNOT CHANGE A VALUE IN A TUPLE """
# fruits[0] = "Pears"
# print(fruits) ## Prints 'tuple' object does not support item assignment

""" Delete a tuple """
# del fruits2
# print(fruits2) ## Prints fruits2 is not defined

""" Length of """
# print(len(fruits))

""" A set is a collection which is unordered and unindexed. No duplicate members. """

""" Create a set """
fruits_set = {"Apples" , "Oranges" , "Mango"}

""" Check if in set """
# print("Apples" in fruits_set) ## Prints True

""" Add to set """
# fruits_set.add("Grapes")
# print(fruits_set)

""" Add duplicate - WHICH WILL NOT WORK - DOESNT THROW ERROR BUT WILL NOT ADD TWICE """
# fruits_set.add("Apples")
# print(fruits_set)

""" Remove from set """
# fruits_set.remove("Apples")
# print(fruits_set)

""" Clear set entirely - STILL HAVE FRUIT_SET BUT IT'S EMPTY """
# fruits_set.clear()
# print(fruits_set)

""" Delete set - COMPLETELY DELETES SET """
# del fruits_set
# print(fruits_set)

