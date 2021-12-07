class Library:

    def __init__(self, name):
        #Class Variable
        self.name = name
        #Data Variables
        self.book_collection = []
        self.books_checked = 0

    #turns a list of dictionairies where each dictionary represents a book into a list of book-objects
    def set_book_collection(self, books):
        #empties book collection list 
        self.book_collection = []
        #for each dictionairy in the list, turns into an object based on the dictionairy and adds the object to the list
        for book in books:
            new_book = Book(book["title"], book["author"], False)
            self.book_collection.append(new_book)

    #returns a visually organized string detailing all the books at the library and their status
    def get_book_collection(self):
        #initializing variables
        longest_title = ''
        longest_author = ''
        space_count = 0
        book_title = ''
        book_author = ''
        num_of_books = 0

        #returns a string with as many spaces as the input integer
        def set_spaces(space_count):
            spaces = ''
            for i in range(space_count):
                spaces += ' '
            return spaces
        
        #interates through books and finds the longest title and author 
        for book in self.book_collection:
            if len(longest_title) < len(book.title):
                longest_title = book.title
            if len(longest_author) < len(book.author):
                longest_author = book.author
            #counts number of books
            num_of_books += 1
        
        #creates the header of the string based on longest title and author, shows how many books out of the total are checked out
        book_collection = f"\n{self.books_checked} of {num_of_books} checked out\nTitle: {set_spaces(abs(len(longest_title)-6))} Author: {set_spaces(abs(len(longest_author)-7))}  Status:    \n"

        #iterates through books and authors and adds spaces in respective areas to make sure collums line up
        for book in self.book_collection:
            #adds spaces to the end of book title so each title is same length
            if len(book.title) < len(longest_title):
                space_count = len(longest_title)-len(book.title)
            else: 
                space_count = 0
            book_title = f"{book.title}{set_spaces(space_count)}"

            #adds spaces to the end of author so each author is the same length
            if len(book.author) < len(longest_author):
                space_count = len(longest_author)-len(book.author)
            else:
                space_count = 0
            book_author = f"{book.author}{set_spaces(space_count)}"
            
            #displays Available or Checked Out depending on wether the objects value is true or false
            if book.checked_out == False:
                book_checked = "Available"
            else:
                book_checked = "Checked Out"

            #adds line to book_collection
            book_collection += f"|{book_title} | {book_author} | {book_checked} \n"
        return book_collection

    #allows user to check out book
    def check_out_book(self):
        #prompts user for the title of the book they want to check out
        title = input("What book would you like to check out? \nEnter Book Title:")
        book_found = False
        #iterates through books checking if title matches the user specified title
        for book in self.book_collection:
            #if title is found, makes sure book is not already checked out, if not, sets checked_out to true
            if book.title == title:    
                book_found = True
                if book.checked_out == False:
                    print(f"You have checked out {book.title} by {book.author}")
                    book.checked_out = True
                    #adds 1 to books_checked tally
                    self.books_checked += 1
                elif book.checked_out == True:
                    print(f"Im sorry, {book.title} by {book.author} has already been checked out")
                break
        #if book is not found lets user know
        if book_found == False:
            print(f"Im sorry, the book: {title} does not belong to this library")

    #allows user to return book
    #same code as check_out_book reversed to return instead of check out
    def return_book(self):
        title = input("What book would you like to return? \nEnter Book Title:")
        book_found = False
        for book in self.book_collection:
            if book.title == title:  
                book_found = True 
                if book.checked_out == False:
                    print(f"{book.title} by {book.author} is not currently checked out")
                elif book.checked_out == True:
                    print(f"{book.title} by {book.author} has been succsesfully returned")
                    book.checked_out = False   
                    #subtracts one from books_checked tally
                    self.books_checked -= 1
                break
        if book_found == False:
            print(f"Im sorry, the book: {title} does not belong to this library")

#class for books, stores title, author, and checked out status
class Book:
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.checked_out = status

#demo program
def main():
    
    library = None

    #example book data
    Books = [{"author":"J.K. Rowling", "title":"Harry Potter"},
            {"author":"Carol Dweck", "title":"Mindset"},
            {"author":"Dante Alighieri", "title":"The Divine Comedy"},
            {"author":"Mark Twain", "title":"The Adventures of Huckleberry Finn"},
            {"author":"Lewis Carroll", "title":"Alice's Adventures in Wonderland"},
            {"author":"George Orwell", "title":"Nineteen Eighty Four"}]

    #creates libraries and loads in book data
    McHenry = Library("McHenry")
    McHenry.set_book_collection(Books)

    SnE = Library("Science and Engineering")
    SnE.set_book_collection(Books)

    #infinite loop that takes user commands and executes class functions
    while True:
        #if no library is chosen prompts user to choose a library and sets it to chosen library
        if library == None:
            user = input("Choose a library: type 'm' for McHenry, type 's' for Science and Engineering. Or type 'exit' to end the program\n>>>")
            if user == 'm':
                library = McHenry
            elif user == 's':
                library = SnE
            elif user == 'exit':
                break
            else:
                print("unrecognized library, please try again")
                continue
            #once library is chosen, a welcome message with library name is printed, followed by the books at the library, and finally the available commands
            print(f"Welcome to the {library.name} Library!")
            #shows user available books at chosen library
            print(library.get_book_collection())
            print("\nCommands:\ncheck - to check out a book\nreturn - to return a book\nlibrary - to view available books\nexit - exit the library\nhelp - to view commands\n")
        #user commands
        user = input(">>>")
        if user == "check":
            #class function
            library.check_out_book()
        elif user == "return":
            #class function
            library.return_book()
        elif user == "library":
            #class function
            print(library.get_book_collection())
        elif user == "exit":
            #resets library to none so the user will be prompted again
            library = None
            continue
        elif user == "help":
            print("\nCommands:\ncheck - to check out a book\nreturn - to return a book\nlibrary - to view available books\nexit - exit the library\nhelp - to view commands\n")
        else:
            print("unrecognized command")

#calls main code
if __name__ == "__main__":
    main()