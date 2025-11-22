import csv

def read_books(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return list(csv.reader(file))

def filter_books_by_genre(books, genre):
    return [book for book in books if book[2] == genre]

def save_books_to_file(books, genre):
    genre_file_map = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt'
    }
    file_name = genre_file_map.get(genre)
    if file_name:
        with open(file_name, 'w', encoding='utf-8') as file:
            for book in books:
                file.write(','.join(book) + '\n')

def process_books(file_name, genre):
    books = read_books(file_name)
    filtered_books = filter_books_by_genre(books, genre)
    save_books_to_file(filtered_books, genre)

file_name = 'books.csv'
genre = input("Enter the genre (Fantasy, Historical, Romance, Classic): ")
process_books(file_name, genre)
