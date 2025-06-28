# Gui means - Graphical User Interface
import sys
# sys --> System-level functions (like exiting the app)

from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel
# QApplication ---> Initializes the app and run the event loop

# QMainWindow ---> Is a Main application window class 
# It provides a framework with predefined areas like : menu bar, toolbars, status bar etc 

from PyQt5.QtGui import QIcon



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # QMainWindow is also a class so it gonna take arguments from that class
        self.setWindowTitle("First Py Window") # tile tag

        # self.setGeometry(x,y,width,height)
        self.setGeometry(500,400,500,500) # where the table will append and width and hight of the tab
        lable = QLabel("Hello World",self) # text lable
        
        
        icon = QIcon("pic.jpg")
        self.setWindowIcon(icon)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


#   sys.exit(app.exec_()) --> Starts the event loop (keeps the app running).
#           The app stays open until you close the window.
#           sys.exit() ensures a clean and safe exit when the app closes.

if __name__ == "__main__":
    main()