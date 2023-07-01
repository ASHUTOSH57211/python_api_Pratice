import requests
import json
from configurations import *
from payload import *

def after_scenario(context,scenario):
    deleteBook_response = requests.post(get_config()['API']['endpoint']+get_config()['API']['DeleteBookpoint'],json=deleteBook(context.responseBookId))
    print(deleteBook_response.json())
