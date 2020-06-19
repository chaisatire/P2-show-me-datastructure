import hashlib
from datetime import datetime


class Block:
    """
       Generating timestamp is quite straight forward using datetime function.
       So only thing required is Data and previous hash
    """

    def __init__(self, data, previous_hash):
        self.timestamp = str(datetime.now())
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.timestamp + data)
        self.next = None

    def calc_hash(self, string):
        """
         Made this function more simple. Using timestamp and data to create the hash.
        """
        sha = hashlib.sha256()
        hash_str = string.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class Blockchain:
    """
       This is the main class which class the helper class to create Block Objects.
       As Blockchain doesn't permit removing data, there is only insert function.
       The implementation is exactly similar to a simple linked list function.
    """

    def __init__(self, ):
        self.head = None

    def insert(self, data=None):
        assert data is not None

        if self.head is None:
            self.head = Block(data, 0)
            return

        node = self.head
        while node.next:
            node = node.next
        prev_hash = node.hash
        node.next = Block(data, prev_hash)


## Test Case 1
block = Blockchain()

try:
    block.insert('First Block Data')
except TypeError:
    print("Multiple values provided. Please provide 1 value to insert\n")
except AssertionError:
    print("No value is provided to add. Please provide 1 value to insert.\n")

try:
    block.insert('Second Block Data')
except TypeError:
    print("Multiple values provided. Please provide 1 value to insert\n")
except AssertionError:
    print("No value is provided to add. Please provide 1 value to insert.\n")

## Test Case 2 - No value to append
try:
    block.insert()
except TypeError:
    print("Multiple values provided. Please provide 1 value to insert\n")
except AssertionError:
    print("No value is provided to add. Please provide 1 value to insert.\n")

# Test case 3 - Too many values:
try:
    block.insert('data1', 'data2', 'data3')
except TypeError:
    print("Multiple values provided. Please provide 1 value to insert\n")
except AssertionError:
    print("No value is provided to add. Please provide 1 value to insert.\n")
