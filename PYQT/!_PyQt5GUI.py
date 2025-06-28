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


def main():
    pass