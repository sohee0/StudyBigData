import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

#클래스 OOP
class qTemplates(QWidget):
    
    # 생성자
    def __init__(self) -> None:   # self는 그냥파라미터 아님. 특수파라미터 , (none)생성자는 리턴값이 없다.
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300,100,640,400)
        self.setWindowTitle('QPushBotton 예제')
        self.show()
    
    def addControls(self) -> None:
        self.label = QLabel('메시지: ',self)
        self.label.setGeometry(10,10,600,40)
        self.btn1 = QPushButton('Click',self)     #self.btn1도 가능
        self.btn1.setGeometry(510,350,120,40)
        self.btn1.clicked.connect(self.btn1_clicked)  #signal connect
        


        # event = signal (python)
    def btn1_clicked(self):
        self.label.setText('메시지 : 비온다')
        # QMessageBox.information(self,'signal','btn1_clicked') #d일반정보
        # QMessageBox.warning(self,'signal','btn1_clicked')     #경고
        QMessageBox.critical(self,'signal','btn1_clicked')      #에러

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplates()
    app.exec_()