import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import kiwoom
#UI파일 연결 코드
UI_class = uic.loadUiType("MainWin.ui")[0]
class MyWindow(QMainWindow, UI_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        hts = kiwoom.Kiwoom()
        hts.CommConnect(block=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()