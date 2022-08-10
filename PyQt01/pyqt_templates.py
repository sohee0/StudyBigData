import sys
from PyQt5.QtWidgets import QApplication,QWidget

#클래스 OOP
class qTemplates(QWidget):
    
    # 생성자
    def __init__(self) -> None:   # self는 그냥파라미터 아님. 특수파라미터 , (none)생성자는 리턴값이 없다.
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.setGeometry(300,100,640,400)
        self.setWindowTitle('QTemplates')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplates()
    app.exec_()