# Linked list implementation with Python dictionaries

# head = {
#         "value" : 11,
#         "next" : {
#                     "value" : 3,
#                     "next" : {
#                                 "value" : 23,
#                                 "next" : {
#                                             "value" : 7,
#                                             "next" : None
#                                             }
#                             }

#                     }                    
# }

# print(head['next']['next']['value'])
# print(head['next']['next']['next']['value'])

#This will only run with a Linked List
#print(my_linked_list.head.next.next.next.value)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next:  # Or while temp.next != None:
                pre = temp
                temp = temp.next
            self.tail = pre     # Once we ended the while loop we assign the pre value tp the tail
            self.tail.next = None # Remove the last item 
            self.length -= 1 
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp.value

            



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
print("before pop")
my_linked_list.print_list()
my_linked_list.pop()
print("after pop")
my_linked_list.print_list()
#print(my_linked_list.tail.value)