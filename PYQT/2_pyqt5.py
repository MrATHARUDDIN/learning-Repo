import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QPushButton
from PyQt5.QtGui import QFont, QPixmap 
from PyQt5.QtCore import Qt

# QPixmap --> For the picture

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 500, 500)

        label = QLabel("hello", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(10, 10, 200, 100)
        label.setStyleSheet(
            "color: #292929;"
            "background-color: #6fdcf7;"
            "font-weight: bold;"
            "font-style: italic;"
        )

        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


        label2 =  QLabel(self)
        label.setGeometry(0,0,500,100)

        btn = QPushButton("Check Out Girls",self) # QPushButton is the module of defining a btn
        btn.setCheckable(True) # set that as a clickable btn
        btn.setGeometry(50,150,90,30) # position of the btn
        btn.clicked.connect(self.after_click) # after click call the function

    
    
    # after click funtion    
    def after_click(self):
        print("Btn has been clicked")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
