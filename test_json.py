""" JSON is commonly used with data APIS. Heres how we parse JSON in a python Dictionary """

import json

## Sample JSON ##
userJson = '{"first_name" : "Logan" , "last_name" : "McCann" , "age" : 23}'

## Parse to Dictionary ##
user = json.loads(userJson)

## Print whole user ##
print(user)

## Print property from user ##
print(user['first_name'])


## TAKE OBJECT AND CONVERT TO JSON ##
car = {"make" : "Ford" , "model" : "model" , "year" : 1970}

carJSON = json.dumps(car)

print(carJSON)