class library:
    def __init__(self):
        self.noofbooks = 0
        self.books = []

    def addnooks(self, book):
        self.books.append(book)
        self.noofbooks = len(self.books)

    def info(self):
        print(f'The total books are {self.noofbooks}')
        print(f'Name of the books are: {self.books}')




l = library()

l.addnooks('Harry Potter')

l.info()