import requests

############GET A BOOK ###################

# response = requests.get("http://216.10.245.166/Library/GetBook.php",
#                         params={"AuthorName":"Rahul Shetty"})


# print(response.text)
#print(type(response.json()))

# cHECKING RESPONSE CODE
#print(response.status_code)

#checking header type
# print(response.headers['Content-Type'])

#retrive a book having isbn no SK485
# book_list = response.json()

# for book in response.json():
#     if book["isbn"]=="SK485":
#         print(book["book_name"])
    
######### POST A BOOK###############

addBook_response = requests.post("http://216.10.245.166/Library/Addbook.php",
                                 json={
"name":"Learn Appium Automation with Java",
"isbn":"bcdzc",
"aisle":"22757",
"author":"John foe"
},
)
json_response = addBook_response.json()
print(json_response['ID'])
