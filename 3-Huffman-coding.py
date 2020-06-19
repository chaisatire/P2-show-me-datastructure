import sys
import heapq


class Node(object):

    def __init__(self, char=None, weight=None):
        self.char = char
        self.weight = weight
        self.left = None
        self.right = None

    # less than operator, this is required for heapq library.
    def __lt__(self, other):
        return self.weight < other.weight


# Function to find  frequency of data
def find_freq(data):
    data_freq = {}
    for i in data:
        if i in data_freq:
            data_freq[i] += 1
        else:
            data_freq[i] = 1
    return data_freq


# Function to find codes from Huffman's tree
def make_codes(root, current_code, codes):
    # Base case 1
    if (root == None):
        return
    # Base case 2
    if (root.char != None):
        codes[root.char] = current_code
        return

    make_codes(root.left, current_code + "0", codes)
    make_codes(root.right, current_code + "1", codes)


def huffman_encoding(data):
    """
       Huffman Encoding function. It does below:
       1. Takes data and find it's frequency in dictionary form
       2. Creates a list of Node object from dictionary data.
       3. Heapify the list and creates a Huffman Tree
       4. There are two cases of string
       5. First case when the string consist of only 1 character.
       6. Second is the general case when there are multiple characters.
       7. We call a recursive function "make_codes" to generate codes.
       8. In the end encoded_data is created from the coes generated.

       For code generation logic and joining the nodes logic,
       I took help to understand logic from already posted questions in knowledge@Udacity
    """
    # Return None of empty data
    if len(data) == 0:
        return None, None

    data_freq = find_freq(data)

    ## Place holders for encoded_data, codes and heap
    encoded_data = ""
    current_code = ""
    codes = {}
    my_heap = []

    ## Heapify the data
    for key in data_freq:
        my_heap.append(Node(key, data_freq[key]))

    heapq.heapify(my_heap)

    """ 
        Start Creating HuffMan's Tree 

    """
    # Edge condition when there is only 1 character
    if len(my_heap) == 1:
        root = Node(None, 1)
        root.left = my_heap[0]
        make_codes(root, current_code, codes)
        for character in data:
            encoded_data += codes[character]
        return encoded_data, root

    # General Case when there are multiple characters in string given
    while len(my_heap) > 1:
        node1 = heapq.heappop(my_heap)
        node2 = heapq.heappop(my_heap)
        new_node = Node(None, node1.weight + node2.weight)
        new_node.left = node1
        new_node.right = node2
        heapq.heappush(my_heap, new_node)

    ## Creating codes from the Huffman Tree created
    root = heapq.heappop(my_heap)
    make_codes(root, current_code, codes)

    ## Creating encoded data
    for character in data:
        encoded_data += codes[character]

    return encoded_data, root


def huffman_decoding(data, tree):
    """
       Huffman Decoding is a simple function which decodes the data using tree provided.
       The traversal is as explained in problem statement for Huffman's decoding.
    """
    # Return None when empty data or tree is provided.
    if data == None or tree == None:
        return None

    decoded_data = ""

    # Start decoding data
    node = tree
    for chars in data:
        if chars == '1':
            if node.right.char is None:
                node = node.right
            else:
                decoded_data += node.right.char
                node = tree
        else:
            if node.left.char is None:
                node = node.left
            else:
                decoded_data += node.left.char
                node = tree
    return decoded_data


if __name__ == "__main__":
    codes = {}

    ## Test Case 1

    print("\n ### Start of Test Case 1: \n ")

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print("\n ### Start of Test Case 2: \n ")

    ## Test Case 2

    small_sentence = "iiiii"

    print("The size of the data is: {}\n".format(sys.getsizeof(small_sentence)))
    print("The content of the data is: {}\n".format(small_sentence))

    encoded_data, tree = huffman_encoding(small_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
