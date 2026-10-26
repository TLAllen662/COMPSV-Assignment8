class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    def __init__(self, name: str, number: str):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key: str, value: Contact):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''

    def __init__(self, size: int):
        if size <= 0:
            raise ValueError("Hash table size must be a positive integer.")
        self.size = size
        self.data = [None] * size

    def hash_function(self, key: str) -> int:
        return sum(ord(character) for character in key) % self.size

    def insert(self, key: str, value: str) -> None:
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                current.value.number = value
                return
            current = current.next

        contact = Contact(key, value)
        node = Node(key, contact)
        if self.data[index] is None:
            self.data[index] = node
            return

        current = self.data[index]
        while current.next is not None:
            current = current.next
        current.next = node

    def search(self, key: str) -> Contact | None:
        current = self.data[self.hash_function(key)]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self) -> None:
        for index, node in enumerate(self.data):
            if node is None:
                print(f"Index {index}: Empty")
                continue

            contacts = []
            current = node
            while current is not None:
                contacts.append(f"- {current.value}")
                current = current.next
            print(f"Index {index}: {' '.join(contacts)}")

# Test your hash table implementation here.  