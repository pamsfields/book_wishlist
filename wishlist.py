#Main program

import ui, datastore
from book import Book


def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        sort_book()

    elif choice == '6':
        search_book()

    elif choice == '7':
        edit_book()

    elif choice == '8':
        delete_book()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    '''Fetch and show all unread books'''
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    '''Fetch and show all read books'''
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    ''' Get choice from user, edit datastore, display success/error'''
    book_id = ui.ask_for_book_id()
    rating = ''
    while rating not in range(1,5):
        try:
            rating = int(input('Please enter a rating low (1) to high (5):'))
            if rating not in range(1,5):
                ui.message('Rating is not in range, please try again')
        except ValueError:
            ui.message('Please enter a valid integer')

    rating = ('*' * rating)

    if datastore.set_read(book_id, True):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')

def delete_book():
    '''Get book id from user, delete selected book if '''
    book_id = ui.ask_for_book_id()
    if datastore.delete_book(book_id):
        ui.message('Book deleted')
    else:
        ui.message('Book id not found in database')

def new_book():
    '''Get info from user, add new book'''
    new_book = ui.get_new_book_info()
    datastore.add_book(new_book)
    ui.message('Book added: ' + str(new_book))

def sort_book():
    '''Sort the books either by title or by author'''
    books_to_sort = datastore.get_books()
    sortBook = int(input('Enter the sort option. 1 = title, 2 = author: '))
    while True:
        if(sortBook == 1):
            sorted_books = sorted(books_to_sort, key = lambda book: book.title)
            ui.show_list(sorted_books)
            break
        elif(sortBook == 2):
            sorted_books = sorted(books_to_sort, key = lambda book: book.author)
            ui.show_list(sorted_books)
            break
        else:
            sortBook = int(input('Enter the correct options (1 = title, 2 = author): '))

def search_book():
    books_to_search = datastore.get_books()
    search_id = int(input('Enter book\'s id to begin search: '))
    books = [book for book in books_to_search if book.id == search_id]
    if len(books) == 0:
        ui.message('Book not found.')
    else:
        for b in books:
            print(b)


def edit_book():
    '''search book by id and edit author and title'''
    book_id = ui.ask_for_book_id()
    if datastore.edit_book(book_id):
        ui.message('Book\'s author and title Successfully edited')
    else:
        ui.message('Book not found in the database.')



def quit():
    '''Perform shutdown tasks'''
    datastore.shutdown()
    ui.message('Bye!')


def main():

    datastore.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
