import csv
import requests
from bs4 import BeautifulSoup

# ジールのセットWebページ
url = 'https://zdh.stagingbridge.net/topics/'

# ジールのセットWebページにアクセス
response = requests.get(url)

# ページの内容を解析
soup = BeautifulSoup(response.text, 'html.parser')

# CSVファイルの出力先パス
output_path = output\test.csv'

# 「AWS」の記載がある記事のタイトルとURLを取得し、test.csvに書き込む
with open(output_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Title', 'URL'])
    
    for article in soup.find_all('a', class_='news-list'):
        title_elements = article.find_all('p')
        for title_element in title_elements:
            if 'AWS' in title_element.text:
                title = title_element.text
                url = article['href']
                csvwriter.writerow([title, url])
                break  # 記事に関連する属性のループを終了
