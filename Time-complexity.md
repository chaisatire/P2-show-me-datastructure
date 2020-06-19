# LRU Cache

## Time complexity
1. For `_handle_max_capacity` function, time complexity is `O(n)` as I am using for loop as well min function, to go through all the elements.
2. For rest of the functions, time complexity is `O(1)` as it's simple insertion and deletion operation in the dictionary.

## Design and Space complexity
1. The creation of cache uses Dictionaries as Data Structure. As I want to find the value for key.
2. The design is taken from the cache implementation given during maps. 
3. As dictionary have N elements. The Space complexity is O(n).

# File recursion

## Time complexity
The time complexity for this is `O(n)` As it's standard for recursive functions.

## Design and Space complexity
1. Design is based on simple recursive functions from Recursion section. 
2. I am calling a helper function where I am providing empty variable called list_files. It keeps on getting updated.
3. Using List for Data structure as I only have to append file names. Space complexity is O(n) as there will be N number of items in list.


# Huffman coding

## Time complexity
As I am sorting elements as well as using recursion and iteration through the encoding section, the time complexity is `O(nlog(n)))`

## Design and Space complexity
1. It was already provided that I need to create a Tree for Huffman encoding and decoding.
2. Used heapq as it was given as a hint (use min-heap) and it makes the whole solution quite easy.
3. For creating codes, I have to use recursion as I have to traverse the same tree again and again to get the codes.
4. Space complexity for dictionary used is O(n), for list is O(n). Hence overall space complexity is O(n)


# Active Directory

## Time complexity
As I am using recursive function, the time complexity is `O(n)`

## Design and Space complexity
1. As we have to use users within groups, which can be within groups. Recursion make sense to use.
2. As I am using lists, the space complexity is O(n)


# Blockchain

## Time complexity
As I am using simple linked list, the time complexity is `O(n)`

## Design and Space complexity
1. Design is based on simple linked list as block chain looks like a singly linked list.
2. Space complexity is equal to space complexity of singly linked list i.e. O(n)


# Union and Intersection

## Time complexity
I am using union and intersection of sets. Hence the time complexity is `O(log(n))`

## Design and Space complexity
1. As I have to find unique elements it make sense to use sets.
2. Sets also make intersection and union quite straight forward. And most of my code remains same.
3. I could have even created another function to generate linked list but I wanted to keep code as simple as possible.
2. Space complexity is equal to space complexity of singly linked list i.e. O(n)
