""" A module is basically a file containing a set of functions to include in your application.
    There are core python modules, modules you can install using the pip manager
    (including Django) as well as custom modules """
""" A LOT OF MODULES COME WITH PYTHON (core modules) , PIP IS USED TO DOWNLOAD MORE MODULES (pip modules) """

#### import CORE python module -- no installation ####
#### DATETIME MODULE ####

import datetime ## This is an import of the whole module ##
from datetime import date ## This is an import of a single object from the "datetime module" ##
today = date.today() ## since we imported "date" from "datetime" we just have to use date.today() ##
# today = datetime.date.today() ## "date" is an object of "datetime" ##
print(today) ## prints 2020-11-27 or whatver the current date is ##

#### TIME MODULE ####
import time ## Import time module ##
from time import time ## imports single "time" object from "time"
timestamp = time()
# timestamp = time.time() ## Gets current timestamp ##
print(timestamp) ## prints timestamp ##


""" LIKE NODEJS FOR JS, PYTHON HAS A PACKAGE MANAGER KNOWN AS PIP, ALLOWING US TO DOWNLOAD MORE  """
#### normally to use pip we just type pip BUT ####
#### SINCE PYTHON 3 IS AVAILABLE IN PYTHON 3 COMMAND , WE USE "pip3" ####
#### TO SEE ALREADY INSTALLED MODULES, WE USE "pip3 freeze"

#### WE INSTALLED CAMELCASE USING PIP ####
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello there world'))

#### Import Custom Module from validator.py ####
import validator
## or ##
from validator import validate_email

email = "test@test.com"
if validate_email(email):
    print("email is valid")
else:
    print("email is bad")
