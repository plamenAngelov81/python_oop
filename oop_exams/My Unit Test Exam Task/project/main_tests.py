from project.bookstore import Bookstore

store = Bookstore(10)

store.receive_book("Book_1", 5)
store.receive_book("Book_2", 4)
store.sell_book("Book_1", 1)
print(store)