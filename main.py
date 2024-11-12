
# 3. Linked List for Queue of Returned Books
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_head(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_value

    def is_empty(self):
        return self.head is None


# 4. LibrarySystem to Interact with Each Data Structure
class LibrarySystem:
    def __init__(self):
        self.books = HashTable()  # Hash table for storing book information
        self.loans = MinHeap()    # Min-heap to prioritize loans by due date
        self.returns = LinkedList()  # Linked list for return queue

    def add_book(self, book_id, book_info):
        self.books.insert(book_id, book_info)
        print(f"Book '{book_info}' added with ID: {book_id}")

    def search_book(self, book_id):
        book_info = self.books.get(book_id)
        if book_info:
            print(f"Book found: {book_info}")
        else:
            print("Book not found.")
        return book_info

    def loan_book(self, book_id, due_date):
        book_info = self.books.get(book_id)
        if book_info:
            self.loans.insert((due_date, book_id))
            print(f"Book '{book_info}' loaned out. Due date: {due_date}")
        else:
            print("Book not available for loan.")

    def return_book(self, book_id):
        book_info = self.books.get(book_id)
        if book_info:
            self.returns.insert_at_tail(book_id)
            print(f"Book '{book_info}' returned.")
        else:
            print("Invalid book ID for return.")

    def process_next_return(self):
        if not self.returns.is_empty():
            book_id = self.returns.remove_from_head()
            book_info = self.books.get(book_id)
            print(f"Processing return for book '{book_info}' with ID: {book_id}")
        else:
            print("No books in the return queue.")

    def get_next_due_book(self):
        if not self.loans.is_empty():
            due_date, book_id = self.loans.get_min()
            book_info = self.books.get(book_id)
            print(f"Next due book: '{book_info}' (ID: {book_id}), Due Date: {due_date}")
        else:
            print("No loans available.")


# 5. Example Usage
if __name__ == "__main__":
    library = LibrarySystem()
    
    # Adding Books
    library.add_book(1, "Data Structures and Algorithms")
    library.add_book(2, "Introduction to Python")
    library.add_book(3, "Advanced Machine Learning")

    # Searching for Books
    library.search_book(1)
    library.search_book(4)  # Not in the library

    # Loaning Books
    library.loan_book(1, "2024-11-15")
    library.loan_book(2, "2024-11-18")

    # Checking Next Due Book
    library.get_next_due_book()

    # Returning Books
    library.return_book(1)
    library.return_book(3)  # Not loaned out, but returned (to check logic)

    # Processing Returns
    library.process_next_return()
    library.process_next_return()
