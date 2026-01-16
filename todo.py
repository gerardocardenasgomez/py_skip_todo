#!/usr/bin/env python3

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        next_node = 'NextNode' if self.next else 'None'
        prev_node = 'PrevNode' if self.prev else 'None'
        return f"Node(value={self.value}, next_node={next_node}, prev_node={prev_node})"

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1

    def remove(self, value):
        current = self.head

        while current:
            if current.value == value:
                # ok this gets sketchy
                if self.size == 1:
                    self.head = None
                    self.tail = None

                elif current == self.head:
                    self.head = self.head.next
                    self.head.prev = None

                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.size -= 1
                return True

            current = current.next

        return False

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __str__(self):
        return '[' + ', '.join(map(repr, self)) + ']'

my_l = CircularList()
my_l.append(5)
my_l.append(4)
my_l.append(3)
my_l.append(2)
my_l.remove(3)
print("Size: ", len(my_l))
print("List: ", my_l)
for item in my_l:
    print("iter: ", item)
