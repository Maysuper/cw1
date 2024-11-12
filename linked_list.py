class Node:
    """
    Node class representing an element in the LinkedList.
    Each node contains a book_id and a reference to the next node.
    """
    def __init__(self, book_id):
        self.book_id = book_id  # Unique identifier for the book
        self.next = None  # Reference to the next node in the list


class LinkedList:
    """
    LinkedList class to manage a queue of book returns.
    """
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None  # Points to the first node in the list
        self.tail = None  # Points to the last node in the list

    def enqueue(self, book_id):
        """
        Adds a book return to the end of the queue.
        
        Parameters:
            book_id (int): Unique identifier for the book being returned.
        """
        new_node = Node(book_id)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if not self.head:
            self.head = new_node
        print(f"Book with ID {book_id} added to the return queue.")

    def dequeue(self):
        """
        Removes and returns the book at the front of the queue.
        
        Returns:
            int: The book_id of the removed book, or None if the queue is empty.
        """
        if not self.head:
            return None
        removed_book_id = self.head.book_id
        self.head = self.head.next
        if not self.head:
            self.tail = None
        print(f"Book with ID {removed_book_id} removed from the return queue.")
        return removed_book_id

    def display(self):
        """
        Displays all book IDs in the return queue.
        """
        current = self.head
        print("Return Queue:")
        while current:
            print(f"Book ID {current.book_id}")
            current = current.next
