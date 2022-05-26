from Service.Maze import Maze
from PyQt5.QtWidgets import (QWidget, QPushButton, QComboBox)


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

        # 建立刷新按鈕
        self.refreshBtn = QPushButton("刷新", self)
        self.refreshBtn.move(900, 10)
        self.refreshBtn.clicked.connect(self.create_maze)

        # 預設產生 20 * 20 地圖
        self.create_maze()
        # self.MazeSize = QComboBox(self)
        # self.MazeSize.addItems(["{:02d}".format(x) for x in range(1, 21)])
        # self.MazeSize.resize(90, 50)
        # self.MazeSize.move(450, 450)

    def create_maze(self):
        self.remove_maze()
        maze = Maze(self.mazeSize)
        maze.random()
        boxSize = int(self.height / self.mazeSize)
        for iIndex, i in enumerate(maze.random()):
            for jIndex, j in enumerate(i):
                if(j == 1):
                    self.create_maze_btn(iIndex * boxSize, jIndex *
                                         boxSize, boxSize, False)
                else:
                    self.create_maze_btn(iIndex * boxSize, jIndex *
                                         boxSize, boxSize, True)

    def create_maze_btn(self, x, y, boxSize, is_wall):
        button = QPushButton('', self)
        button.resize(boxSize, boxSize)
        button.move(x, y)
        if(is_wall):
            button.setStyleSheet(
                "border-image: url('./Images/wall.jpg');border: none;border-radius: 0px")
        else:
            button.setStyleSheet(
                "border: none;border-radius: 0px;border-image: url('./Images/ground.jpg');")
        button.show()
        self.maze.append(button)

    def remove_maze(self):
        for i in self.maze:
            i.deleteLater()
        self.maze = []
