import time
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal


class SolveMaze(QtCore.QThread):

    _signal = pyqtSignal(list)

    def __init__(self, maze, solvetype) -> None:
        super(SolveMaze, self).__init__()
        self.maze = maze
        self.solveType = solvetype

    def __del__(self):
        self.wait()

    def run(self):
        if(self.solveType == "BFS"):
            self.BFS()

        elif(self.solveType == "DFS"):
            self.DFS()

    def DFS(self):
        di = [0, -1, 0, 1]
        dj = [-1, 0, 1, 0]
        h, w = len(self.maze), len(self.maze)
        dist = [[1e9 for i in range(w)] for j in range(h)]
        stack = []
        dfspath = {}
        stack.append([0, 0])
        dist[0][0] = 0
        while len(stack) > 0:
            cur = stack.pop()
            self._signal.emit([cur[0], cur[1], False, {}])
            if(cur == [h-1, w-1]):
                break
            time.sleep(0.1)
            for i in range(4):
                next = [cur[0]+di[i], cur[1]+dj[i]]
                if(0 <= next[0] < h and 0 <= next[1] < w and self.maze[next[0]][next[1]] != 0 and dist[next[0]][next[1]] == 1e9):
                    dist[next[0]][next[1]] = dist[cur[0]][cur[0]] + 1
                    stack.append([next[0], next[1]])
                    dfspath[(cur[0]+di[i], cur[1]+dj[i])] = tuple(cur)

        fwdpath = {}
        cell = (h-1, w-1)
        while cell != (0, 0):
            fwdpath[dfspath[cell]] = cell
            cell = dfspath[cell]
        self._signal.emit([h-1, w-1, True, fwdpath])

    def BFS(self):
        di = [0, -1, 0, 1]
        dj = [-1, 0, 1, 0]
        h, w = len(self.maze), len(self.maze)
        dist = [[1e9 for i in range(w)] for j in range(h)]
        stack = []
        bfspath = {}
        stack = []
        stack.append([0, 0])
        dist[0][0] = 0
        while len(stack) > 0:
            cur = stack.pop(0)
            self._signal.emit([cur[0], cur[1], False, {}])
            if(cur == [h-1, w-1]):
                break
            time.sleep(0.1)
            for i in range(4):
                next = [cur[0]+di[i], cur[1]+dj[i]]
                if(0 <= next[0] < h and 0 <= next[1] < w and self.maze[next[0]][next[1]] != 0 and dist[next[0]][next[1]] == 1e9):
                    dist[next[0]][next[1]] = dist[cur[0]][cur[0]] + 1
                    stack.append([next[0], next[1]])
                    bfspath[(cur[0]+di[i], cur[1]+dj[i])] = tuple(cur)

        fwdpath = {}
        cell = (h-1, w-1)
        while cell != (0, 0):
            fwdpath[bfspath[cell]] = cell
            cell = bfspath[cell]
        self._signal.emit([h-1, w-1, True, fwdpath])
