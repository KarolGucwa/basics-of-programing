from ebook import EBook

def main():
    my_book = EBook("The Great Gatsby", "F. Scott Fitzgerald", 180)
    my_book.open_book()
    my_book.show_status()
    my_book.next_page()
    my_book.next_page()
    my_book.show_status()
    my_book.close_book()
    my_book.next_page()

if __name__ == "__main__":
    main()
