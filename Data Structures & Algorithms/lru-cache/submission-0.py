class Node:
    """A doubly-linked list"""
    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key = key
        self.val = val
        self.prev: Node | None = None
        self.next: Node | None = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict() # values are elements of self.used
        self.used = deque([]) # a dll LRU (key, val) on left
        self.capacity = capacity
        self.size = 0

        self.head = Node() # dummy head
        self.tail = Node() # dummy tail
        self.head.next = self.tail
        self.tail.next = self.head

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        item = self.cache[key]
        self._remove_node(item)
        self._add_node(item)
        return item.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove the node, we're readding it
            self._remove_node(self.cache[key])
        elif self.size == self.capacity:
            oldest = self.tail.prev
            del self.cache[oldest.key]
            self._remove_node(oldest)
        else:
            # we're adding a new node
            self.size += 1
        item = Node(key, value)
        self._add_node(item)
        self.cache[key] = item


    def _remove_node(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_node(self, node: Node):
        # adds node *after* the dummy head
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node              

