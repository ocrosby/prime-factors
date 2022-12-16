from collections import deque


class Stack:
    items: deque

    def __init__(self, **kwargs):
        self.items = deque()

        items = kwargs.get("items")

        if items:
            for item in items:
                self.push(item)

    @property
    def size(self):
        return len(self.items)

    @property
    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty:
            return None

        return self.items.pop()

    def peek(self):
        if self.is_empty:
            return None

        return self.items[len(self.items)-1]

