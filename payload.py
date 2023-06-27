def addBook(isbnValue):
    bookdata={
        "name":"Learn Appium Automation with Java",
        "isbn":isbnValue,
        "aisle":"227571",
        "author":"Ashutosh"}
    return bookdata

def deleteBook(id):
    deleteInf = {
        "ID" : id
    }
    return deleteInf

