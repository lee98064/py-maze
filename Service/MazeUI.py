from Service.Maze import Maze
from Service.SolveMaze import SolveMaze
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QComboBox, QLabel, QGridLayout)


class MazeUI(QWidget):

    def __init__(self):
        super().__init__()
        self.maze = []
        self.mazeBtn = []
        self.mazeSize = 20
        self.solveType = "DFS"
        self.last_x = 0
        self.last_y = 0
        self.width = 1200
        self.height = 800
        self.thread = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Maze')
        self.setGeometry(50, 50, self.width, self.height)
        self.setFixedSize(self.width, self.height)

        # 建立mazeSizeComboBox Label
        self.mazeSizeComboBoxLabel = QLabel(self)
        self.mazeSizeComboBoxLabel.setText("請選擇地圖大小：")
        self.mazeSizeComboBoxLabel.resize(200, 30)
        self.mazeSizeComboBoxLabel.move(810, 10)

        # 建立下拉式選單
        self.mazeSizeComboBox = QComboBox(self)
        self.mazeSizeComboBox.addItems(
            ["{:02d}".format(x) for x in range(2, 41)])
        self.mazeSizeComboBox.resize(200, 30)
        self.mazeSizeComboBox.move(810, 40)
        self.mazeSizeComboBox.setCurrentIndex(18)
        self.mazeSizeComboBox.currentIndexChanged.connect(
            self.change_maze_size)

        # 建立刷新按鈕
        self.refreshBtn = QPushButton("刷新", self)
        self.refreshBtn.resize(90, 30)
        self.refreshBtn.move(1030, 40)
        self.refreshBtn.clicked.connect(self.create_new_maze)

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

        # 建立清空地圖按鈕
        self.cleanMazeBtn = QPushButton("清空迷宮", self)
        self.cleanMazeBtn.resize(90, 30)
        self.cleanMazeBtn.move(1030, 180)
        self.cleanMazeBtn.clicked.connect(self.clean_maze)

        # 預設產生 20 * 20 地圖
        self.create_new_maze()

    def change_solve_type(self):
        self.solveType = self.solveMazeComboBox.currentText()

    def change_maze_size(self):
        # print(self.mazeSizeComboBox.currentText())
        self.mazeSize = int(self.mazeSizeComboBox.currentText())

    def create_new_maze(self):
        maze = Maze(self.mazeSize)
        self.maze = maze.random()
        self.create_maze()

    def create_maze(self):
        self.remove_maze()
        self.mazeBtn = [
            [None for _ in range(0, self.mazeSize)]
            for _ in range(0, self.mazeSize)
        ]
        for x, i in enumerate(self.maze):
            for y, j in enumerate(i):
                if(j == 1):
                    self.maze_btn(x, y, "GRASS")
                else:
                    self.maze_btn(x, y, "WALL")

    def maze_btn(self, x, y, type):
        boxSize = self.height // self.mazeSize
        self.mazeBtn[x][y] = QPushButton('', self)
        self.mazeBtn[x][y].resize(boxSize, boxSize)
        self.mazeBtn[x][y].move(x * boxSize, y * boxSize)
        style = "border: none;border-radius: 0px;"
        if(x == 0 and y == 0):
            style += "border-image: url('./Images/mouse_ground.png');"
        elif (x == self.mazeSize - 1 and y == self.mazeSize - 1):
            style += "border-image: url('./Images/end.png');"
        elif(type == "WALL"):
            style += "border-image: url('./Images/wall.jpg');"
        elif(type == "GRASS"):
            style += "border-image: url('./Images/ground.jpg');"

        self.mazeBtn[x][y].setStyleSheet(style)
        self.mazeBtn[x][y].show()

    def remove_maze(self):
        for i in self.mazeBtn:
            for j in i:
                j.deleteLater()
        self.mazeBtn = []

    def clean_maze(self):
        self.remove_maze()
        self.create_maze()

    def solve_maze(self):
        self.last_x, self.last_y = 0, 0
        self.refreshBtn.setDisabled(True)
        self.solveMazeBtn.setDisabled(True)
        self.cleanMazeBtn.setDisabled(True)
        self.thread = SolveMaze(self.maze, self.solveType)
        self.thread._signal.connect(self.solve_maze_callback)
        self.thread.finished.connect(self.solve_maze_finished)
        self.thread.start()

    def solve_maze_callback(self, coordinate):
        x, y, isEnd, route = coordinate

        style = "border: none;border-radius: 0px;"

        self.mazeBtn[self.last_x][self.last_y].setStyleSheet(
            style + "border-image: url('./Images/past.png');")

        self.mazeBtn[x][y].setStyleSheet(
            style + "border-image: url('./Images/mouse_ground.png');")

        self.last_x, self.last_y = x, y

        if(isEnd):
            for rx, ry in route:
                self.mazeBtn[rx][ry].setStyleSheet(
                    style + "border-image: url('./Images/route.png');")

    def solve_maze_finished(self):
        self.refreshBtn.setDisabled(False)
        self.solveMazeBtn.setDisabled(False)
        self.cleanMazeBtn.setDisabled(False)
        self.thread = None
