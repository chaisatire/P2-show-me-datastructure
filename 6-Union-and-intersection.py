class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def find_sets(node1, node2):
    """
    Helper function which finds sets from the nodes given.
    The sets fetched can be used by main function for further set operations
    """
    set1 = set()
    set2 = set()
    while node1:
        set1.add(node1.value)
        node1 = node1.next
    while node2:
        set2.add(node2.value)
        node2 = node2.next
    return set1, set2


def union(llist_1, llist_2):
    """
       Here, First I am generating nodes from lists given.
       Using helper function to get the sets from these nodes.
       Once I have sets, I am using set union operation.
       Once I have union, it's quite easy to create a linked list out of it.
    """
    node1 = llist_1.head
    node2 = llist_2.head
    set1, set2 = find_sets(node1, node2)
    union_set = set1 | set2
    union_list = LinkedList()
    for elements in union_set:
        union_list.append(elements)
    return 'The union of provided linked lists is: {}'.format(union_list)


def intersection(llist_1, llist_2):
    """
       Here, First I am generating nodes from lists given.
       Using helper function to get the sets from these nodes.
       Once I have sets, I am using set intersection operation.
       Once I have intersection, it's quite easy to create a linked list out of it.
    """
    node1 = llist_1.head
    node2 = llist_2.head
    set1, set2 = find_sets(node1, node2)
    intersection_set = set1 & set2
    intersection_list = LinkedList()
    for elements in intersection_set:
        intersection_list.append(elements)
    if intersection_list.head is None:
        return ("The intersection is empty as either the sets doesn't contain common elements or one of the list "
                "provided is empty")
    else:
        return 'Intersection of provided linked lists is:  {}'.format(intersection_list)


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))
print("\n\n")
# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
print("\n\n")

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))