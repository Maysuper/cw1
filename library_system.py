# library_system.py

from hash_table import HashTable
from min_heap import MinHeap
from linked_list import LinkedList

class LibrarySystem:
    """
    LibrarySystem class manages the book catalog, loan system, and return queue.
    It integrates HashTable for fast book lookups, MinHeap for prioritizing loans,
    and LinkedList for the return queue.
    """
    
    def __init__(self):
        """
        Initializes the library system with a HashTable for the catalog,
        a MinHeap for loan management, and a LinkedList for the return queue.
        """
        self.catalog = HashTable()            # Stores books with unique IDs
        self.loan_management = MinHeap()      # Manages loans by due dates
        self.returns_queue = LinkedList()     # Manages the order of book returns

    def add_book(self, book_id, book_title):
        """
        Adds a book to the catalog.
        
        Parameters:
            book_id (int): Unique identifier for the book.
            book_title (str): Title of the book.
        """
        self.catalog.insert(book_id, book_title)
        print(f"Book '{book_title}' added to the catalog with ID {book_id}.")

    def search_book(self, book_id):
        """
        Searches for a book in the catalog by book ID.
        
        Parameters:
            book_id (int): Unique identifier for the book.
            
        Returns:
            str: Title of the book if found, else None.
        """
        book_title = self.catalog.search(book_id)
        if book_title:
            print(f"Book found: {book_title}")
        else:
            print("Book not found in catalog.")
        return book_title

    def loan_book(self, book_id, due_date):
        """
        Loans a book to a user and adds it to the loan management system (MinHeap).
        
        Parameters:
            book_id (int): Unique identifier for the book.
            due_date (str): Due date for returning the book in YYYY-MM-DD format.
        """
        book_title = self.catalog.search(book_id)
        if book_title:
            # Insert into the MinHeap with (due_date, book_id) for priority handling
            self.loan_management.insert((due_date, book_id))
            print(f"Book '{book_title}' loaned out with due date: {due_date}.")
        else:
            print("Book not found in catalog. Cannot loan.")

    def return_book(self, book_id):
        """
        Returns a book to the library and adds it to the return queue (LinkedList).
        
        Parameters:
            book_id (int): Unique identifier for the book.
        """
        book_title = self.catalog.search(book_id)
        if book_title:
            # Add the book_id to the returns queue
            self.returns_queue.append(book_id)
            print(f"Book '{book_title}' added to the return queue.")
        else:
            print("Book not found in catalog. Cannot return.")

    def process_next_return(self):
        """
        Processes the next book in the return queue, removing it from the queue
        and updating the catalog status accordingly.
        
        Returns:
            str: Title of the processed book if there was one in the queue, else None.
        """
        book_id = self.returns_queue.pop()
        if book_id is not None:
            book_title = self.catalog.search(book_id)
            print(f"Processed return for book: {book_title}")
            return book_title
        else:
            print("No books in return queue.")
            return None

    def get_next_due_loan(self):
        """
        Retrieves and processes the loan with the earliest due date.
        
        Returns:
            tuple: (due_date, book_id) of the next due loan if available, else None.
        """
        next_due = self.loan_management.extract_min()
        if next_due:
            due_date, book_id = next_due
            book_title = self.catalog.search(book_id)
            print(f"Next due loan: Book '{book_title}' with due date {due_date}.")
            return next_due
        else:
            print("No outstanding loans.")
            return None

    def display_catalog(self):
        """
        Displays all books currently in the catalog.
        """
        print("Library Catalog:")
        for index, bucket in enumerate(self.catalog.table):
            for book_id, book_title in bucket:
                print(f" - ID: {book_id}, Title: '{book_title}'")

    def display_loaned_books(self):
        """
        Displays all currently loaned books in the system with their due dates.
        """
        print("Currently Loaned Books (by due date):")
        for item in self.loan_management.heap:
            due_date, book_id = item
            book_title = self.catalog.search(book_id)
            print(f" - Book ID: {book_id}, Title: '{book_title}', Due Date: {due_date}")

    def display_return_queue(self):
        """
        Displays the books in the return queue in the order they are to be processed.
        """
        print("Return Queue:")
        current = self.returns_queue.head
        while current:
            book_id = current.data
            book_title = self.catalog.search(book_id)
            print(f" - Book ID: {book_id}, Title: '{book_title}'")
            current = current.next
