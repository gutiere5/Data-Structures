import heapq

# Create a priority queue (just a normal list)
pq = []

# Push items onto the heap (insertion)
heapq.heappush(pq, 5)   # pq is now [5]
heapq.heappush(pq, 2)   # pq is now [2, 5]
heapq.heappush(pq, 8)   # pq is now [2, 5, 8]
heapq.heappush(pq, 1)   # pq is now [1, 2, 8, 5]

# Peek at the smallest item (it's always at index 0)
print(f"Smallest item: {pq[0]}") # Output: 1

# Pop the smallest item (deletion)
smallest = heapq.heappop(pq) # returns 1, pq is now [2, 5, 8]
print(f"Popped: {smallest}") # Output: 1
print(f"New smallest item: {pq[0]}") # Output: 2