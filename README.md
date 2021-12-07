# LibraryClass
The Library class provides a framework to store multiple Book - objects of the Book class and mimics the functions of a real library. The Library class can turn a list of dictionaries, where each dictionary represents a book and author, into book objects. Books can be displayed in an organized fashion, checked out, and returned.

# Class and Data variables:
name(class variable)(string) - stores the name of the library object, entered as a parameter when creating a library. 

book_collection(data variable) (list)– stores book objects in a list

books_checked(data variable)(integer) – stores the number of books checked out as an integer


# Methods:
set_book_collection – requires one list (of dictionaries) argument with the format:
[{“author”:”book author”,”title”:”book title”}, {“author”:”book author 2”,”title”:”book title 2”},(….)]
Turns all dictionaries into book objects and adds them to book_collection.

get_book_collection – returns an organized string of books in the library showing for each book: the author, title, and whether the book is checked out or not.

check_out_book – prompts terminal for a book title and prints whether the entered book was successfully checked out, is already checked out, or is not contained in the library. 

return_book – prompts terminal for a book to be returned and prints whether the entered book was successfully returned, is not checked out, or is not contained in the library.

# Demo Program:

Creates a terminal environment where user can enter commands to run the methods of two different library objects, and navigate between each library.

Instructions to run: Launch the program in the terminal using python 3, commands are provided once program is launched. (optional) change ‘Books’ data in the script to add and remove different books before running. 



