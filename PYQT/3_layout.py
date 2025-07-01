import sys
from PyQt5.QtWidgets import (QApplication ,QMainWindow, QLabel,
                             QWidget, QVBoxLayout ,QHBoxLayout , QBoxLayout, QGridLayout)
from PyQt5.QtGui import QFont
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,400,600,600)
        self.setWindowTitle("Layout")
        lable_1 = QLabel("Hi bro",self)
        lable_1.setFont(QFont("Arial", 16))
        lable_1.setGeometry(10,10,100,30)

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()