
"""
A stack class that pops and pushes items from a stack
"""

class Stack:
    #create the constructor
    def __init__ (self):
        self.__stack_list = []

    # The push method
    def push(self, val):
        self.__stack_list.append(val)
    
    #The pop method
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

# instantiate a stack object
stack_object = Stack()

# Push and pop
stack_object.push(3)
stack_object.push("Mary had a car")
stack_object.push(665)
stack_object.push("In the beginingninging")

stack_object.pop()
stack_object.pop()
stack_object.pop()



