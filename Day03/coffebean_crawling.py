#selenium 사용 페이지 크롤링

from bs4 import BeautifulSoup
import pandas as pd 
import time
from selenium import webdriver

#크롬웹드라이버 객체 생성
def getCoffeBeanStoreInfo(result):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    wd = webdriver.Chrome('./day03/chromedriver.exe', options=options)  #경로조심!!
    
    for i in range(1,21):
        wd.get('https://www.coffeebeankorea.com/store/store.asp')
        time.sleep(1)

        try:
            wd.execute_script(f"storePop2('{i}')")
            
            time.sleep(0.5)                       #팝업표시후 크롤링이 되기전 브라우저가 닫히는 것을 방지
            html = wd.page_source
            soup =BeautifulSoup(html,'html.parser')
            store_name = soup.select('div.store_txt > h2')[0].string
            print(store_name)
            store_info = soup.select('table.store_table >tbody>tr>td')
            store_address_list = list(store_info[2])
            store_address =store_address_list[0].strip()
            store_contact = store_info[3].string
            result.append([store_name]+[store_address]+[store_contact])
        except Exception as e:
            print(e)
            continue

def main():
    result = []
    print('커피빈매장크롤링>>> ')
    getCoffeBeanStoreInfo(result)

    #판다스 df 생성
    columns= ['store','address','phone']
    coffeebean_df = pd.DataFrame(result,columns=columns)

    #csv저장
    coffeebean_df.to_csv('./coffeebean_shop_info.csv',index=True,encoding='utf8')
    print('저장완료')

    del result[:]

if __name__ == '__main__':
    main()

