class ListNode:
    def __init__(self, key, val=0, count= 0, next=None, prev = None):
        self.key = key
        self.val = val
        self.count = count
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.tail = None
        

    def get(self, key: int) -> int:

        if key in self.cache:
            self.move_to_head(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        
    def move_to_head(self, cur: ListNode):
        if cur.prev is not None:
            if (cur == self.tail):
                self.tail = cur.prev

            cur.prev.next = cur.next

            if cur.next is not None:
                cur.next.prev = cur.prev
                
            cur.next = self.head
            self.head.prev = cur
            cur.prev = None
            self.head = cur

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.move_to_head(self.cache[key])
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.tail.key]

                if self.tail == self.head:
                    self.head = None
                    self.tail = None
                else:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev

            cur = ListNode(key, value)
            cur.next = self.head
            cur.prev = None

            if (self.head is not None):
                self.head.prev = cur

            self.head = cur

            if (self.tail is None):
                self.tail = cur

            self.cache[key] = cur