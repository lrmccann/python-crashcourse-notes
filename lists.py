""" Lists in Python , VERY SIMILAR TO AN ARRAY IN JS
    - The definition of a list in Python is :
        "a collection which is ordered and changeable. Allows duplicate members."
 """

""" Create List - THIS IS THE MORE COMMON WAY """
# numbers = [1 , 2 , 3 , 4 , 5]
fruits = ["Apples" , "Oranges" , "Grapes" , "Pears"]

""" Use a Constructor """
# numbers2 = list((1 , 2 , 3 , 4 , 5))

# print(numbers , numbers2)

""" Get a Value """
# print(fruits[1])

""" Get length """
# print(len(fruits))

""" Append to list """
# fruits.append("Mangos")
# print(fruits)

""" Remove item from list """
# fruits.remove("Grapes")
# print(fruits)

""" Insert into position """
# fruits.insert(2 , "Strawberries")
# print(fruits)

""" Remove with pop """
# fruits.pop(1)
# print(fruits)

""" Reverse list """
# fruits.reverse()
# print(fruits)

""" Sort list """
# fruits.sort()
# print(fruits)

""" Reverse sort """
# fruits.sort(reverse = True)
# print(fruits)

""" Change Value """
# fruits[0] = "Blueberries"
# print(fruits)