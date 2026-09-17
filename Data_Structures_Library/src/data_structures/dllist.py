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

    def get(self, i):
        self.error(i)

        if i < self.n/2:
            node = self.dummy.next
            for _ in range (i):
                node = node.next

        node = self.dummy
        for _ in range (self.n,i,-1):
            node = node.prev

        return node

    def set(self, i, x):
        node = self.get(i)
        y = node.x
        node.x = x
        return y
