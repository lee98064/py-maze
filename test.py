from random import shuffle


def RunMaze(x, y):
    global count
    global total
    global c
    global s
    if x == s-1 and y == s-1:  # 跑到終點 不用再跑了
        c = True
    path = route[str(x)+","+str(y)]  # 把路徑丟給Lpath
    for i in path:
        if i not in temp and c == False:
            n1, n2 = map(int, i.split(","))
            maze[n1][n2] = 1
            temp.append(i)  # 避免下次再跑到
            RunMaze(n1, n2)


s = int(input())  # 迷宮長度
maze = []  # 迷宮
temp = ["0,0"]  # 紀錄哪些點走過 0,0是起點直接放進去
route = {}  # 紀錄有哪些路徑
c = False  # 判斷是否到終點了
# 建迷宮 二維list
for i in range(0, s):
    m = [0 for i in range(0, s)]
    maze.append(m)
maze[0][0] = 1  # 數字1 代表走過
# 建立路徑表
for i in range(0, s):
    for j in range(0, s):
        route[str(i)+","+str(j)] = []
        # 舉例: 1,1可以走到 0,1 --- route{1,1:"0,1"}
        if i-1 >= 0:
            route[str(i)+","+str(j)].append(str(i-1)+","+str(j))
        # 舉例: 1,1可以走到 2,1 --- route{1,1:"0,1" ,"2,1"}
        if i+1 < s:
            route[str(i)+","+str(j)].append(str(i+1)+","+str(j))
        # 舉例: 1,1可以走到 1,0 --- route{1,1:"0,1" ,"2,1","1,0"}
        if j-1 >= 0:
            route[str(i)+","+str(j)].append(str(i)+","+str(j-1))
        # 舉例: 1,1可以走到 1,2 --- route{1,1:"0,1" ,"2,1","1,0","1,2"}
        if j+1 < s:
            route[str(i)+","+str(j)].append(str(i)+","+str(j+1))
L = route.values()
# 打亂順序
for i in L:
    shuffle(i)
RunMaze(0, 0)
# 列印迷宮
for i in maze:
    print(i)
