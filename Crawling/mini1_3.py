# requests, BeautifulSoup, urllib.request 패키지 가져오기
import requests
from bs4 import BeautifulSoup
import urllib.request

# 검색어 입력 후 search_text에 저장
search_text = input("검색어를 입력하세요: ")

# 검색할 결과가 뉴스인지 이미지인지 확인
search_type = input("news / image 중 하나를 선택해주세요: ")

# 가져올 url 문자열로 입력
url = f'https://search.naver.com/search.naver?where={search_type}&sm=tab_jum&query={search_text}'

# BeautifulSoup 에러로 인해 header 추가
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

# requests의 get 함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
response = requests.get(url, headers=headers)

# html을 잘 정리된 형태로 변환
soup = BeautifulSoup(response.text, 'html.parser')

# 이미지 이름 구분하기 위한 변수
cnt = 1

# a 태그의 class 속성명이 news_tit인 태그를 찾고 반복문을 돌며 뉴스의 text 부분만을 잘라 print
if search_type == "news":
    for news in soup.select('a.news_tit', limit=10):
        print('title: ' + news.text.strip())

elif search_type == "image":
# img태그를 가지고 있는 것을 총 10개 찾고, 반복문을 돌며 이미지 파일 해당 위치에 저장
    for image in soup.find_all('img', limit=10):
        urllib.request.urlretrieve(image['src'], search_text + str(cnt) + '.jpg')
        cnt += 1

