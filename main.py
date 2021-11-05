import sys
import random

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Click me"))


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = 0
        self.y = 0
        self.pushButton.clicked.connect(self.random_circles)

    def random_circles(self):
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent) -> None:
        shape = QtGui.QPainter()
        for i in range(random.randint(1, 4)):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.x = random.randint(2, self.width())
            self.y = random.randint(2, self.height())
            size = random.randint(2, self.width() // 3)
            shape.begin(self)
            shape.setBrush(QtGui.QColor(r, g, b))
            shape.drawEllipse(self.x - size // 2, self.y - size // 2, size, size)
            shape.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
