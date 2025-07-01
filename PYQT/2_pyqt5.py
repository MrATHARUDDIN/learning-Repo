import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage

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
        url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PyQt_logo.svg/320px-PyQt_logo.svg.png"
        label2 = QLabel(self)
        label2.setGeometry(10, 300, 250, 250)

        # to put the img in center
        label2.setGeometry(self.width()- label2.width() // 2,
                           self.height() - label2.height() // 2,
                           )

        try:
            response = requests.get(url)
            image = QImage.fromData(response.content)
            pixmap = QPixmap.fromImage(image)

            if pixmap.isNull():
                label2.setText("Failed to load image!")
            else:
                label2.setPixmap(pixmap)
                label2.setScaledContents(True)
        except:
            label2.setText("Network error!")


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
