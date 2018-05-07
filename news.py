#coding:utf-8
import requests
from bs4 import BeautifulSoup
base_url = 'https://tw.news.yahoo.com'
headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
})
global news
news=[]
def crawer_news():
    response_get=requests.get(base_url,headers=headers)
    soup= BeautifulSoup(response_get.text,'html.parser')
    news_tag=soup.find('ul',attrs={'class':'Z(0) Pos(r) W(100%) H(312px) Fz(16px)'})
    news_tag=news_tag.find_all('a')
    # global news
    index=1
    for new in news_tag:
        if new.text=='':
            continue
        news.append({
            'title':new.text,
            'url':base_url+new['href']
        })
        print(str(index)+'. '+new.text)
        index+=1

def crawer_new_content(index):
    index=int(index)-1
    response_get=requests.get(news[index]['url'],headers=headers)
    soup=BeautifulSoup(response_get.text,'html.parser')
    new_content=soup.find('article')
    # print(new_content.text+'\n')
    for article in new_content.children:
        if article.name != 'figure':
            new_content = article
            break
    for text in new_content:
        if text.name=='p' and (text.text.strip()!='' and text.text[0]!='▲' and text.text[0]!='▼'and ('／' not in text.text)) :
            print(text.text)
            break


crawer_news()
while True:
    index=input("要閱覽的新聞編號: ")
    if(index=='quit'):
        print('bye')
        break
    crawer_new_content(index)