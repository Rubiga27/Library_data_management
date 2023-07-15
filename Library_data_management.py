class LibraryItem:
    def __init__(self):
        self.__id = None
        self.title = None
        self.year = None

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def library(self):
        print(f"Available book id is {self.id} and title is {self.title} Published in {self.year}")

class Book(LibraryItem):

    def __init__(self):
        super().__init__()
        self.author = None

    def author_name(self):
        print(f"Author name is {self.author}")

class Magazine(Book):
    def __init__(self):
        super().__init__()

        self.issue = None

    def author_name(self, year):
        print(f"This book was issued in the year {year}")


if __name__ == "__main__":
    book = Magazine()
    book.title="Pooniyin Selvan"
    book.id=567
    book.year=1954
    book.author="Kalki Krishnamurthy"
    print(book.title,book.id,book.year,book.author)
    obj=LibraryItem()
    obj.set_id(23)
    obj.title="The Great Gatsby"
    obj.year=1949
    print(obj.get_id())
    obj.library()
    