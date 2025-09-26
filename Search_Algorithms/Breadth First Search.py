import collections

# A simple graph represented as an adjacency list
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

def bfs(graph, start_node):
    """
    Performs a Breadth-First Search on a graph.
    """
    visited = set()  # A set to store visited nodes to prevent cycles

    queue = collections.deque([start_node]) #A queue for the BFS algorithm. We'll use collections.deque for efficiency.
    visited.add(start_node)

    # Loop as long as there are nodes to visit in the queue
    while queue:
        current_node = queue.popleft() # Dequeue a vertex from the front of the queue
        print(current_node, end=" ")  # Process the node (in this case, just print it)

        # Get all neighbors of the dequeued node.
        for neighbor in graph[current_node]:
            # If the neighbor has not been visited yet
            if neighbor not in visited:
                # mark it as visited and enqueue it.
                visited.add(neighbor)
                queue.append(neighbor)



print("BFS traversal starting from node 'A':")
bfs(graph, 'A')
# Expected Output: A B C D E F