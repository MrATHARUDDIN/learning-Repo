import sys
from PyQt5.QtWidgets import (QApplication ,QMainWindow, QLabel,
                             QWidget, QVBoxLayout ,QHBoxLayout , QBoxLayout, QGridLayout)
from PyQt5.QtGui import QFont

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,400,600,600)
        
        self.intUI()

    # this function is for the layout because we can't use layout in our mainClass  
    def intUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setWindowTitle("Layout")

        lable_1 = QLabel("Hi bro",self)
        lable_2 = QLabel("Hi Athar",self)
        lable_3 = QLabel("Hi MC",self)

        lable_1.setStyleSheet("background-color: red;")
        lable_2.setStyleSheet("background-color: yellow;")
        lable_3.setStyleSheet("background-color: green;")
        # Now all the lables are overlaping layer by layer
        # lable_1 > lable_2 > than finaly lable_3
        # so right now we can only see lable_3 for overlap



# now all the labels are still technically children of the main window
# but we are going to add them to a layout to stack them vertically
        vbox = QVBoxLayout() # creating a vertical layout
        # vbox = QHBoxLayout() # creating a horizontal layout
        vbox.addWidget(lable_1)
        vbox.addWidget(lable_2)
        vbox.addWidget(lable_3)

        central_widget.setLayout(vbox)

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()