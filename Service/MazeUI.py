import time
from Service.Maze import Maze
from PyQt5.QtWidgets import (
    QWidget, QPushButton, QComboBox, QLabel, QGridLayout)


class MazeUI(QWidget):

    def __init__(self):
        super().__init__()
        self.maze = []
        self.mazeSize = 20
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

        # 預設產生 20 * 20 地圖
        self.create_maze()

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
