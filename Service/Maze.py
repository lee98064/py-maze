from random import shuffle


class Maze():
    def __init__(self, s) -> None:
        self.size = s
        self.maze = self.generate()
        self.is_end = False  # 紀錄哪些點走過 0,0是起點直接放進去
        self.temp = ["0,0"]  # 判斷是否到終點了

    def run(self, x, y, route):
        if x == self.size-1 and y == self.size-1:  # 跑到終點 不用再跑了
            self.is_end = True
        path = route[str(x)+","+str(y)]  # 把路徑丟給Lpath
        for i in path:
            if i not in self.temp and self.is_end == False:
                n1, n2 = map(int, i.split(","))
                self.maze[n1][n2] = 1
                self.temp.append(i)  # 避免下次再跑到
                self.run(n1, n2, route)

    def generate(self):
        maze = []
        # 建迷宮 二維list
        for _ in range(0, self.size):
            m = [0 for _ in range(0, self.size)]
            maze.append(m)
        return maze

    def random(self):
        route = {}  # 紀錄有哪些路徑
        self.maze[0][0] = 1  # 數字1 代表走過
        # 建立路徑表
        for i in range(0, self.size):
            for j in range(0, self.size):
                route[str(i)+","+str(j)] = []
                # 舉例: 1,1可以走到 0,1 --- route{1,1:"0,1"}
                if i-1 >= 0:
                    route[str(i)+","+str(j)].append(str(i-1)+","+str(j))
                # 舉例: 1,1可以走到 2,1 --- route{1,1:"0,1" ,"2,1"}
                if i+1 < self.size:
                    route[str(i)+","+str(j)].append(str(i+1)+","+str(j))
                # 舉例: 1,1可以走到 1,0 --- route{1,1:"0,1" ,"2,1","1,0"}
                if j-1 >= 0:
                    route[str(i)+","+str(j)].append(str(i)+","+str(j-1))
                # 舉例: 1,1可以走到 1,2 --- route{1,1:"0,1" ,"2,1","1,0","1,2"}
                if j+1 < self.size:
                    route[str(i)+","+str(j)].append(str(i)+","+str(j+1))
        L = route.values()
        # 打亂順序
        for i in L:
            shuffle(i)
        self.run(0, 0, route)
        # 列印迷宮
        return self.maze


# n = Maze(9)
# for i in n.random():
#     print(i)
