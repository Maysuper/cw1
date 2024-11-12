import heapq

class MinHeap:
    """
    MinHeap class that uses Python's built-in heapq library to manage loan due dates.
    Each entry in the heap is a tuple containing (due_date, book_id), 
    where 'due_date' is the priority key for maintaining the heap order.
    """

    def __init__(self):
        """
        Initializes an empty MinHeap for managing loans based on due dates.
        """
        self.heap = []  # Initialize an empty list to store the heap elements

    def insert(self, due_date, book_id):
        """
        Inserts a new loan record into the heap.
        
        Parameters:
            due_date (str): The due date of the loan, formatted as 'YYYY-MM-DD'.
            book_id (int): The unique ID of the book on loan.
        """
        heapq.heappush(self.heap, (due_date, book_id))
        print(f"Inserted book with ID {book_id} due on {due_date} into the loan management system.")

    def get_earliest_due(self):
        """
        Retrieves the loan with the earliest due date without removing it.
        
        Returns:
            tuple: A tuple (due_date, book_id) representing the earliest due loan, or None if empty.
        """
        if self.heap:
            return self.heap[0]  # Peek at the root of the heap (earliest due date)
        return None

    def remove_earliest_due(self):
        """
        Removes and returns the loan with the earliest due date.
        
        Returns:
            tuple: A tuple (due_date, book_id) representing the earliest due loan, or None if empty.
        """
        if self.heap:
            earliest_due = heapq.heappop(self.heap)
            print(f"Removed book with ID {earliest_due[1]} due on {earliest_due[0]} from the loan management system.")
            return earliest_due
        return None

    def display(self):
        """
        Displays all loans in the heap sorted by due date.
        """
        print("Loan Due Dates (Min-Heap):")
        for due_date, book_id in sorted(self.heap):
            print(f"Book ID {book_id} due on {due_date}")

