class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            temp = self.top
            self.top = new_node
            self.top.next = temp
            # OR
            # new_node.next = self.top
            # self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top # store reference of the value to be popped out
            self.top = self.top.next # move the reference of the top to the next node
            temp.next = None # remove the reference of the old top Node
        self.height -= 1 # decrement the height of the stack
        return temp

my_stack = Stack(1)
my_stack.push(2)
my_stack.push(3)
my_stack.print_stack()
print('\n')
my_stack.pop()
#my_stack.push(3)
my_stack.print_stack()