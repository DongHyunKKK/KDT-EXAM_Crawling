from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

def main():
    file = '../DATA/hollys_branches.csv'
    while True:
        city_gu = input('검색할 매장의 도시를 입력하세요 : ')
        if city_gu == 'quit':
            print('종료 합니다.')
            break
        elif len(city_gu.split()) != 2:
            print('다시 입력하세요.')
        elif len(city_gu.split()) == 2:
            if not city_gu.split()[0].isalpha() or not city_gu.split()[1].isalpha():
                print('다시 입력하세요.')
            else:
                f = open(file, 'r', encoding = 'utf-8')
                data = csv.reader(f, delimiter = ',')  # delimiter : 구분자(','), csv파일은 delimiter 생략 가능
                p = re.compile(city_gu.split()[0] + '.*' + ' ' +city_gu.split()[1])  # 예를 들어 서구, 달서구 구분하기 위해서 중간에 ' ' 추가
                address_list = []
                for row in data:
                    if p.match(row[2]):
                        address_list.append(row[2:])
                print('-' * 20)
                print(f'검색된 매장 수 : {len(address_list)}')
                print('-' * 20)
                i = 1
                for address in address_list:
                    print(f'[{i:3d}] : {address}')
                    i += 1
                print('-' * 100)
                f.close()

main()