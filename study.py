#!/usr/bin/python3


'''
# 网页采集器
import  requests
#UA检测：门户网站的服务器会检测对应请求的身份标识，如果检测到请求的载体身份标识为某一款浏览器，那么就说明该请求是一个正常请求，
# 但是，如果检测到请求的载体的身份标识不是基于某一款浏览器，则表示该请求为不正常的请求（爬虫），则服务器段很可能拒绝这次请求。
#UA： User-Agent(请求载体的身份标识)
#UA伪装: 让爬虫对应得请求载体身份标识伪装成某一款浏览器
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    #处理URL携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    #对指定的URL发起的请求对应得URL是携带参数的，并且请求过程中处理了参数
    reponse = requests.get(url=url,params=param,headers=headers)
    page_text = reponse.text

    filename = kw +'.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename,"保存成功！！！")
'''          #网页采集器
'''
 #需求：破解百度翻译
 #   - post请求（携带了参数）
 #   - 响应数据是一组json数据 

import requests
import json
if __name__ == '__main__':
    #1.指定URL
    post_url = 'https://fanyi.baidu.com/sug'
    #2.UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    #3. post请求参数处理（同get请求一致）
    kw = input('enter a word:')
    data = {
        'kw': kw
    }
    #4.请求发送
    reponse = requests.post(url=post_url,data=data,headers=headers)
    #5.获取响应数据.json()方法返回的是obj(如果确认响应数据是json类型的，才可以使用.json（）)
    dic_obj = reponse.json()
    filename = kw+'.json'
    fp = open(filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
'''    #破解百度翻译
'''
import requests
import json
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '0',#从库中的第几部电影去取
        'limit': '20',#一次取出的个数
    }
    reponse = requests.get(url=url,params=param,headers=headers)
    list_data = reponse.json()
    print(list_data)
    fp = open('./doubai.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
'''    # 爬取豆瓣电影分类排行榜
'''
import requests
import json
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    kw = input('请输入城市: ')
    data = {
        'cname': '',
        'pid': '',
        'keyword': kw,
        'pageIndex': '1',
        'pageSize': '100',
    }'
    reponse = requests.post(url=url,data=data,headers=headers)
    page_text = reponse.text
    print(page_text)
    #obj_json = json.dumps(page_text)
    #print(obj_json)
'''    # 爬取kfc 指定城市的门店地址

import requests
import  json
'''
if __name__ == '__main__':
    #批量获取不同企业的ID值
    id_list = []
    all_data_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    for page in range(1,7):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        json_ids = requests.post(url=url,data=data,headers=headers).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
    #获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data={
            'id':id
        }
        detai_json = requests.post(url=post_url,headers=headers,data=data).json()
        all_data_list.append(detai_json)
    #持久化存储
    fp = open('./alldata.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('over!!!')
    #获取药监局相关数据
'''
#需求：爬取糗事百科的糗图
# import requests
# from  bs4 import  BeautifulSoup
# import  re
# import os
# import lxml
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
#     }
# '''
# path = 'C:/Users/Administrator/Pictures/qiutu/'
# if not os.path.exists(path):
#     os.mkdir(path)
#
# url = 'https://www.qiushibaike.com/imgrank/page/%d'
# for pagnum in range(1,3):
#     #使用通用爬虫对url对应的一整张页面进行爬取
#     new_url= format(url%pagnum)
#     page_text = requests.get(url=new_url,headers=headers).text
#     #使用聚焦爬虫将页面中的所有糗图进行解析
#     # <div class="thumb">
#     #
#     # <a href="/article/123678037" target="_blank">
#     # <img src="//pic.qiushibaike.com/system/pictures/12367/123678037/medium/6VIEUWKAUJ2YG0EK.jpg" alt="糗事#123678037" class="illustration" width="100%" height="auto">
#     # </a>
#     # </div>
#     ex  = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
#     img_herf = re.findall(ex,page_text,re.S)
#     #print(img_herf)
#     for i in img_herf:
#         src = 'https:'+i
#         #请求到了图片的二进制数据
#         imgae_date = requests.get(url=src,headers=headers).content
#         #生产图片名称
#         img_name = src.split('/')[-1]
#         img_path = path+img_name
#         with open(img_path,'wb',) as fp:
#             fp.write(imgae_date)
#             pagnum =str(pagnum)
#             print(img_name,"下载成功")
#     print("==============第"+pagnum+"页下载成功================")
# '''#爬取糗事百科的糗图(只是爬取全两页)
# url = 'https://www.biquge.com.cn/book/32883/'
# fp = open('./333.txt','w',encoding='utf8')
# page_text = requests.get(url=url,headers=headers).text
# soup = BeautifulSoup(page_text,'lxml')
# li_list = soup.select('#list > dl > dd' )
# for i in li_list:
#     title = i.a.string
#     detail_url = 'https://www.biquge.com.cn'+i.a['href']
#     #print(title)
#     #print(detail_url)
#     detail_text = requests.get(url=detail_url,headers=headers).text
#     detail_soup = BeautifulSoup(detail_text,'lxml')
#     #print(detail_soup)
#     detail_body = detail_soup.find('div',id='content')
#     content = detail_body.text
#     fp.write(title+'---++--'+content+'\n')
#     print(title+'：----爬取成功----')
print("hello \rWo \brd")