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

    def _add(self, x):
        node = self.new_node(x)
        if self.n == 0:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.n += 1
        return True
