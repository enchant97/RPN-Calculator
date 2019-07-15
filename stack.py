__version__ = "1.0"
class Stack:
    """A simple stack class"""
    def __init__(self, max_size=0):
        """
        Takes max_size of the stack, if 0
        will be infinite size
        """
        self.__stack = []
        self.__max_size = max_size
    
    def clear(self):
        """Clears the stack of all items"""
        self.__stack = []

    def pop(self):
        """
        Removes a item from the stack,
        if stack is empty will return None
        """
        try:
            return self.__stack.pop(0)
        except IndexError:
            return None

    def get_len(self):
        return len(self.__stack)

    def push(self, value):
        """
        Pushes a item to the stack,
        if stack is full will return False
        """
        if self.__max_size == 0 or self.__max_size != len(self.__stack):
            self.__stack.insert(0, value)
            return True
        return False
