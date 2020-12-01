""" If/Else statements are used to decide to do something based on something being True or False
    VERY SIMILAR TO JS CONDITIONALS """

#### variables for Comparision Operators, Nested if , and Logical Operators
# y = 5
# x = 10

""" Comparison Operators (== , != , > , >= , < , <=) - Used to compare values """

""" Simple if """
# if x > y:
    # print(f'{x} is greater than {y}')

""" If / Else """
# if x > y:
    # print(f'{x} is greater than {y}')
# else:
    # print(f'{y} is greater than {x}')

""" If / Elif / Else """
# if x > y:
    # print(f'{x} is greater than {y}')
# elif x == y:
    # print(f'{x} is equal to {y}')
# else:
    # print(f'{y} is greater than {x}')

""" Nested if - THIS IS BETTER DONE WITH A LOGICAL OPERATOR """
# if x > 2:
    # if x <= 10:
        # print(f'{x} is greater than 2 and less than or equal to 10')


""" Logical Operators (and , or , not) - Used to combine conditional statements """

##### And Operator #####
# if x > 2 and x <= 10:
    # print(f'{x} is greater than 2 and less than or equal to 10')

#### Or Operator ####
# if x > 4 or x <= 10:
    # print(f'{x} is greater than 4 and less than or equal to 10 ')

#### Not Operator ####
# if not(x == y):
    # print(f'{x} is not equal to {y}')

""" Membership Operators (not , not in ) - Used to test if a sequence is presented in an object/dictionary or list """

#### variables for MemberShip Operators and Identity Operators
x = 3
y = 20

numbers = [1 , 2 , 3 , 4 , 5]

#### In Operator ####
if x in numbers:
    print(x in numbers) ## THIS PRINTS A BOOLEAN DEPENDING ON ANSWER

#### Not In Operator ####
if y not in numbers:
    print(x not in numbers)


""" Identity Operators (is , is not) - Used to compare objects/dictionaries or lists, NOT IF THEY ARE EQUAL, BUT IF 
    THEY ARE ACTUALLY THE SAME OBJECT, WITH THE SAME MEMORY LOCATION : """

#### Is Operator ####
if x is y:
    print(x is y) ## THIS PRINTS A BOOLEAN DEPENDING ON ANSWER

if type(y) is type(int()):
    print(f'{y} is an int')


#### Is Not Operator ####
if x is not y:
    print(x is not y)

if x is not int(20):
    print(f'{x} is not 20')