
""" Variable Rules:
   - Variables are case sensitive ( name is different than NAME)
   - Must start with a letter or underscore
   - Can have numbers but cannot start with numbers """

""" Data Types:
    -int is a number value
    -float or float point is a number that contains a .
    -string is a value surrounded by single or double quotes
    -boolean is True or False """

# x = 1 #int
# y = 2.5 #float or float point
# name = "John" #str (string)
# is_cool = True #boolean

""" Multiple line assignment """
# x , y , name , is_cool = (1 , 2.5 , "John" , True)

""" Python equiv to console.log() """
# print(x) ## prints the int/num 1
# print(x , y , name , is_cool) ## prints the int/num 1, float 2.5 , string "John" , and bool True

""" Basic Math """
# a = x + y
# print(a) ## prints float val of 3.5

""" Check type of """
# print(type(x)) ## prints <class 'int'>

""" Casting - purposely converting the data type of a varible (similar to type coersion in JS) """
# x = str(x) ## converts x from <class 'int'> to <class 'str'>
# print(type(x))

# y = int(y) ## converts y from <class 'float'> to <class 'int'>
# print(type(y))

""" Create new var z
    - If we uncomment the conversion values in "Casting" and print z it will be <class 'float' BUT a value of 2.0,
    this is because we convert y from a float to an int, which is a whole # value, then print the value of z AFTER
    y has already been converted, so the number is set at 2.0 and will not convert back to 2.5 """
# z = float(y) ## z is now the value of <class 'float'> with a value of 2.5
# print(type(z) , z)