import sys
from PyQt5.QtWidgets import QMainWindow , QApplication, QPushButton, QLabel


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,500,700,700)
        self.initUI()
    
    
    def initUI(self):
        self.button =QPushButton("Click me!",self)
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 18px")
        self.button.clicked.connect(self.onclick)
    
    def onclick(self):
        print("btn clicked")
        self.button.setText("Clicked")
        self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()