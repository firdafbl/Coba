class Book:
    def __init__(self, id, title, is_borrowed=False):
        self.id = id
        self.title = title
        self.is_borrowed = is_borrowed

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, id, title):
        self.books.append(Book(id, title))
    print()
    print("================LIBRARY FIRDA================")
    print()
    def borrow_book(self, id, borrower):
        for book in self.books:
            if book.id == id and not book.is_borrowed:
                book.is_borrowed = True
                print(f"Buku {book.title} dipinjam oleh {borrower}")
                return
        print(f"Buku dengan ID {id} tidak ditemukan atau sudah dipinjam")

    def get_total_books(self):
        return len(self.books)

    def get_borrowed_books(self):
        return len([book for book in self.books if book.is_borrowed])

# Buat perpustakaan baru
library = Library()

# Tambahkan beberapa buku
library.add_book(1, "Kalkulus")
library.add_book(2, "Fisika")
library.add_book(3, "Sistem Digital")
library.add_book(4, "Matematika")
library.add_book(5, "Organisasi Komputer")

# Pinjam buku dengan ID 1
library.borrow_book(1, "Nabilla")

# Pinjam buku dengan ID 2
library.borrow_book(5, "Fira")
print("=============================================")

# Cetak total buku
print(f"Total buku                  : {library.get_total_books()}")

# Cetak total buku yang dipinjam
print(f"Total buku yang dipinjam    : {library.get_borrowed_books()}")
print("=============================================")