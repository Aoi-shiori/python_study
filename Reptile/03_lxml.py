#codin =utf-8
from lxml import etree
import requests
url ="https://movie.douban.com/chart"
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
response =requests.get(url,headers=headers)
htm_str = response.content.decode() #将获取到的返回内容转化成str类型
# print(htm_str)
#使用etree处理数据
html =etree.HTML(htm_str)
#1.获取所有的电影的url地址
# url_list=html.xpath("//div[@class='indent']/div/table//div[@class ='pl2']/a/@href")
# print(url_list)
#2.获取所有的图片地址
# img_list = html.xpath("//div[@class='indent']/div/table//a[@class='nbg']/img/@src")
# print(img_list)
#3.需要把每部电影组成一个字典，字典中是电影的各种数据，比如标题，url,图片地址，评论数，评分
#思路：
        #1、第一步分组
        #2、每一组提取数据
set_1=html.xpath("//div[@class='indent']/div/table") #已经定位到当前的table
# print(set_1)

#特别注意路径地址，已经在当前table下
for table in  set_1:
    item = {}
    item["title"]=table.xpath(".//div[@class ='pl2']/a/text()")[0].replace("/","").strip() #获取电影名称，并将"/'用空代替，并通过strip移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
    item['href']=table.xpath(".//div[@class ='pl2']/a/@href")[0] #获取电影链接地址
    item['img'] = table.xpath(".//a[@class ='nbg']/img/@src")[0] #获取图片地址
    item['comment_Num'] = table.xpath(".//span[@class ='pl']/text()")[0] #获取评分人数
    item['comment_Fraction'] = table.xpath(".//span[@class ='rating_nums']/text()") #获取上映时间，演职员信息
    item['p_lis'] =table.xpath(".//p[@class ='pl']/text()")[0].replace("/",".").strip("...")
    print(item)