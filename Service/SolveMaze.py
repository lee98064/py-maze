import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal


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
            return

        if(self.solveType == "DFS"):
            self.DFS()
            return

    def DFS(self):
        di = [0, -1, 0, 1]
        dj = [-1, 0, 1, 0]
        h, w = len(self.maze), len(self.maze)
        dist = [[1e9 for i in range(w)] for j in range(h)]
        for i in range(h):
            stack = []
            stack.append([0, 0])
            dist[0][0] = 0
            while len(stack) > 0:
                cur = stack.pop()
                self._signal.emit([cur[0], cur[1]])
                if(cur == [h-1, w-1]):
                    break
                time.sleep(0.1)
                for i in range(4):
                    next = [cur[0]+di[i], cur[1]+dj[i]]
                    if(0 <= next[0] < h and 0 <= next[1] < w and self.maze[next[0]][next[1]] != 0 and dist[next[0]][next[1]] == 1e9):
                        dist[next[0]][next[1]] = dist[cur[0]][cur[0]] + 1
                        stack.append([next[0], next[1]])
            if(cur == [h-1, w-1]):
                break
        self._signal.emit([h-1, w-1])

    def BFS(self):
        di = [1, 0, -1, 0]
        dj = [0, 1, 0, -1]
        h, w = len(self.maze), len(self.maze)
        dist = [[1e9 for i in range(w)] for j in range(h)]
        for i in range(h):
            stack = []
            stack.append([0, 0])
            dist[0][0] = 0
            while len(stack) > 0:
                cur = stack.pop(0)
                if(cur == [h-1, w-1]):
                    break
                time.sleep(0.1)
                for i in range(4):
                    next = [cur[0]+di[i], cur[1]+dj[i]]
                    if(0 <= next[0] < h and 0 <= next[1] < w and self.maze[next[0]][next[1]] != 0 and dist[next[0]][next[1]] == 1e9):
                        dist[next[0]][next[1]] = dist[cur[0]][cur[0]] + 1
                        self._signal.emit([cur[0], cur[1]])
                        stack.append([next[0], next[1]])

        self._signal.emit([h-1, w-1])
