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
fp = open('./abc.txt','w',encoding='utf-8',errors='igore')
a_list = soup.select('#list-chapterAll > .panel-body > dd > a')
#print(a_list)
for i in a_list:
    b = i.string
    #print(b)
    a  = i['href']
    a = a.split('.')[0]+'_2.html'
    #print(a)
    detail_url = url+i['href']
    detail_url2 = url+a
    #print(detail_url+'\t'+detail_url2 )
    detail = requests.get(url=detail_url,headers=headers)
    detail2 = requests.get(url=detail_url2,headers=headers)
    detail.encoding = 'gbk'
    detail2.encoding = 'gbk'
    detail_text = detail.text
    detail2_text = detail2.text
    detail_soup = BeautifulSoup(detail_text,'lxml')
    detail_soup2 = BeautifulSoup(detail2_text,'lxml')
    div_tag = detail_soup.find('div',class_='panel-body')
    div_tag2 = detail_soup2.find('div',class_='panel-body')
    content = div_tag.text
    content2 = div_tag2.text
    fp.write(b+':'+content+content2+'\t')
    #fp.write(content2+'\t')
    print(b,"爬取成功")
