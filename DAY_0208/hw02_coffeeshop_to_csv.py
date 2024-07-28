from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

html = urlopen('http://www.hollys.co.kr')
bs = BeautifulSoup(html.read(), 'html.parser')

url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=1&sido=&gugun=&store='

html = urlopen(url)
bs = BeautifulSoup(html.read(), 'html.parser')

def setpageurl(start_page, last_page):
    url_list = []
    try:
        for page_number in range(start_page, last_page + 1):
            url = f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page_number}&sido=&gugun=&store='.format(
                page_number)
            url_list.append(url)
    except Exception as e:
        print('페이지를 잘못 입력하였습니다.')
    return url_list


setpageurl(1, 51)


def cafeshopinfo():
    i = 1
    hollys_dict = {'매장이름': [], '위치(시,구)': [], '주소': [], '전화번호': []}
    for page_url in setpageurl(1, 51):
        html = urlopen(page_url)
        bs = BeautifulSoup(html.read(), 'html.parser')
        for ind in range(int(len(bs.select('tbody td')) / 6)):

            try:
                store_name = bs.select('tbody td')[1 + 6 * ind].string
            except Exception as e:
                print(e)
                store_name = None

            hollys_dict['매장이름'].append(store_name)

            try:
                location = bs.select('tbody td')[0 + 6 * ind].string
            except Exception as e:
                print(e)
                location = None

            hollys_dict['위치(시,구)'].append(location)

            try:
                address = bs.select('tbody td')[3 + 6 * ind].string
            except Exception as e:
                print(e)
                address = None

            hollys_dict['주소'].append(address)

            try:
                phone_number = bs.select('tbody td')[5 + 6 * ind].string
            except Exception as e:
                print(e)
                phone_number = None

            hollys_dict['전화번호'].append(phone_number)

            print(
                f"[{i:3d}] 매장 이름 : {bs.select('tbody td')[0 + 6 * ind].string}, 지역 : {bs.select('tbody td')[1 + 6 * ind].string}, 주소 : {bs.select('tbody td')[3 + 6 * ind].string}, 전화번호 : {bs.select('tbody td')[5 + 6 * ind].string}")
            i += 1

    hollysDF = pd.DataFrame(hollys_dict)
    hollysDF.to_csv('../DATA/hollys_branches.csv', index=False, encoding='utf-8-sig')
    print(f'전체 매장 수 : {i - 1}')
    print('hollys_branches.csv 파일 저장 완료')

cafeshopinfo()