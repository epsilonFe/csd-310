import sys
import mysql.connector
from mysql.connector import errorcode
config = {
    "user": "quebook_user",
    "password": "XkuELbuck0",
    "host": "127.0.0.1",
    "database": "quebook",
    "raise_on_warnings": True
}

def show_menu():
    print("\n  -- Main Menu --")
    print("     1. View Books\n     2. View Store Locations\n     3. My Account\n     4. Exit Program")
    
    try:
        choice = int(input('    <Example enter: 1 for book listing>: '))
        return choice
    except ValueError:
        print("\n   Invalid number, program terminated...\n")

        sys.exit(0)

def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, book_year from book")
    book = _cursor.fetchall()
    print("\n  --  DISPLAYING BOOK LISTING --")

    for book in book:
        print("     Book Id: {}\n   Book Name: {}\n   Author: {}\n   Book Year: {}\n".format(book[0], book[1], book[2], book[3]))

def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    
    locations = _cursor.fetchall()
    print("\n   -- DISPLAYING STORE LOCATIONS --")
    for location in locations:
        print("     Locale: {}\n".format(location[1]))

def validate_patron():
    """ validate the patrons ID """
    try:
        patron_id = int(input('\n       Enter a customer id <Example 1 for patron_id 1>: '))
        if patron_id < 0 or patron_id > 3:
            print("\n   Invalid patron number, program terminated...\n")
            sys.exit(0)
        return patron_id
    except ValueError:
        print("\n Invalid patron number, program terminated...\n")
        sys.exit(0)

def show_account_menu():
    """ display the patron account menu"""
    try:
        print("\n       -- Patron Menu --")
        print("     1. Wishlist\n     2. Add Book\n     3. Main Menu")
        account_option = int(input('        <Example enter: 1 for wishlist>: '))
        return account_option
    except ValueError:
        print("\n   Invalid number, program terminated...\n")
        sys.exit(0)

def show_wishlist(_cursor, _patron_id):
    """ query the database for a list of books added to the patron wishlist """
    _cursor.execute("SELECT patrons.patron_id, patrons.first_name, patrons.last_name, book.book_id, book.book_name, book.author " +
                    "FROM wishlist " +
                    "INNER JOIN patrons ON wishlist.patron_id = patrons.patron_id " +
                    "INNER JOIN book ON wishlist.book_id = book.book_id " +
                    "WHERE patrons.patron_id = {}".format(_patron_id))
    wishlist = _cursor.fetchall()

    print("\n       -- DISPLAYING WISHLIST ITEMS --")

    for book in wishlist:
        print("     Book Name: {}\n     Author: {}\n".format(book[4], book[5]))

def show_books_to_add(_cursor, _patron_id):
    """ query the database for a list of books not in the patrons wishlist """
    query = ("SELECT book_id, book_name, author, book_year "
        "FROM book "
        "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE patron_id = {})".format(_patron_id))
    print(query)
    _cursor.execute(query)

    books_to_add = _cursor.fetchall()
    print("\n       -- DISPLAYING AVAILABLE BOOKS --")
    for book in books_to_add:
        print("     Book Id: {}\n       Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _patron_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(patron_id, book_id) VALUES({}, {})".format(_patron_id, _book_id))
try:
    """ try/catch block for handling potential MySQL database errors """
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    print("\n Welcome to the Quebook Application! ")
    user_selection = show_menu()
    while user_selection != 4:
        if user_selection == 1:
            show_books(cursor)
        
        if user_selection == 2:
            show_locations(cursor)
        
        if user_selection == 3:
            patron_id = validate_patron()
            account_option = show_account_menu()
            
            while account_option != 3:
                if account_option == 1:
                    show_wishlist(cursor, patron_id)
                if account_option == 2:
                    show_books_to_add(cursor, patron_id)
                    book_id = int(input("\n     Enter the id of the book you want to add: "))
                    add_book_to_wishlist(cursor, patron_id, book_id)

                    db.commit()

                    print("\n       Book id: {} added to your wishlist!".format(book_id))

                if account_option < 0 or account_option > 3:
                    print("\n   Invalid option, please retry...")

                account_option = show_account_menu()

        if user_selection < 0 or user_selection > 4:
            print("\n   Invalid option, please retry...")
        user_selection = show_menu()
    print("\n  Program terminated...")
except mysql.connector.Error as err:
    """ Handles errors """
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("     The supplied username or password are incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("     The specified database does not exist ")
    else:
        print(err)
finally:
    """ close the connection to MySQL """
    db.close()