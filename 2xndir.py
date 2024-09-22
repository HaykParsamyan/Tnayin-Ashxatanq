class Girq:
    def __init__(self, book_name, book_author, book_ejer):

        self.name = book_name
        self.author = book_author
        self.ej = book_ejer

    def __str__(self):
        return self.name + ' ' + self.author + ' ' + self.ej

a = Girq('Book1', 'author1', 'ej1')
print(a.__str__())