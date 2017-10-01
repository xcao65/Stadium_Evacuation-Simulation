from math import pi
from sets import Set
from location import *
from cell import *
from collections import deque

class Roadmap:
    neighborRandians = {0.75*pi, 0.5*pi,
			0.25*pi, 0.0, -0.25*pi, -0.5*pi, -0.75*pi, -pi}

    def __init__(self):
        container = None
        entries = None
        exits = None

    def __init__(self, container, entries, exits):
        self.container = container # 2-d array from ndarray in numpy
        self.entries = entries     # list of entry
        self.exits = exits         # list of exit
        print "exit number is ", len(self.exits)
        for exit in exits:
            exit.set_path(self.shortest_path(exit))

    def get_cell(self, x, y):
        if x < 0 or y < 0 or x >= len(self.container) or y >= len(self.container[0]):
            return None
        else:
            return self.container[x][y]

    def get_x_length(self):
        return len(self.container) if self.container else 0

    def get_y_length(self):
        return len(self.container[0]) if self.container else 0

    def get_entries(self):
        return self.entries

    def get_entries_num(self):
        return len(self.entries) if self.entries else 0

    def get_exits(self):
        return self.exits

    def get_exit_num(self):
        return len(self.exits) if self.exits else 0

    def shortest_path(self, exit):
        x = [-1, -1, -1, 0, 0, 1, 1, 1]
        y = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited = Set([])
        m = len(self.container)
        n = len(self.container[0])
        dist = [[-1 for i in range(n)] for j in range(m)]

        q = deque([])
        new_x, new_y = int(exit.get_x()), int(exit.get_y())
        q.append(Location(new_x, new_y, 0))
        print "get a new exit: (%s, %s)"  %(new_x, new_y)
        dist[new_x][new_y] = 0
        while len(q) > 0:
            p = q.popleft()
            px, py = int(p.get_x()), int(p.get_y())
            visited.add((px, py))
            for i in range(8):
                a = px + x[i]
                b = py + y[i]

                if a>-1 and b >-1 and a<m and b<n:
                    if dist[a][b] == -1 and self.container[a][b].get_cell_type() != "block":
                        dist[a][b] = 1 + dist[px][py]
                        if (a,b) not in visited: q.append(Location(a,b,0))
        # end of while loop
        return dist


if __name__ == '__main__':
    pass
