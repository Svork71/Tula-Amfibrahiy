import random
import PyQt5
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication

class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        d = random.randint(10, 100)
        qp.setBrush(QColor(255, 0, 0))
        qp.drawEllipse(d, d, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

