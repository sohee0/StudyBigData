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
        uic.loadUi('./PyQt02/basic01.ui',self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()

        self.show()
    
    def btn1_clicked(self):
        self.label.setText('메시지 : 비온다')
        QMessageBox.information(self,'signal','btn1_clicked') #일반정보


    
    def addControls(self) -> None:
        self.btn1.clicked.connect(self.btn1_clicked)
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplates()
    app.exec_()