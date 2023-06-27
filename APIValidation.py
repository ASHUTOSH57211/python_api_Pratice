import requests
import json
from configurations import *
from payload import *
#perform basic http request like GET POST UPDATE AND DELETE operation using library api

#

#ADD BOOK to LIBRARY - post operation
addBook_response = requests.post(get_config()['API']['endpoint']+get_config()['API']['AddBookpoint'],json=addBook("bcdzcqwcc"))
print(addBook_response.status_code)
print(addBook_response.json())
responseBookId = addBook_response.json()['ID']
print(responseBookId)
print("##########################BOOK ADDED SUCCESSFULLLY##########################")

#GETBook by Author name

getBook_response = requests.get(get_config()['API']['endpoint']+get_config()['API']['GetBookpoint'],params={'ID':responseBookId})
print(getBook_response.status_code)
print(getBook_response.json())

print("##########################BOOK FETCHED SUCCESSFULLLY##########################")


#Delete Book by ID

deleteBook_response = requests.post(get_config()['API']['endpoint']+get_config()['API']['DeleteBookpoint'],json=deleteBook(responseBookId))
print(deleteBook_response.json())

print("##########################BOOK deletedS SUCCESSFULLLY##########################")


