# hash_table.py

class HashTable:
    """
    HashTable class implements a hash table with separate chaining for collision resolution.
    Used for storing and retrieving book information by book ID.
    """

    def __init__(self, size=10):
        """
        Initializes the hash table with a specified size.
        
        Parameters:
            size (int): The initial size of the hash table (default is 10).
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize hash table with empty lists for chaining

    def _hash(self, key):
        """
        Private method to compute hash value of a given key.
        
        Parameters:
            key (int): The key to hash (usually the book ID).
            
        Returns:
            int: The hash index for the given key.
        """
        return key % self.size

    def insert(self, key, value):
        """
        Inserts a key-value pair (book ID and title) into the hash table.
        
        Parameters:
            key (int): Unique identifier for the book.
            value (str): Title of the book.
        """
        index = self._hash(key)
        # Check if the key already exists, update value if found
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                print(f"Updated Book ID {key} with new title '{value}'.")
                return
        # If key is not found, append it to the chain
        self.table[index].append((key, value))
        print(f"Inserted Book ID {key}: '{value}' into the hash table.")

    def search(self, key):
        """
        Searches for a value in the hash table by key.
        
        Parameters:
            key (int): Unique identifier for the book.
            
        Returns:
            str: Title of the book if found, else None.
        """
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v  # Return the value (book title) if found
        return None  # Return None if the key is not found

    def delete(self, key):
        """
        Deletes a key-value pair from the hash table by key.
        
        Parameters:
            key (int): Unique identifier for the book.
            
        Returns:
            bool: True if the key was found and deleted, False otherwise.
        """
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                print(f"Deleted Book ID {key} from the hash table.")
                return True
        print(f"Book ID {key} not found in the hash table.")
        return False

    def display(self):
        """
        Displays all key-value pairs in the hash table.
        """
        print("Hash Table Contents:")
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")
            else:
                print(f"Index {i}: Empty")

