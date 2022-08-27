import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import kiwoom

# UI파일 연결 코드
UI_class = uic.loadUiType("MainWin.ui")[0]


class MyWindow(QMainWindow, UI_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        hts = kiwoom.Kiwoom()
        hts.CommConnect(block=True)

        res = hts.GetFutureList()
        print(res)

        res = hts.GetMonthList()
        print(res)

        hts.SetRealReg("1111", "", "20;214;215", "0")
        hts.SetRealReg("1111", "209AK220", "10;20", "1")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
