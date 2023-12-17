import pandas as pd
import requests
from bs4 import BeautifulSoup

query = "한파" 
page = 1

data = {'Title': [], 'Summary': []}

for i in range(1, page+1):
    url = 'https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q={}&p={}'.format(query, i)
    news = requests.get(url)
    news_bs = BeautifulSoup(news.content, 'html.parser')
    news_list = news_bs.findAll('div', class_="item-bundle-mid")

    for item in news_list:
        title = item.find('a').text
        summary = item.find('p').text
        
        data['Title'].append(title)
        data['Summary'].append(summary)

# 데이터프레임 생성
df = pd.DataFrame(data)

# 엑셀 파일로 저장
excel_filename = 'news_data.xlsx'
df.to_excel(excel_filename, index=False)

print(f"데이터가 '{excel_filename}' 파일로 저장되었습니다.")
