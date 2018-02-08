from collections import deque


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self._buffer = deque(maxlen=capacity)

    def clear(self):
        self._buffer.clear()

    def read(self):
        try:
            return self._buffer.popleft()
        except IndexError:
            raise BufferEmptyException("buffer is empty")

    def write(self, data):
        if len(self._buffer) == self._buffer.maxlen:
            raise BufferFullException("buffer is full")
        self._buffer.append(data)

    def overwrite(self, data):
        self._buffer.append(data)
