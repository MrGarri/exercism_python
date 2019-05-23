class Node(object):

    def __init__(self, value):
        self._value = value
        self.next_node = None

    def value(self):
        return self._value

    def next(self):
        return self.next_node


class LinkedList(object):
    def __init__(self, values=[]):
        self._values = values
        self._len = 0
        self._head = None

        for value in values:
            self.push(value)

    def __len__(self):
        return self._len

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.value()
            current = current.next()

    def head(self):
        if len(self) > 0:
            return self._head
        else:
            raise EmptyListException("List cannot be empty.")

    def push(self, value):
        if len(self) == 0:
            self.__push_when_emtpy(value)
        else:
            tmp = self.head()
            node = Node(value)
            node.next_node = tmp
            self._head = node
            self._len += 1

    def pop(self):
        if len(self) == 0:
            raise EmptyListException("List cannot be empty.")

        result = self.head()
        self._head = result.next()
        self._len -= 1

        return result.value()

    def reversed(self):
        return reversed(list(self))

    def __push_when_emtpy(self, value):
        node = Node(value)
        self._head = node
        self._len += 1


class EmptyListException(Exception):
    pass
