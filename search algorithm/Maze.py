
# Search Algorithm

import sys

# Represents a node in the search tree
class Node():
    def __init__(self, state, parent, action):
        self.state = state      # Current position (row, col)
        self.parent = parent    # Node we came from
        self.action = action    # Action taken to reach this node

# Frontier class using Stack (LIFO) for DFS
class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        # Check if state already in frontier
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        # Remove node from end (stack behavior)
        if self.empty():
            raise Exception("empty frontier")
        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node

# Frontier class using Queue (FIFO) for BFS
m.output_image("maze.png", show_explored=True)
