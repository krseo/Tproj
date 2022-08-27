import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from kiwoom import Kiwoom, logger

# UI파일 연결 코드
UI_class = uic.loadUiType("MainWin.ui")[0]


class MyWindow(QMainWindow, UI_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        hts = Kiwoom()
        if hts.kiwoom_GetConnectState() == 0:
            logger.debug('로그인 시도')
            res = hts.kiwoom_CommConnect()
            logger.debug('로그인 결과: {}'.format(res))
            if res.get('result') != 0:
                print("Login failed")
                sys.exit()

        ##res = hts.kiwoom_CommConnect()
        res = hts.kiwoom_GetAccList()
        print(res)
        res = hts.GetFutureList()
        print(res)
        res = hts.GetMonthList()
        print(res)

        hts.SetRealReg("1111","209AK220","10;20","0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
