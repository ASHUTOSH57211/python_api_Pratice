from behave import *
import requests
from configurations import *
from payload import *


#to run a feature file in behave the follwing commands - behave feature/bookAPI.feature --no-capture

@given('Book details needed for the Library') 
def step_impl(context):
    context.url = get_config()['API']['endpoint']+get_config()['API']['AddBookpoint']
    context.PayLoad = addBook("bcdzcqwccpqo","4321")
    

@when('we execute the add Book POST API method')
def step_impl(context):
    context.addBook_response = requests.post(context.url,json=context.PayLoad)

    

@then('Book added successfully')
def step_impl(context):
    print(context.addBook_response.json())
    context.responseBookId = context.addBook_response.json()['ID']
    print(context.responseBookId)

@given('Book details needed for the Librar ywith parameters like {isbn} and {aisle}') 
def step_impl(context,isbn,aisle):
    context.url = get_config()['API']['endpoint']+get_config()['API']['AddBookpoint']
    context.PayLoad = addBook(isbn,aisle)
    