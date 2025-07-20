class Books:
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self. year = year
        self.status = "Available!"
    
    def show_info(self):
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Book Year: {self.year}")
        print(f"Book Status: {self.status}")
    
    def borrow_book(self):
        self.status = "Book is already borrowed!"
    
    def return_book(self):
        self.status = "Available!"
    

book1 = Books("Science", "Micheal Jordan", 2002)
book1.return_book()
book1.show_info()