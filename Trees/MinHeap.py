class MinHeap:
    def __init__(self):
        """
        Initializes the heap with an empty list.
        """
        self.heap = []

    def _get_parent_index(self, i):
        return (i - 1) // 2

    def _get_left_child_index(self, i):
        return 2 * i + 1

    def _get_right_child_index(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    ## Insertion Operation
    def insert(self, value):
        """
        Adds a new value to the heap.
        Cost: O(log n)
        """
        # 1. Add the element to the end of the list
        self.heap.append(value)

        # 2. "Bubble up" to maintain the heap property
        current_index = len(self.heap) - 1
        parent_index = self._get_parent_index(current_index)

        # While we are not at the root and the child is smaller than its parent
        while current_index > 0 and self.heap[current_index] < self.heap[parent_index]:
            self._swap(current_index, parent_index)
            current_index = parent_index
            parent_index = self._get_parent_index(current_index)

    ## Deletion Operation
    def delete(self):
        """
        Removes and returns the smallest element (the root).
        Cost: O(log n)
        """
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        # 1. Save the root (the minimum value) to return later
        root = self.heap[0]

        # 2. Move the last element to the root
        self.heap[0] = self.heap.pop()

        # 3. "Bubble down" to restore the heap property
        current_index = 0
        while True:
            left_child_index = self._get_left_child_index(current_index)
            right_child_index = self._get_right_child_index(current_index)
            smallest_child_index = current_index

            # Check if left child exists and is smaller than current
            if (left_child_index < len(self.heap) and
                    self.heap[left_child_index] < self.heap[smallest_child_index]):
                smallest_child_index = left_child_index

            # Check if right child exists and is smaller than the current smallest
            if (right_child_index < len(self.heap) and
                    self.heap[right_child_index] < self.heap[smallest_child_index]):
                smallest_child_index = right_child_index

            # If the current node is already smaller than its children, we're done
            if smallest_child_index == current_index:
                break

            # Otherwise, swap with the smaller child and continue down
            self._swap(current_index, smallest_child_index)
            current_index = smallest_child_index

        return root

    ## Search Operation
    def search(self, value):
        """
        Searches for a value in the heap.
        Cost: O(n) - Inefficient!
        """
        # Heaps are not designed for searching. You have to check every element.
        for item in self.heap:
            if item == value:
                return True
        return False