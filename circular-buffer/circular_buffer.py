from collections import deque


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque()

    def clear(self):
        self.buffer.clear()

    def read(self):
        try:
            return self.buffer.popleft()
        except IndexError:
            raise BufferEmptyException("buffer is empty")

    def write(self, data):
        if len(self.buffer) == self.capacity:
            raise BufferFullException("buffer is full")
        self.buffer.append(data)

    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            self.read()
        self.buffer.append(data)
