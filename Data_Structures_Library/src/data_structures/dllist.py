class DLList:

    class Node:
        def __init__(self, x):
            self.x = x
            self.prev = None
            self.next = None

    def __init__(self):
        self.n = 0
        self.dummy = DLList.Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def new_node(self, x):
        return DLList.Node(x)

    def clear(self):
        self.__init__()
    
    # Handles invalid index
    def error(self, i):
        if i < 0 or i >= self.n : raise IndexError

