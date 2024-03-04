class Book:
    def __init__(self, Title, Author, Price):
        self.Title = Title
        self.Author = Author
        self.Price = Price.replace('$', '')

    def view(self):
        print(
            f"Book Title: -> {self.Title} Book Author: -> {self.Author} Book Price: -> {self.Price} $")


my_book = Book('Python Complete Reference', 'Tony stark', '$28')

my_book.view()
