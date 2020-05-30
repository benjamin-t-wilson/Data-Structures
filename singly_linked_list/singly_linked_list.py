class ListNode:
    def __init__(self, value, next=None):
        # a SLL can only go one way
        # so we don't need a prev
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        # node defaults to none, so if we init with a value
        # both become the value, otherwise both are none
        self.head = node
        self.tail = node

        # account for the possibility of a starting value
        self.length = 1 if node is not None else 0

    # it makes a little bit of sense to be able to
    # add to head still? But there's no test for that
    def add_to_tail(self, value):
        # create a node
        node = ListNode(value)

        # keep length updated
        self.length += 1

        # if head does not exist, a single node length
        # becomes the head and tail
        if self.head is None:
            self.head = node
            self.tail = node

        # assume we have a head
        else:
            # set the next of the tail from none to our new node
            self.tail.next = node

            # and change the tail
            self.tail = node

    def contains(self, value):
        # since we can't index or loop,
        # we need a way to keep track of where we are
        current_node = self.head

        # if we reach the end of our list, our current node
        # becomes none, and breaks the while loop
        while current_node is not None:

            # do our check
            if current_node.value == value:
                return True

            # continue forward
            current_node = current_node.next

        # upon loop breaking it will run this
        return False

    def remove_head(self):
        # if we don't have a head, this condition will block
        # the entire rest of the function, causing it to return None
        if self.head is not None:

            # set aside this node for use
            current_head = self.head

            # consider we have a head, check if we have only
            # a single node
            if self.head == self.tail:

                # in the event we have a single node,
                # none them both out and return the value for the test
                self.head = None
                self.tail = None
                return current_head.value

            # assuming we have more than one
            # move the head down one
            self.head = self.head.next

            # disconnect the old head from the list entirely
            current_head.next = None

            # return the value for the test
            return current_head.value

    def get_max(self):
        # the test wants a "None" if empty,
        # instead of 0, so we check for that first
        if self.head is None:
            return None

        # set a node to keep track
        node = self.head

        # and increment, also for tracking
        incr = 0

        # and a value for, you guessed it, tracking
        value = 0

        # in hindsight, I could have done a while node is not None,
        # but this does the same thing
        while incr < self.length:
            # increase our increment first off
            incr += 1

            # compare values, if greater, store it
            if value < node.value:
                value = node.value

            # move our node down
            node = node.next

        # the while loop breaks at the end and returns
        # whatever was stored for max
        return value
