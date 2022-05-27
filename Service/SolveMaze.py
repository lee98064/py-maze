import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread, pyqtSignal


class SolveMaze(QtCore.QThread):

    _signal = pyqtSignal(list)

    def __init__(self, maze) -> None:
        super(SolveMaze, self).__init__()
        self.maze = maze

    def __del__(self):
        self.wait()

    def run(self):
        for x, i in enumerate(self.maze):
            for y, j in enumerate(self.maze):
                self._signal.emit([x, y])
                time.sleep(0.1)
