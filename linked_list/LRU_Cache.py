class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # This hashmap maps key to Nodes

        # left = LRU, right = Most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Basic pointer fns: remove & insert
    # 1. Removes LRU node
    def remove(self, node):
        # node is middle Node
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev  # Node is now no longer in b/w prev & nxt

    # 2. Inserts Most recently accessed node at right b/w right ptr
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # Update Most recent everytime get is called
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            # self.cache[key] is the node as each key is mapped to a value
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        if a key exists in hashmap (cache), it means
        a node already exists in our list with that
        same key value. So before we insert the new
        key, we need to remove existing one.
        """
        if key in self.cache:
            self.remove(self.cache[key])
        # Create a new node with Key Val & put it in hashmap
        self.cache[key] = Node(key, value)
        # Also insert this Node in Doubly LL
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from list & del LRU node from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
