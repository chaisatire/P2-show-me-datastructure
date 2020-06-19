class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables

        self.cache_map = dict()
        self.capacity = capacity
        self.num_elements = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache_map:
            print(-1)
            return -1
        self.cache_map[key][1] += 1
        print(self.cache_map[key][0])
        return self.cache_map[key][0]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.cache_map:
            # Move the existing key to the right of dictionary.
            # This is under assumption that modern python dictionaries support a order.
            temp = self.cache_map[key]
            del self.cache_map[key]
            self.cache_map[key] = temp
            # Update the value for the given key
            self.cache_map[key][0] = value
            return

        if self.num_elements == self.capacity:
            self._handle_max_capacity()

        self.cache_map[key] = [value, 0]
        self.num_elements += 1

    def _handle_max_capacity(self):
        """ Support function:
            It searches for the entry which was never used and delete it first.
            we are using min function to find the minimum value present and
            then deleting it.
        """
        dict_values = []

        for key in self.cache_map:
            # Deleting the first entry which was never used
            if self.cache_map[key][1] == 0:
                del self.cache_map[key]
                return
            dict_values.append(self.cache_map[key][1])

        # Finding the minimum used value
        min_value = min(dict_values)

        for key in self.cache_map:
            if self.cache_map[key][1] == min_value:
                del self.cache_map[key]
                return


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

## Test Case 1
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
q = our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
print(our_cache.cache_map)
our_cache.set(6, 6)

# Test Case 2
our_cache.get(3) # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
print(our_cache.cache_map)
