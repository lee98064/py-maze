import sys
from PyQt5.QtWidgets import (QApplication)
from Service.MazeUI import MazeUI
from qt_material import apply_stylesheet

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # 設定樣式
    apply_stylesheet(app, theme='light_pink.xml')
    w = MazeUI()
    w.show()
    # w.remove_maze()
    sys.exit(app.exec_())
