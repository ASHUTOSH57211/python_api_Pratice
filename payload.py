def addBook(isbnValue,aisleValue):
    bookdata={
        "name":"Learn Appium Automation with Java",
        "isbn":isbnValue,
        "aisle":aisleValue,
        "author":"Ashutosh"}
    return bookdata

def deleteBook(id):
    deleteInf = {
        "ID" : id
    }
    return deleteInf

