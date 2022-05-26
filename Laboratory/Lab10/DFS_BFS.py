from Stack import Stack
from Queue import Queue
from Graph import Graph


def dfs(g, start): # DFS is a stack
    """
    given a graph and a start point node as an input
    return list of visited nodes DFS
    """
    S = Stack()
    S.push(start)
    visited = []
    while not S.isEmpty():
        node = S.pop()
        if node not in visited:
            visited.append(node)
            for child in g.children(node):
                if child not in visited:
                    S.push(child)
    return visited
    
    
def bfs(g, start): #  BFS is a queue
    """
    given a graph and a start point node as an input
    return list of visited nodes BFS
    """
    Q = Queue()
    Q.enqueue(start)
    visited = []
    while not Q.isEmpty():
        node = Q.dequeue()
        if node not in visited:
            visited.append(node)
            for child in g.children(node):
                if child not in visited:
                    Q.enqueue(child)
    return visited

if __name__ == "__main__":
    ### DO NOT MODIFY
    nodes = [1, 2, 3, 4, 5, 6]

    ### DO NOT MODIFY
    pairs = [(1, 2), (3, 4), (4, 6), (1, 6), (2, 3)]


    ###############################################################################
    # Complete the tasks using the Graph Class (Directional)
    print("" + "="*30 + " Directional Graph " + "="*30 + "")
    g = Graph(nodes, True) # DONE: Should be a directional graph

    # Adds all the edges to the graph
    for p in pairs:
        g.add_edge(p)
    print("dfs list:")
    print(dfs(g, 1))
    print("bfs list")
    print(bfs(g,1))

