import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

Text = "Hello again!"
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 500, 500)

        # Text label
        self.label = QLabel("hello", self)
        self.label.setFont(QFont("Arial", 20))
        self.label.setGeometry(10, 10, 270, 100)
        self.label.setStyleSheet(
            "color: #292929;"
            "background-color: #6fdcf7;"
            "font-weight: bold;"
            "font-style: italic;"
        )
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        # Image label
        label2 = QLabel(self)
        label2.setGeometry(10, 300, 100, 100)
        pixmap = QPixmap("icon.ico")
        label2.setPixmap(pixmap)
        label2.setScaledContents(True)

        # Button
        btn = QPushButton("Check Out Girls", self)
        btn.setCheckable(True)
        btn.setGeometry(50, 150, 150, 40)
        btn.clicked.connect(self.after_click)

    def after_click(self):
        global Text
        self.label.setText(Text)
        print("Btn has been clicked")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
