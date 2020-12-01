""" Python has functions for creating , reading , updating , and deleting files """

## Open a file ##
## this also creates the file and the "w" gives write access ##
myFile = open('myfile.txt' , 'w')

## Get some info on file ##
print('Name : ' , myFile.name)
print('IsClosed : ' , myFile.closed)
print('Opening Mode : ' , myFile.mode)

## Write to file ##
myFile.write('I love python')
myFile.write(' and javascript')
## After writing to a file, MAKE SURE TO CLOSE IT ##
myFile.close()

## Append to file after closure -- the "a" is for append ##
myFile = open('myfile.txt' , 'a')
myFile.write(' my fav framework is React')
myFile.close()

## Read from file -- "r+" is to read ##
myFile = open('myfile.txt' , 'r+')
text = myFile.read(100) ## sets the character limit for the read
print(text)