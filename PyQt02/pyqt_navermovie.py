from ast import keyword
import imp
from re import search
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from urllib.parse import quote
import urllib.request
import json
import webbrowser

#클래스 OOP
class qTemplates(QWidget):
    
    # 생성자
    def __init__(self) -> None:   # self는 그냥파라미터 아님. 특수파라미터 , (none)생성자는 리턴값이 없다.
        super().__init__()
        uic.loadUi('./PyQt02/navermovie.ui',self)
        self.initUI()

    def initUI(self) -> None:
        self.addControls()

        self.show()
    
    def btn1_clicked(self):
        pass

    
    def addControls(self) -> None:  #위젯정의,이벤트(시그널)처리
        self.btnSearch.clicked.connect(self.btnSearchClicked)
        self.txtSearch.returnPressed.connect(self.btnSearchClicked)  #검색하고 엔터치면 나오게
        self.tblResult.itemSelectionChanged.connect(self.tblResultSelected)

    def tblResultSelected(self) -> None:
        selected = self.tblResult.currentRow()  #선택된 열의 인덱스
        link = self.tblResult.item(selected,2).text()
        webbrowser.open(link)

    def btnSearchClicked(self) -> None: #슬롯(이벤트핸들러) 파이큐티에서만 슬롯
        jsonResult = []
        totalResult = []
        keyword ='movie'
        search_word = self.txtSearch.text()
        display_count = 100

        # QMessageBox.information(self,'결과',search_word)
        jsonResult = self.getNaverSearch(keyword,search_word,1,display_count)
        # print(jsonResult)
        for post in jsonResult['items']:
            totalResult.append(self.getPostData(post))

        # print(totalResult)
        self.makeTable(totalResult)
        return #(아무값도 안넣으면 return none이야 )

    def makeTable(self,result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection) 
        self.tblResult.setColumnCount(3)
        self.tblResult.setRowCount(len(result))  #디스플레이카운트에 따라 변경 (현재50)
        self.tblResult.setHorizontalHeaderLabels(['영화제목','상영연도','뉴스링크'])
        self.tblResult.setColumnWidth(0,250)
        self.tblResult.setColumnWidth(1,100)
        self.tblResult.setColumnWidth(2,100)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)  #readonly

        i =0
        for item in result:
            title = self.strip_tag(item[0]['title'])
            subtitle = self.strip_tag(item[0]['subtitle'])
            pubDate = item[0]['pubDate']
            link = item[0]['link']
            self.tblResult.setItem(i,0,QTableWidgetItem(f'{title}/{subtitle}'))
            self.tblResult.setItem(i,1,QTableWidgetItem(pubDate))
            self.tblResult.setItem(i,2,QTableWidgetItem(link))
            i +=1

        #html 태그 제거
    def strip_tag(self,title):
        ret = title.replace('&lt;' ,'<')
        ret = ret.replace('&gt;','>' )
        ret = ret.replace('&quot;','"' )
        ret = ret.replace('&apos;',"'" )
        ret = ret.replace('&amp;','&' )
        ret = ret.replace('<b>','' )
        ret = ret.replace('</b>','' )
        return ret

    
    def getPostData(self,post):
        temp = []
        title = post['title']
        subtitle = post['subtitle']
        link = post['link']
        pubDate = post['pubDate']

        temp.append({'title':title,
                    'subtitle':subtitle,
                    'pubDate':pubDate,
                    'link':link})

        return temp


    #네이버API 크롤링 함수
    def getNaverSearch(self,keyword,search,start,display):
        url = f'https://openapi.naver.com/v1/search/{keyword}.json'\
              f'?query={quote(search)}&start={start}&display={display}'
        print(url)

        req = urllib.request.Request(url)
        # 네이버인증추가
        req.add_header('X-Naver-Client-Id','aNqzpW12RSOjmhxbxgVV')
        req.add_header('X-Naver-Client-Secret','tZs99j7b5e')

        res = urllib.request.urlopen(req)
        if res.getcode()==200:
            print('URL request succeed')
        else:
            print('URL request failed')

        ret= res.read().decode('utf-8')
        if ret == None:
            return None
        else:
            return json.loads(ret)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = qTemplates()
    app.exec_()