import requests
from bs4 import BeautifulSoup

# 로봇이 아니라는 것을 말해주는 코드
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

search = input("검색할 키워드 입력: ")
page = int(input("크롤링 할 페이지(숫자) 입력: "))

page_num = 1
if page:
    page_num = (page - 1) * 10 + 1

url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=" + search + "&start=" + str(page_num)
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.select("div.group_news > ul.list_news > li div.news_area > a")
# print(articles)

print("\n네이버에 '", search, "' 를 입력했을 때의 뉴스 기사", end= "\n")
print(page, "페이지의", end= " ")
print(len(articles), "개의 기사가 검색됨", end= "\n\n")

article_file = open("article.txt", "a", encoding="UTF-8")

i = 1
for article in articles:
    article_file.write(str(i) + "번째 기사: " + article.get_text() + "\n")
    print(str(i) + "번째 기사: " + article.get_text(),"\n")
    i += 1
