import copy


class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        it = self.head
        for _ in range(0, self.size):
            yield it.value
            it = it.succeeding

    def push(self, value: int):
        if self.__is_empty():
            self.__add_if_empty(value)
        else:
            curr_tail = self.tail
            self.tail = Node(value, previous=curr_tail)
            curr_tail.succeeding = self.tail

        self.size += 1

    def pop(self) -> int:
        curr_tail = self.tail
        self.tail = curr_tail.previous
        self.size -= 1
        return curr_tail.value

    def shift(self) -> int:
        curr_head = self.head
        self.head = curr_head.succeeding
        self.size -= 1
        return curr_head.value

    def unshift(self, value: int):
        if self.__is_empty():
            self.__add_if_empty(value)
        else:
            curr_head = self.head
            self.head = Node(value, succeeding=curr_head)
            curr_head.previous = self.head

        self.size += 1

    def __is_empty(self):
        return self.head is None

    def __add_if_empty(self, value: int):
        node = Node(value)
        self.head = node
        self.tail = node
