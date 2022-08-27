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

        #res = hts.kiwoom_CommConnect()
        acct = hts.kiwoom_GetAccList()
        print(acct)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
