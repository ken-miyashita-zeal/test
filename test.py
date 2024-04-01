import csv
import requests
from bs4 import BeautifulSoup

# ジールのセットWebページ
url = 'https://zdh.stagingbridge.net/'

# ジールのセットWebページにアクセス
response = requests.get(url)

# ページの内容を解析
soup = BeautifulSoup(response.text, 'html.parser')

# CSVファイルの出力先パス
output_path = r'C:\Users\ken.miyashita\Documents\個人データ\Pyhton\test.csv'

# 「AWS」の記載がある記事のタイトルとURLを取得し、test.csvに書き込む
with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Title', 'URL'])
    
    for article in soup.find_all('article'):
        title = article.find('h2').text
        url = article.find('a')['href']
        if 'AWS' in title:
            csvwriter.writerow([title, url])
