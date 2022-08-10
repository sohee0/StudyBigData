import sys
from this import d
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt


#클래스 OOP
class qTemplates(QWidget):
    
    # 생성자
    def __init__(self) -> None:   # self는 그냥파라미터 아님. 특수파라미터 , (none)생성자는 리턴값이 없다.
        super().__init__()
        self.initUI()

    # 화면정의를 위한 사용자 함수(이름변경가능)
    def initUI(self) -> None:
        self.setGeometry(300,100,640,400)
        self.setWindowTitle('QTemplates')
        self.text = 'HELLO SUMMER !'
        self.show()
    
    # 기본적으로 Qwidget 함수
    def paintEvent(self,event) -> None:
        paint = QPainter()
        paint.begin(self)
        #그리는 함수 추가(drawText는 내장함수)
        self.drawText(event,paint)
        paint.end()

    # 텍스트 그리기 위한 사용자함수
    def drawText(self,event,paint):
        paint.setPen(QColor(50,50,50))
        paint.setFont(QFont('Impact',20))
        paint.drawText(105,100,'HI')
        paint.setPen(QColor(10,10,10))
        paint.setFont(QFont('NanumSquareRoundR',20))
        paint.drawText(event.rect(),Qt.AlignCenter,self.text)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplates()
    app.exec_()