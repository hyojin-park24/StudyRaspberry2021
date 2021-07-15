## QT5 베이스 프레임 소스
import sys
from PyQt5.QtWidgets import * 

# 윈도우 클래스 선언
class MyWindow(QMainWindow):
    def __init__(self):     #self : 스스로 초기화
        super().__init__()

app = QApplication(sys.argv)

#button = QPushButton("Click me")
#button.show()
#label = QLabel("Hello QT5!!")
#label.show()

win = MyWindow()
win.show()

app.exec_()