import imp
from select import select
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time

# UI스레드와 작업스레드 분리
class Worker(QThread):
    #Q스레드는 화면을 그릴 권한이 없음. 
    # 대신 통신을 통해 UI스레드가그림을 그릴 수 있도록 통신수행
    valChangeSignal = pyqtSignal(int) 
    


    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.working = True      # 클래스 내부변수 워킹을 지정

    def run(self) -> None:
        while self.working:
            for i in range(0,1000000):                 
                print(f'출력 : {i}')
                # self.pgbTask.setValue(i)
                # self.txbLog.append(f'출력 > {i}')
                self.valChangeSignal.emit(i)  #ui스레드 화면 그려줭
                time.sleep(0.0001) #1micro second



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
        self.worker.start()
        self.worker.working = True


    
    def addControls(self) -> None:
        self.btnStart.clicked.connect(self.btn1_clicked)
        # worker 클래스 생성
        self.worker = Worker(self)
        self.worker.valChangeSignal.connect(self.updateProgress)

    @pyqtSlot(int)
    def updateProgress(self,val):   #val이 worker스레드에서 전달받은 반복값
        self.pgbTask.setValue(val)
        self.txbLog.append(f'출력 > {val}')
        if val == 999999:
            self.worker.working = False
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplates()
    app.exec_()