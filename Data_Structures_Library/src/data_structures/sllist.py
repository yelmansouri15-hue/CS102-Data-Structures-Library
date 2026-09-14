class SLList:

    class Node:
        def __init__(self, x):
            self.x = x
            self.next = None

    def __init__(self):
        self.n = 0
        self.head = None
        self.tail = None

    def new_node(x):
        return SLList.Node(x)

    # Stack operations (LIFO)

    def _remove(self):
            return self.pop()
    
    def pop(self):
        if self.n == 0: return None
        x = self.head.x
        self.head = self.head.next
        self.n -= 1
        if self.n == 0: 
            self.tail = None
        return x

    def push(self, x):
        node = self.new_node(x)
        node.next = self.head
        self.head = node
        if self.n == 0:
            self.tail = node
        self.n += 1
        return True
        
    def _add(self, x):
        node = self.new_node(x)
        if self.n == 0:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.n += 1
        return True
