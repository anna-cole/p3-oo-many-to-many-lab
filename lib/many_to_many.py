# Each class (Author, Book, and Contract) has a class variable called all. This variable is used to store all instances of the respective class.
# These classes form a simple representation of authors, books, and contracts between them. By using these classes, you can create and manage relationships between authors and books, track contracts, and calculate royalties.

class Author:

    all = []

    def __init__(self, name):
        '''The __init__ method is a special method called a constructor. It is used to initialize an instance of a class. In the Author class, the __init__ method takes a name parameter and sets the name instance variable. It also adds the instance to the all list.'''
        self.name =  name
        Author.all.append(self)

    def contracts(self):
        '''This method should return a list of related contracts (contracts by author). It returns a list of contracts related to the author. It uses a list comprehension to filter the Contract.all list based on the author of each contract.'''
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        '''This method should return a list of related books using the Contract class as an intermediary. It returns a list of books related to the author. It uses the contracts method to get the related contracts and then retrieves the book from each contract.''' 
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        '''This method should create and return a new Contract object between the author and the specified book with the specified date and royalties'''
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        '''This method should return the total amount of royalties that the author has earned from all of their contracts.''' 
        return sum([contract.royalties for contract in self.contracts()]) 
    
class Book:

    all = []

    def __init__(self, title):
        '''In the Book class, the __init__ method takes a title parameter and sets the title instance variable. It also adds the instance to the all list.'''
        self.title = title
        Book.all.append(self)

    def contracts(self):
        '''It returns a list of contracts related to the book. It uses a list comprehension to filter the Contract.all list based on the book of each contract.'''
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        '''It returns a list of authors related to the book. It uses the contracts method to get the related contracts and then retrieves the author from each contract.'''
        return [contract.author for contract in self.contracts()]
         
class Contract:
    #Contract Validation: The Contract class defines getter and setter methods for the author, book, date, and royalties properties.The setter methods validate that the input objects are of the expected type. If the input object is not of the expected type, an exception is raised

    all = []

    def __init__(self, author, book, date, royalties):
        '''In the Contract class, the __init__ method takes an author, book, date, and royalties parameter. It sets the respective instance variables and adds the instance to the all list.'''
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Input object is not of type Author")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Input object is not of type Book")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Input object is not of type string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Input object is not of type number")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        '''The contracts_by_date method in the Contract class returns a list of contracts with the specified date. It uses a list comprehension to filter the Contract.all list based on the date of each contract.'''
        return [contract for contract in cls.all if contract.date == date]

        
           


        



