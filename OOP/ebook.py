class EBook:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 1
        self.is_open = False

    def open_book(self):
        if not self.is_open:
            self.is_open = True
            self.current_page = 1
            print(f"The book '{self.title}' is now open.")
        else:
            print(f"The book '{self.title}' is already open.")

    def close_book(self):
        if self.is_open:
            self.is_open = False
            print(f"The book '{self.title}' is now closed.")
        else:
            print(f"The book '{self.title}' is already closed.")

    def next_page(self):
        if self.is_open:
            if self.current_page < self.total_pages:
                self.current_page += 1
                print(f"Turned to page {self.current_page}.")
            else:
                print("You are already on the last page.")
        else:
            print(f"Cannot turn the page. The book '{self.title}' is closed.")

    def previous_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
                print(f"Turned to page {self.current_page}.")
            else:
                print("You are already on the first page.")
        else:
            print(f"Cannot turn the page. The book '{self.title}' is closed.")

    def show_status(self):
        if self.is_open:
            print(f"Book: {self.title}\nAuthor: {self.author}\nPages: {self.total_pages}\nCurrent Page: {self.current_page}")
        else:
            print(f"The book '{self.title}' is closed.")
