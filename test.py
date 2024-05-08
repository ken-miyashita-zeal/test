import csv
import requests
from bs4 import BeautifulSoup

# ジールのセットWebページからAWSを検索したWebページ
search_url = 'https://zdh.stagingbridge.net/?s=aws'

# ジールのセットWebページにアクセス
search_response = requests.get(search_url)

# ページの内容を解析
search_soup = BeautifulSoup(search_response.text, 'html.parser')

# CSVファイルの出力先パス
output_path = r'C:\Users\ken.miyashita\Documents\個人データ\Pyhton\TEST\test.csv'

# CSVファイルを読み込み、ヘッダーの書き込み
with open(output_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Title', 'URL'])

    # 検索結果のページから、タイトルとURLを取得してCSVファイルに書き込む
    for item in search_soup.find_all('div', class_='result-list'):
        title = item.find('span', class_='ttl').text.strip()
        url = item.find('a')['href']
        csvwriter.writerow([title, url])