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

        """
        상장일 = kiwoom.GetMasterListedSTockDate("005690")
        print(상장일)
        print(type(상장일))        # datetime.datetime 


        전일가 = hts.GetMasterLastPrice("005930")
        print(int(전일가))
        print(type(전일가))
        """

        df = hts.block_request("opt10001",
                                  종목코드="005930",
                                  output="주식기본정보",
                                  next=0)
        print(df)

        df = hts.block_request("opt10081",
                                  종목코드="005930",
                                  기준일자="20200424",
                                  수정주가구분=1,
                                  output="주식일봉차트",
                                  next=0)
        print(df.head())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
