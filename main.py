import sys
import random

from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.random_circles)

    def random_circles(self):
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        shape = QtGui.QPainter()
        for i in range(random.randint(1, 4)):
            self.x = random.randint(2, self.width())
            self.y = random.randint(2, self.height())
            size = random.randint(2, self.width() // 3)
            shape.begin(self)
            shape.setBrush(QtGui.QColor(255, 255, 0))
            shape.drawEllipse(self.x - size // 2, self.y - size // 2, size, size)
            shape.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
