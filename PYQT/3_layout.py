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
        lable_4 = QLabel("Hello bro",self)
        lable_5 = QLabel("Hi Hello",self)

        lable_1.setStyleSheet("background-color: red;")
        lable_2.setStyleSheet("background-color: yellow;")
        lable_3.setStyleSheet("background-color: green;")
        lable_4.setStyleSheet("background-color: lightpink;")
        lable_5.setStyleSheet("background-color: lightblue;")
        # Now all the lables are overlaping layer by layer
        # lable_1 > lable_2 > than finaly lable_3
        # so right now we can only see lable_3 for overlap



# now all the labels are still technically children of the main window
# but we are going to add them to a layout to stack them vertically
        vbox = QVBoxLayout()   # creating a vertical layout
        # vbox = QHBoxLayout() # creating a horizontal layout
        vbox.addWidget(lable_1)
        vbox.addWidget(lable_2)
        vbox.addWidget(lable_3)
        

        grid = QGridLayout()

        grid.addWidget(lable_4, 0,0)
        grid.addWidget(lable_5, 0,1)

        # now combining both layouts inside a main vertical layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(vbox)   # adding the vertical layout
        main_layout.addLayout(grid)   # adding the grid layout
        # setting the combined layout to the central widget
        central_widget.setLayout(main_layout)

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()