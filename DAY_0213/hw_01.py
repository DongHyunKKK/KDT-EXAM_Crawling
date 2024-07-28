from bs4 import BeautifulSoup
import requests

top10_url = []
top10_name = []
top10_code = []

def url_name():
    url = 'https://finance.naver.com/sise/sise_market_sum.naver'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    for ind in range(1, 6):
        link = soup.select('tbody')[0].select('tr', {'id': 'onmouseover'})[ind]
        top10_url.append('https://finance.naver.com' + link.find('a', {'class': 'tltle'})['href'])
        top10_name.append(link.find('a', {'class': 'tltle'}).text)
        top10_code.append(link.find('a', {'class': 'tltle'})['href'].split('=')[1])

    for ind in range(9, 14):
        link = soup.select('tbody')[0].select('tr', {'id': 'onmouseover'})[ind]
        top10_url.append('https://finance.naver.com' + link.find('a', {'class': 'tltle'})['href'])
        top10_name.append(link.find('a', {'class': 'tltle'}).text)
        top10_code.append(link.find('a', {'class': 'tltle'})['href'].split('=')[1])

url_name()
print(top10_url)
print(top10_name)
print(top10_code)

def enterprise_info(number):
    url = top10_url[number - 1]
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    link = soup.find('div', {'class': 'rate_info'})
    rateinfo_list = link.find_all('span', {'class': 'blind'})
    print(f'종목명 : {link.strong.text}')
    print(f'종목코드 : {top10_code[number - 1]}')
    print(f'현재가 : {rateinfo_list[0].text}')
    print(f'전일가 : {rateinfo_list[3].text}')
    print(f'시가 : {rateinfo_list[7].text}')
    print(f'고가 : {rateinfo_list[4].text}')
    print(f'저가 : {rateinfo_list[8].text}')

def main():
    while True:
        print('-' * 40)
        print('[ 네이버 코스피 상위 10대 기업 목록 ]')
        print('-' * 40)
        i = 1
        for name in top10_name:
            print(f'[{i:2d}] : {name}')
            i += 1

        number = int(input('주가를 검색할 기업의 번호를 입력하세요(-1 : 종료) : '))
        if number == -1:
            print('프로그램 종료')
            break
        enterprise_info(number)

main()