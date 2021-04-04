class LRUCache:
    class NoKeyException(Exception):
        pass
    class Node:
        def __init__(self, key:int, value: int):
            self.key = key
            self.val = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        """ Initialize a doubly-linked list and a hashtable"""
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.hash = dict()

    def get(self, key: int) -> int:
         """Retrieves value from LRU Cache and moves it to the front of the linked list 
         (i.e making it the most recently used).
            O(1) time.
        Parameters:
        key (int): integer key that maps to a value in the LRU Cache
    
        Returns:
        int: returns value from LRU Cache

       """
        if key in self.hash:
            value = self.hash[key].val
            self.delete(key)
            self.add(key, value)      
            return value
        else:
            raise self.NoKeyException("Key does not exist in LRU Cache")

    def put(self, key: int, value: int) -> None:
         """Places value into LRU Cache and updates if the key already exists. 
            Update moves it to the front of the linked-list.
            Putting the value checks if the size of the cache surpasses the capacity which thens deletes the 
            last recently used value.
            O(1) time.
        Parameters:
        key (int): integer key that maps to a value in the LRU Cache
        key (int): integer value to be stored in LRU Cache
        """
        if key in self.hash:
            self.delete(key)
            self.add(key, value)
        else:
            self.add(key, value)
            if len(self.hash) > self.capacity:
                lru = self.tail.prev
                self.delete(lru.key)
            
    def add(self, key: int, value: int) -> None:
        '''Helper function to add to hash and linked-list'''
        node = self.Node(key, value)
        self.hash[key] = node
        
        nxt = self.head.next
        nxt.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        
    def delete(self, key: int) -> None:
        '''Helper function to remove from hash and linked-list'''
        if key in self.hash:
            node = self.hash[key]
            prev = node.prev 
            nxt = node.next

            prev.next = nxt
            nxt.prev = prev
            del self.hash[key]
        else:
            raise self.NoKeyException("Key does not exist in LRU Cache")

        
    def reset(self) -> None:
        """
        Resets the cache.
        """
        self.hash = dict()
        self.head = self.Node(0, 0) # Python has automatic garbage collection so referencing a new head node
        self.tail = self.Node(0, 0) # will delete the old linked list and hash table
        self.head.next = self.tail
        self.tail.prev = self.head