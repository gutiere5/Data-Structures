class HashTable:
    def __init__(self, size=10):
        """
        Initializes the hash table with a list of empty lists (buckets).
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """
        A simple hash function. It takes a key, sums the ASCII values
        of its characters, and uses the modulo operator to get an index.
        NOTE: Real-world hash functions are far more complex!
        """
        hash_value = 0
        # Ensure the key is a string for this simple hash
        for char in str(key):
            hash_value += ord(char)
        return hash_value % self.size

    ## Insertion / Update Operation
    def set(self, key, value):
        """
        Inserts or updates a key-value pair.
        Average Cost: O(1)
        """
        index = self._hash(key)
        bucket = self.table[index]

        # Check if the key already exists in the bucket to update it
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket[i] = [key, value]  # Update existing key
                return

        # If the key doesn't exist, append the new pair to the bucket
        bucket.append([key, value])

    ## Search Operation
    def get(self, key):
        """
        Retrieves the value associated with a key.
        Average Cost: O(1)
        """
        index = self._hash(key)
        bucket = self.table[index]

        # Search for the key within the bucket's list
        for pair in bucket:
            if pair[0] == key:
                return pair[1]  # Return the value

        # If key is not found
        raise KeyError(f"Key '{key}' not found")

    ## Deletion Operation
    def delete(self, key):
        """
        Deletes a key-value pair.
        Average Cost: O(1)
        """
        index = self._hash(key)
        bucket = self.table[index]

        # Find the key in the bucket and remove it
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return

        # If key is not found
        raise KeyError(f"Key '{key}' not found")


# Let's use it!
my_table = HashTable()
my_table.set("name", "Alice")
my_table.set("age", 30)

print(my_table.get("name"))  # Output: Alice
my_table.set("name", "Bob")  # Update the value for "name"
print(my_table.get("name"))  # Output: Bob

my_table.delete("age")
# print(my_table.get("age")) # This will now raise a KeyError