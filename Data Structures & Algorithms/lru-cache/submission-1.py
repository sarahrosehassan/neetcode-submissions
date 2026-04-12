class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # initialize LRU cache with positive size capacity
        self.capacity = capacity
        # initialize hashmap
        self.hashmap = {}
        # initialize doubly linkedlist
        self.head = Node (0,0)
        self.tail = Node (0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # check hashmap. not there? return -1
        if key not in self.hashmap:
            return -1
        # move node to the front of the linked list (MRU)
        node = self.hashmap[key]
        self.remove(node)
        self.add(node)
        # return the value
        return node.val

    def put(self, key: int, value: int) -> None:
        # If key already exists
        if key in self.hashmap:
        # Update value of key
            node = self.hashmap[key]
            node.val = value
        # Move it to MRU
            self.remove(node)
            self.add(node)
        # return early
            return
        # elif key is new
        node = Node(key, value)
        # If cache is full evict LRU
        if len(self.hashmap) >= self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.hashmap[lru.key]
        # add new node to the front
        self.add(node)
        # Add key to the hashmap
        self.hashmap[key] = node

    def remove(self, node):
        # get previous node's next (right pointer) to point to next
        node.prev.next = node.next
        # get next node's prev (left pointer) to point to previous
        node.next.prev = node.prev

    def add(self, node):
        # add new node's prev (left pointer) pointing to head
        node.prev = self.head
        # add new node's next (right pointer) after the head
        node.next = self.head.next
        # change head's next to point to new node
        self.head.next = node
        # change node.next's prev
        node.next.prev = node
        
        

