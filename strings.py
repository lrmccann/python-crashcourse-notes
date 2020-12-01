""" Strings in Python are surrounded by either single or double quotes ('' or "") """

# name = 'Logan'
# age = 23

""" Concatenate - To insert a variable into a string
    - the variable name can be printed using concat, however age is an int and will not be printed
        there are a few methods we go over in "String Formatting" to help us with this problem """

""" String Formatting """
# Method 1 Set new var that Casts age to str
# new_age = str(age)
# print("Hello my name is " + name + ". I am " + new_age + " years old.")

# Method 2 Casting the var
# print("Hello my name is " + name + ". I am " + str(age) + " years old.")

# Method 3 Arguments by position (content in {} are just place holders to be defined at the end of the string)
# print("Hello my name is {name}. I am {age} years old.".format(name = name , age = age))

# Method 4 and probably the best/easiest method (available Python 3.6 +) THE F-STRING
# This method is very similar to JS but it doesnt require the `` (back ticks) or the $ , just the f in the beg of string
# print(f"Hello my name is {name}. I am {age} years old.")


""" String Methods
    - Methods work the same as JS, we add a . and then the method after the var """

# s = "hello World"

""" Capitalize """
# print(s.capitalize())

""" Upper """
# print(s.upper())

""" Lower """
# print(s.lower())

""" Swap Case """
# print(s.swapcase())

""" Length """
# print(len(s))

""" Replace """
# print(s.replace("world" , "everyone"))

""" Count """
# sub = "h"
# print(s.count(sub))

""" Starts With """
# print(s.startswith("hello"))

""" Ends with """
# print(s.endswith("d"))

""" Split into a list """
# print(s.split())

""" Find position """
# print(s.find("r"))

""" Is alphanumeric """
# print(s.isalnum())

""" Is alphabetic """
# print(s.isalpha())

""" Is numeric """
# print(s.isnumeric())