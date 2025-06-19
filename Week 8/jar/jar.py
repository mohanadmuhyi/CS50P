class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return self.size*"🍪"

    def deposit(self, n):
        if (self.size + n) not in range(0, self.capacity+1):
            raise ValueError
        self.size = self.size + n

    def withdraw(self, n):
        if (self.size - n) not in range(0, self.capacity+1):
            raise ValueError
        self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size=0):
        self._size = size
