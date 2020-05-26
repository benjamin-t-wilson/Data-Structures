class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def add_to_tail(self, value):
        node = ListNode(value)
        self.length += 1
        # if head does not exist
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        # if head exists

    def contains(self, value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def remove_head(self):
        if self.head is not None:
            current_head = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return current_head.value
            self.head = self.head.next
            current_head.next = None
            return current_head.value

    def get_max(self):
        if self.head is None:
            return None
        node = self.head
        incr = 0
        value = 0
        while incr < self.length:
            incr += 1
            if value < node.value:
                value = node.value
            node = node.next
        return value
