import numpy

class ArrayList:
    def __init__(self):
        self.a = numpy.empty(1, dtype=object)
        self.n = 0

    def clear(self):
        self.__init__()

    def error(self, i):
        if i < 0 or i >= self.n : raise IndexError

    def get(self, i):
        self.error(i)
        return self.a[i]

    def set(self, i, x):
        self.error(i)
        y = self.a[i]
        self.a[i] = x
        return y

    def add(self, i, x):
        if i < 0 or i > self.n : raise IndexError
        if self.n == len(self.a) : self.resize()
        self.a[i + 1:self.n + 1] = self.a[i:self.n]
        self.a[i] = x
        self.n += 1

    def remove(self, i):
        self.error(i)
        x = self.a[i]
        self.a[i:self.n - 1] = self.a[i + 1:self.n]
        self.n -= 1
        if len(self.a) >= 3*self.n : self.resize()
        return x

    def resize(self):
        b = numpy.empty(max(2*self.n, 1), dtype=object)
        b[:self.n] = self.a[:self.n]
        self.a = b
    
