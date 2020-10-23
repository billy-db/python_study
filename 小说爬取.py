from  bs4 import  BeautifulSoup
import requests
import lxml
from lxml import etree
import  os
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }

url = 'https://www.77xsw.la/book/55621/'
page =  requests.get(url=url,headers=headers)
page.encoding = 'gbk'
page_text = page.text
#在首页中解析出章节的的标题和详情页的url
soup = BeautifulSoup(page_text,'lxml')
#print(soup)
fp = open('./111.txt','w',encoding='utf-8',errors='igore')
a_list = soup.select('#list-chapterAll > .panel-body > dd > a')
#print(a_list)
for i in a_list:
    b = i.string
    print(b)
    detail_url = url+i['href']
    print(detail_url)
    detail = requests.get(url=detail_url,headers=headers)
    detail.encoding = 'gbk'
    detail_text = detail.text
    detail_soup = BeautifulSoup(detail_text,'lxml')
    div_tag = detail_soup.find('div',class_='panel-body')
    content = div_tag.text
    fp.write(b+':'+content+'\n')
    print(b,"爬取成功")
