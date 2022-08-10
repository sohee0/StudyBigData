import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


#클래스 OOP
class qTemplates(QWidget):
    
    # 생성자
    def __init__(self) -> None:   # self는 그냥파라미터 아님. 특수파라미터 , (none)생성자는 리턴값이 없다.
        super().__init__()
        self.initUI()

    # 화면정의를 위한 사용자 함수(이름변경가능)
    def initUI(self) -> None:
        self.addControls()
        self.setGeometry(300,100,640,400)
        self.setWindowTitle('QLabel')
        self.show()

    def addControls(self) -> None:
        self.setWindowIcon(QIcon('./PyQt01/image/lion.png'))  # 윈도우 아이콘 지정
        label1 = QLabel(self)
        label2 = QLabel(self)
        label1.setStyleSheet(
             'border-width: 3px;'
             'border-style: solid;'
             'border-color: blue;'
             'image: url(./PyQt01/image/image1.png)'  
        )

        label2.setStyleSheet(
             'border-width: 3px;'
             'border-style: dot-dot-dash;'
             'border-color: red;'
             'image: url(./PyQt01/image/image2.png)'  
        )
        box = QHBoxLayout()
        box.addWidget(label1)
        box.addWidget(label2)

        self.setLayout(box)

               
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplates()
    app.exec_()