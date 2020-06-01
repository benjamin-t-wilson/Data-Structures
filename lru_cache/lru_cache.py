from collections import OrderedDict
from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.storage = DoublyLinkedList()
        self.size = self.storage.length

        # we're going to use an Ordered Dictionary from the built in
        # collections module of python. This has some cool methods
        # and also cares about the order keys are inserted
        self.dict = OrderedDict()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.dict:
            return None
        else:
            # OrderedDict.move_to_end takes a key and last arg
            # last can be false to move it to front :D
            # this moves the most recently used key to the top

            self.dict.move_to_end(key, last=False)
            return self.dict[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if the key exists already
        if key in self.dict:

            # lets make a loop to update the value in the dll

            node = self.storage.head
            incr = 0
            while incr < self.storage.length:
                incr += 1
                if {key: value} == node.value:
                    self.storage.delete(node)
                    self.storage.add_to_head(node)
                    incr = self.storage.length + 1

            # and then update the dictionary
            # and move it to the front

            self.dict.update({key: value})
            self.dict.move_to_end(key, last=False)

        # if the key doesn't exist, we treat it as new
        # first, we will check to see if we have space for it

        elif self.size < self.limit:
            # if we do have space, it's a simple add
            # update length, and set to the front of the dict

            self.storage.add_to_head(value)
            self.size = self.storage.length
            self.dict.update({key: value})
            self.dict.move_to_end(key, last=False)

        elif self.size >= self.limit:

            # also check to see if we don't have space
            # in which case we will still add to head,
            # but follow with a remove from tail

            self.storage.add_to_head(value)
            self.storage.remove_from_tail()

            # keep size updated
            self.size = self.storage.length

            # add the key to the dict
            # move it to the front
            # delete the last item
            self.dict.update({key: value})
            self.dict.move_to_end(key, last=False)
            self.dict.popitem(last=True)
