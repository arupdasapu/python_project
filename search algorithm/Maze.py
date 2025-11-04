
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
class QueueFrontier(StackFrontier):
    def remove(self):
        # Remove node from front (queue behavior)
        if self.empty():
            raise Exception("empty frontier")
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node

# Maze class: Loads maze from file, finds solution, can output maze
class Maze():
    def __init__(self, filename):
        # Read maze from file
        with open(filename) as f:
            contents = f.read()

        # Validate that there is exactly one start 'A' and one goal 'B'
        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        # Process maze dimensions
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Create wall grid
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    # If no character in line, treat as open space
                    row.append(False)
            self.walls.append(row)

        self.solution = None  # Solution path will be set after solving

    def print(self):
        """Print the maze showing walls, start, goal, and solution (if any)."""
        solution = self.solution[1] if self.solution else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        """Return list of (action, state) pairs for neighbors reachable from current state."""
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        """Solve the maze using DFS or BFS and store the solution path."""

        # Initialize frontier with the start node
        self.num_explored = 0
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()  # Use QueueFrontier() for BFS
        frontier.add(start)

        # Initialize explored set
        self.explored = set()

        # Loop until solution is found
        while True:
            if frontier.empty():
                raise Exception("no solution")

            node = frontier.remove()
            self.num_explored += 1

            # If goal reached, reconstruct the path
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)

    def output_image(self, filename, show_solution=True, show_explored=False):
        """Generate an image of the maze with optional solution and explored paths."""
        from PIL import Image, ImageDraw

        cell_size = 50
        cell_border = 2

        # Create blank image
        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution else None

        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    fill = (40, 40, 40)  # Wall
                elif (i, j) == self.start:
                    fill = (255, 0, 0)  # Start
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)  # Goal
                elif solution and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)  # Solution path
                elif solution and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)  # Explored cells
                else:
                    fill = (237, 240, 252)  # Empty space

                # Draw the cell
                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(filename)

# ===== Main Program =====

# Load maze from file
m = Maze('/content/maze2.txt')

# Print initial maze
print("Maze:")
m.print()

# Solve maze
print("Solving...")
m.solve()

# Print solution
print("States Explored:", m.num_explored)
print("Solution:")
m.print()

# Output maze image with solution and explored paths
m.output_image("maze.png", show_explored=True)