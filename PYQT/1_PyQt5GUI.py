# Gui means - Graphical User Interface
import sys
# sys --> System-level functions (like exiting the app)

from PyQt5.QtWidgets import QApplication , QMainWindow
# QApplication ---> Initializes the app and run the event loop

# QMainWindow ---> Is a Main application window class 
# It provides a framework with predefined areas like : menu bar, toolbars, status bar etc 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First Py Window")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


#   sys.exit(app.exec_()) --> Starts the event loop (keeps the app running).
#           The app stays open until you close the window.
#           sys.exit() ensures a clean and safe exit when the app closes.

main()