""" A for loop is used to iterate over a sequence, either : 
    (a list, a tuple, a dictionary, a set, or a string) """

people = ["Mark" , "Robbie" , "John" , "Will", "Sam"]

#### Simple for loop iterating through a list ####

# for person in people:
    # print(f'Current Person: {person}')


#### Break out of a loop -- This stops the loop at the person ####
# for person in people:
#     if person == 'John':
#         break
#     print(f'Current Person: {person}')

#### Continue in loop -- This does not stop the loop, just skips over the person ####
# for person in people:
#     if person == 'Will':
#         continue
#     print(f'Current Person : {person} ')

#### Range ####
# for i in range(len(people)):
#     print(people[i])

#### Custom Range ####
# for i in range(2 , 12):
#     print(f'Numbers : {i}')

""" While loops execute a set of statements as long as a conditional is true """

# count = 0
# while count <= 10:
#     print(f'Count : {count}')
#     count += 1