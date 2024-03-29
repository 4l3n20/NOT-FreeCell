# stack.py: implementation of the Stack ADT using an array structure
# borrowed from Monash Alexandria article
class Stack:
    # creates a new stack
    def __init__(self):
        self.the_stack = []  # represent the stack as a list
        self.count = 0  # indicate the current size of the stack
        self.top = -1  # indicate the top position of the stack

    # returns the number of items in the stack
    def __len__(self):
        return self.count

    # returns True if the stack is empty or False otherwise
    def is_empty(self):
        return len(self) == 0

    # pushes an item onto the top of the stack
    def push(self, item):
        self.the_stack.append(item)
        self.top += 1
        self.count += 1

    # removes and returns the top item on the stack
    def pop(self):
        assert not self.is_empty(), "Cannot pop from an empty stack"
        item = self.the_stack[self.top]
        self.top -= 1
        self.count -= 1
        del self.the_stack[len(self)]
        return item

    # returns the item on the stack without removing it
    def peek(self):
        assert not self.is_empty(), "Cannot peek at an empty stack"
        item = self.the_stack[self.top]
        return item