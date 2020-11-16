import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QImage
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.flag = False
        self.initUI()

    def initUI(self):
        self.image = QImage(self.width(), self.height(), QImage.Format_ARGB32)
        self.image.fill(QColor(255, 255, 255))
        self.btn.clicked.connect(self.click)
        self.show()

    def click(self):
        self.paint = QPainter(self.image)
        self.ellips()

    def paintEvent(self, e):
        paint = QPainter(self)
        paint.drawImage(0, 0, self.image)

    def ellips(self):
        x, y = [randint(10, 400) for i in range(2)]
        w = randint(10, 100)
        paint = QPainter(self)
        paint.drawImage(0, 0, self.image)
        self.paint.setBrush(QColor('yellow'))
        self.paint.drawEllipse(x, y, w, w)
        self.update()


app = QApplication(sys.argv)
w = Example()
sys.exit(app.exec_())
