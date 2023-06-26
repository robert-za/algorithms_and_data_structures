"""
Python Data Structures - A Game-Based Approach
Queue class
Robin Andrews - https://compucademy.net/
"""

from collections import deque
from typing import Any


class Queue:
    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self) -> bool:
        return not self.items

    def enqueue(self, item) -> None:
        self.items.append(item)

    def dequeue(self) -> Any:
        return self.items.popleft()

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> Any:
        return self.items[0]

    def __str__(self) -> str:
        return str(self.items)

if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.is_empty())
    q.enqueue("R")
    q.enqueue("Z")
    q.enqueue("E")
    print(q)
    print(q.dequeue())
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q.peek())
    print(q)
    