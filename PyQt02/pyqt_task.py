import imp
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#클래스 OOP
class qTemplates(QWidget):
    
    # 생성자
    def __init__(self) -> None:   # self는 그냥파라미터 아님. 특수파라미터 , (none)생성자는 리턴값이 없다.
        super().__init__()
        uic.loadUi('./PyQt02/ttask.ui',self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()

        self.show()
    
    def btn1_clicked(self):
        self.txbLog.append('실행')
        self.pgbTask.setRange(0,999999)
        for i in range(0,1000000):                  # 1000000 으로 하면 응답없음발생
            print(f'출력 : {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'출력 > {i}')

    
    def addControls(self) -> None:
        self.btnStart.clicked.connect(self.btn1_clicked)
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplates()
    app.exec_()