#할리스 매장정보 크롤링

from unittest import result
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd 
import datetime


def getHollysStoreInfo(result):
    for page in range(1,54):
        hollys_url=f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}'
        # print(hollys_url)
        html = urllib.request.urlopen(hollys_url)
        soup = BeautifulSoup(html,'html.parser')
        tbody = soup.find('tbody')

        for store in tbody.find_all('tr'):
            if len(store)<=3: break

            strore_td = store.find_all('td')

            store_name = strore_td[1].string
            store_sido = strore_td[0].string
            store_address = strore_td[3].string
            store_phone = strore_td[5].string

            result.append([store_name]+[store_sido]+[store_address]+[store_phone])

# result
print('완료')

def main():
    result = []
    print('할리스매장크롤링>>> ')
    getHollysStoreInfo(result)

    #판다스 df 생성
    columns= ['store','sido-gu','address','phone']
    hollys_df = pd.DataFrame(result,columns=columns)

    #csv저장
    hollys_df.to_csv('./hollys_shop_info.csv',index=True,encoding='utf8')
    # hollys_df.to_csv('C:/localrepository/StudyBigData/Day03/hollys_shop_info2.csv',index=True,encoding='utf8') 이렇게 하면 Day3안에 csv파일이 생긴다.
    print('저장완료')

    del result[:]

if __name__ == '__main__':
    main()

