from  bs4 import  BeautifulSoup
import requests
import lxml
from lxml import etree
import  os
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }

# 聚焦爬虫：爬取页面指定内容
# -*- coding:utf-8 -*-
# 数据解析分类：
# 		- 正则
# 		- bs4
# 		- xpath
# 数据解析原理概述：
# 		- 解析的局部的文本内容都会在标签之间或者标签对应的属性中进行存储
# 		- 1.进行指定标签的定位
# 		- 2.标签的或者标签对应的属性中存储的的数据值进行提前（解析）
'''
#需求：爬取糗事百科的糗图
import requests
import  re
import os
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
path = 'C:/Users/Administrator/Pictures/qiutu/'
if not os.path.exists(path):
    os.mkdir(path)

url = 'https://www.qiushibaike.com/imgrank/'
#使用通用爬虫对url对应的一整张页面进行爬取
page_text = requests.get(url=url,headers=headers).text
#使用聚焦爬虫将页面中的所有糗图进行解析
# <div class="thumb">
#
# <a href="/article/123678037" target="_blank">
# <img src="//pic.qiushibaike.com/system/pictures/12367/123678037/medium/6VIEUWKAUJ2YG0EK.jpg" alt="糗事#123678037" class="illustration" width="100%" height="auto">
# </a>
# </div>
ex  = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
img_herf = re.findall(ex,page_text,re.S)
#print(img_herf)
for i in img_herf:
    src = 'https:'+i
    #请求到了图片的二进制数据
    imgae_date = requests.get(url=src,headers=headers).content
    #生产图片名称
    img_name = src.split('/')[-1]
    img_path = path+img_name
    with open(img_path,'wb',) as fp:
        fp.write(imgae_date)
        print(img_name,"下载成功")
'''
# bs4进行数据解析的原理：
#     - 1. 实例化一个BeatifulSoup对象，并且将页面源码数据加载到该对象中
#     - 2.通过调用BeatifulSoup对象重点相关的属性或者方法进行标签定位和数据提取
#     - 环境安装：- pip install bs4
#     - pip install lxml

# url = 'https://www.77xsw.la/book/55621/'
# page =  requests.get(url=url,headers=headers)
# page.encoding = 'gbk'
# page_text = page.text
# #在首页中解析出章节的的标题和详情页的url
# soup = BeautifulSoup(page_text,'lxml')
# #print(soup)
# fp = open('./111.txt','w',encoding='utf-8',errors='igore')
# a_list = soup.select('#list-chapterAll > .panel-body > dd > a')
# #print(a_list)
# for i in a_list:
#     b = i.string
#     print(b)
#     detail_url = 'https://www.77xsw.la/book/55621/'+i['href']
#     print(detail_url)
#     detail = requests.get(url=detail_url,headers=headers)
#     detail.encoding = 'gbk'
#     detail_text = detail.text
#     detail_soup = BeautifulSoup(detail_text,'lxml')
#     div_tag = detail_soup.find('div',class_='panel-body')
#     content = div_tag.text
#     fp.write(b+':'+content+'\n')
#     print(b,"爬取成功")

#爬取58二手房
# import requests
# import lxml
# from lxml import etree
# url = 'https://bj.58.com/yizhuang/ershoufang/'
# page_text = requests.get(url=url,headers=headers).text
# tree = etree.HTML(page_text)
# li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
# # print(li_list)
# for i in li_list:
#     title = i.xpath('./div[2]/h2/a/text()')[0]
#     base_info = i.xpath('./div[2]/p[1]/span//text()')[0]
#     base_info_2 = i.xpath('./div[2]/p[2]/span[1]/a//text()')
#     price = i.xpath('./div[3]/p[1]//text()')
#     danjia = i.xpath('./div[3]/p[2]/text()')
#
#     print(danjia)
'''
url = 'https://music.163.com/artist?id=4292'
base_url ='https://music.163.com/song/media/outer/url?id='
path = 'D:/Program Files (x86)/网易云音乐/'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
lt_list = tree.xpath('//div[@id="song-list-pre-cache"]/ul/li')
for i in lt_list:
       song = i.xpath('./a/@href')[0]
       song_id = song.split('=')[1]
       title = i.xpath('./a/text()')[0]
       songurl = base_url+song_id
       print(songurl)
       song_dir = requests.get(url=songurl,headers=headers)
       with open(path+title+'.mp3','wb') as fp:
           fp.write(song_dir.content)
       print(title+'下载成功')
print('over!!!!')
# 爬取指定歌手的网易云音乐 需要挂vpn 到国内
'''

# url = 'https://www.huya.com/g/4079'
# page_text = requests.get(url=url,headers=headers).text
# path = 'C:/Users/Administrator/Desktop/虎牙女主播图片/'
# tree = etree.HTML(page_text)
# imgurl_list = tree.xpath('//ul[@class="live-list clearfix"]/li')
# #print(imgurl_list)
# for img in imgurl_list:
#     imgurl = img.xpath('./a/img/@data-original')[0]
#     img_url = imgurl.split('?')[0]
#     title = img.xpath('./span/span/i/@title')[0]
#     #print(title)
#     imgpic = requests.get(url=img_url,headers=headers).content
#     with open(path+title+'.jpg','wb') as fp:
#             fp.write(imgpic)
#     print(title+'.jpg'+'---下载成功')
# print('全部下载成功')
# 读取txt文件写入数据库
'''
url = 'http://pic.netbian.com/4kmeinv/'
if not os.path.exists('C:/Users/Administrator/Desktop/piclibs/'):
        #print('meiyou')
        os.mkdir('C:/Users/Administrator/Desktop/piclibs/')
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="slist"]/ul/li')
for i in li_list:
    img_src = 'http://pic.netbian.com'+i.xpath('./a/img/@src')[0]
    img_name = i.xpath('./a/img/@alt')[0]+'.jpg'
    img_name = img_name.encode('iso-8859-1').decode('gbk')
    print(img_name+'----'+img_src)
    img_data = requests.get(url=img_src,headers=headers).content
    img_path = 'C:/Users/Administrator/Desktop/piclibs/'+img_name
    with open(img_path,'wb') as fp:
        fp.write(img_data)
        print(img_name+'下载成功')
'''     #4k图片解析下载
if not os.path.exists('C:/Users/Administrator/Desktop/jianli/'):
        #print('meiyou')
        os.mkdir('C:/Users/Administrator/Desktop/lianji/')
url = 'http://sc.chinaz.com/jianli/free.html'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="container"]/div')
downurl =[]
#print(li_list)
for i in li_list:
    first_url = i.xpath('./a/@href')[0]
    #name = i.xpath('./a/img/@alt')[0]
    #name =name.encode('iso-8859-1').decode('gbk')
    pagetwo_text = requests.get(url=first_url,headers=headers).text
    treetwo = etree.HTML(pagetwo_text)
    two_list = treetwo.xpath('//*[@id="down"]/div[2]/ul/li[10]')
    for i in two_list:
        download_url = i.xpath('./a/@href')[0]
        name = download_url.split('/')[-1]
        print(name)
        jianli_tat = requests.get(url=download_url,headers=headers).content
        with open('C:/Users/Administrator/Desktop/lianji/'+name,'wb') as fp:
            fp.write(jianli_tat)
            print(name+'下载成功')
            break



