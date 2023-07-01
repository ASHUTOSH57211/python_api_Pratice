Feature: verify if a book is added successfull
    Scenario: ADD BOOK 
        Given Book details needed for the Library
        When we execute the add Book POST API method
        Then Book added successfully
#implemention of HOOKS with multiple data sent as parameters
    Scenario Outline: ADD BOOK
        Given Book details needed for the Librar ywith parameters like <isbn> and <aisle>
        When we execute the add Book POST API method 
        Then Book added successfully
        Examples:
            | isbn | aisle |
            | cksedf | 2323  |
            |  juyt  | 3464  |
        
    