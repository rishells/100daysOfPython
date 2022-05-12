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

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head # unnecessary ??
            self.head = self.head.next
            temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            #temp = temp.next
            temp = temp.next
        return temp
        #return temp.value

    def set_value(self, index, value):
        temp = self.get(index)
        #print(f"Temp: {temp}")
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length: # index out of the range
            return False
        if index == 0:                    
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index -1) # to store the previous node of where we are inserting
        new_node.next = temp.next
        temp.next = new_node # remove the reference of previous node to the next and then insert the new node reference
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length: # index out of the range
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        prev = self.get(index -1) # node previous to the removal
        temp = prev.next # node next to the removal
        prev.next = temp.next # copying the refrences of the deleted node to the previous node
        temp.next = None # deleting the wanted node
        self.length -=1 # decreasing the length after the removal
        return temp

    def reverse(self):
        '''1.- First we need to switch the head and the tail
            2.- Add 2 variables before and after to stores the positions as its names
            3.- Iterate 3 variables (before - temp - after  trhough the list
            '''
        temp = self.head 
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next # moves the iteration to the right
            temp.next = before # flips the connection
            before = temp # moves the conection to the rightr in the tail side to the head
            temp = after # makes the rest connection that the movement generated




# my_linked_list = LinkedList(1)
# my_linked_list.append(2)
# my_linked_list.append(3)
# print("before pop")
# my_linked_list.print_list()
# my_linked_list.pop()
# print("after pop")
# my_linked_list.print_list()

# print("before prepend")
# my_linked_list.print_list()
# my_linked_list.prepend(666)
# print("after prepend")
# my_linked_list.print_list()

# print("before pop_first")
# my_linked_list.print_list()
# #my_linked_list.pop_first()
# print("after pop_first")
# my_linked_list.pop_first()
# my_linked_list.print_list()

# print("after pop_first")
# my_linked_list.pop_first()
# my_linked_list.print_list()
# #print(my_linked_list.tail.value)

# Testings for get
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
#my_linked_list.set_value(3,4)
#my_linked_list.insert(1,1)

my_linked_list.print_list()
print("\n")
#my_linked_list.remove(-3)
my_linked_list.reverse()
my_linked_list.print_list()