import time
from Service.Maze import Maze
from Service.SolveMaze import SolveMaze
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QComboBox, QLabel, QGridLayout)


class MazeUI(QWidget):

    def __init__(self):
        super().__init__()
        self.maze = []
        self.mazeSize = 20
        self.solveType = "DFS"
        self.width = 1200
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Maze')
        self.setGeometry(50, 50, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        # self.setLayout(self.layout)

        # 建立mazeSizeComboBox Label
        self.mazeSizeComboBoxLabel = QLabel(self)
        self.mazeSizeComboBoxLabel.setText("請選擇地圖大小：")
        self.mazeSizeComboBoxLabel.resize(200, 30)
        self.mazeSizeComboBoxLabel.move(810, 10)

        # 建立下拉式選單
        self.mazeSizeComboBox = QComboBox(self)
        self.mazeSizeComboBox.addItems(
            ["{:02d}".format(x) for x in range(2, 21)])
        self.mazeSizeComboBox.resize(200, 30)
        self.mazeSizeComboBox.move(810, 40)
        self.mazeSizeComboBox.setCurrentIndex(18)
        self.mazeSizeComboBox.currentIndexChanged.connect(
            self.change_maze_size)

        # 建立刷新按鈕
        self.refreshBtn = QPushButton("刷新", self)
        self.refreshBtn.resize(90, 30)
        self.refreshBtn.move(1030, 40)
        self.refreshBtn.clicked.connect(self.create_maze)

        # 建立solveMazeComboBox Label
        self.solveMazeComboBoxLabel = QLabel(self)
        self.solveMazeComboBoxLabel.setText("請選擇解迷宮方法：")
        self.solveMazeComboBoxLabel.resize(200, 30)
        self.solveMazeComboBoxLabel.move(810, 100)

        # 建立解迷宮方法下拉選單
        self.solveMazeComboBox = QComboBox(self)
        self.solveMazeComboBox.addItems(["DFS", "BFS"])
        self.solveMazeComboBox.resize(200, 30)
        self.solveMazeComboBox.move(810, 130)
        self.solveMazeComboBox.currentIndexChanged.connect(
            self.change_solve_type)

        # 建立解迷宮按鈕
        self.solveMazeBtn = QPushButton("解迷宮", self)
        self.solveMazeBtn.resize(90, 30)
        self.solveMazeBtn.move(1030, 130)
        self.solveMazeBtn.clicked.connect(self.solve_maze)

        # 預設產生 20 * 20 地圖
        self.create_maze()

    def change_solve_type(self):
        self.solveType = self.solveMazeComboBox.currentText()

    def change_maze_size(self):
        # print(self.mazeSizeComboBox.currentText())
        self.mazeSize = int(self.mazeSizeComboBox.currentText())

    def create_maze(self):
        self.remove_maze()
        self.maze = [
            [None for _ in range(0, self.mazeSize)]
            for _ in range(0, self.mazeSize)
        ]
        maze = Maze(self.mazeSize)
        for x, i in enumerate(maze.random()):
            for y, j in enumerate(i):
                if(j == 1):
                    self.create_maze_btn(x, y, "GRASS")
                else:
                    self.create_maze_btn(x, y, "WALL")

    def create_maze_btn(self, x, y, type):
        boxSize = self.height // self.mazeSize
        self.maze[x][y] = QPushButton('', self)
        self.maze[x][y].resize(boxSize, boxSize)
        self.maze[x][y].move(x * boxSize, y * boxSize)
        style = "border: none;border-radius: 0px;"
        if(type == "WALL"):
            style += "border-image: url('./Images/wall.jpg');"
        elif(type == "GRASS"):
            style += "border-image: url('./Images/ground.jpg');"

        self.maze[x][y].setStyleSheet(style)
        self.maze[x][y].show()

    def remove_maze(self):
        for i in self.maze:
            for j in i:
                j.deleteLater()
        self.maze = None

    def solve_maze(self):
        self.refreshBtn.setDisabled(True)
        self.solveMazeBtn.setDisabled(True)
        self.thread = SolveMaze(self.maze)
        self.thread._signal.connect(self.solve_maze_callback)
        self.thread.finished.connect(self.solve_maze_finished)
        self.thread.start()

    def solve_maze_callback(self, coordinate):
        x, y = coordinate
        style = "border: none;border-radius: 0px;border-image: url('./Images/mouse.png');background-color: green;"
        self.maze[x][y].setStyleSheet(style)

    def solve_maze_finished(self):
        self.refreshBtn.setDisabled(False)
        self.solveMazeBtn.setDisabled(False)
