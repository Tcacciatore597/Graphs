
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")
# create a graph using the ancestors being passed in.
# Traverse the graph backwards from the starting node
# find the path with the longest length
# if more than one path has the longest length return the last node with the lower numeric id.
# otherwise return the last node in that path
# if there is no parent ancestor return -1
# neighbors are the parents not the children

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for i in ancestors:
        graph.add_vertex(i)
        graph.add_edge(graph.vertices[i][1], graph.vertices[i][0])

    q = Queue()
    q.enqueue([starting_node])

    visited = set()

    while q:
        path = q.dequeue()
        last = path[-1]
        print(path)
        if last not in visited:
            neighbors = graph.vertices[last]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                q.enqueue(new_path)
        visited.add(last)
