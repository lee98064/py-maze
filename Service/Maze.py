from random import shuffle


class Maze():
    def __init__(self, s) -> None:
        self.size = s
        self.maze = []
        self.mazeC = []

    def get_maze(self):
        self.maze, self.mazeC = self.generate()
        self.randomMaze(0, 0)
        return self.maze

    def generate(self):
        a = []
        b = []
        for i in range(0, self.size):
            m = ["tr" for j in range(0, self.size)]
            a.append(m)
            n = [0 for j in range(0, self.size)]
            b.append(n)
        b[0][0] = 1
        return a, b

    def R(self, x, y):
        self.maze[x][y] = (self.maze[x][y]).replace("r", "")

    def D(self, x, y):
        self.maze[x+1][y] = (self.maze[x+1][y]).replace("t", "")

    def L(self, x, y):
        self.maze[x][y-1] = (self.maze[x][y-1]).replace("r", "")

    def T(self, x, y):
        self.maze[x][y] = (self.maze[x][y]).replace("t", "")

    def randomMaze(self, x, y):
        temp = ["R", "D", "L", "T"]
        shuffle(temp)
        for i in temp:
            if i == "R" and y+1 < self.size and self.mazeC[x][y+1] != 1:
                self.R(x, y)
                self.mazeC[x][y+1] = 1
                self.randomMaze(x, y+1)

            if i == "D" and x+1 < self.size and self.mazeC[x+1][y] != 1:
                self.D(x, y)
                self.mazeC[x+1][y] = 1
                self.randomMaze(x+1, y)

            if i == "L" and y-1 >= 0 and self.mazeC[x][y-1] != 1:
                self.L(x, y)
                self.mazeC[x][y-1] = 1
                self.randomMaze(x, y-1)

            if i == "T" and x-1 >= 0 and self.mazeC[x-1][y] != 1:
                self.T(x, y)
                self.mazeC[x-1][y] = 1
                self.randomMaze(x-1, y)


# n = Maze(6)
# for i in n.get_maze():
#     print(i)
