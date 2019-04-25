import requests
from lxml import etree
import json

class Taohuazu:
    def __init__(self):
        self.url_temp = "http://thz8.net/forum-181-1.html"
        self.headers = {"Host":"thz8.net",
                            "Proxy-Connection": "keep-alive",
                            "Cache-Control": "max-age=0",
                            "Upgrade-Insecure-Requests": "1",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36",
                            "DNT": "1",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                            "Accept-Encoding": "gzip, deflate",
                            "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
                            "Cookie":"WMwh_2132_saltkey=bblF5LBV; WMwh_2132_lastvisit=1554903667; UM_distinctid=16a07bf526f555-09d84eb7595497-61507e2b-7e9000-16a07bf5270816; HstCfa2810755=1554908170936; HstCmu2810755=1554908170936; __dtsu=2DE7B66B597C7B58E6624D7202972FB1; CNZZDATA1254190848=1529662506-1554907571-http%253A%252F%252Ft.thzdz.us%252F%7C1555836313; HstCnv2810755=25; Hm_lvt_acfaccaaa388521ba7e29a5e15cf85ad=1555710661,1555711398,1555785934,1555839590; HstCns2810755=36; HstCla2810755=1555839631309; HstPn2810755=8; HstPt2810755=162; yunsuo_session_verify=0d93d8b672b8aca8d3ee8d0967767041; WMwh_2132_st_t=0%7C1555839232%7C1baa2aa18774ab94d1453875b50ee7df; WMwh_2132_forum_lastvisit=D_220_1555711586D_182_1555711591D_69_1555711963D_203_1555712697D_181_1555839232; WMwh_2132_sendmail=1; Hm_lpvt_acfaccaaa388521ba7e29a5e15cf85ad=1555840120; WMwh_2132_lastact=1555839233%09misc.php%09secqaa; WMwh_2132_secqaa=405693.30eb43e47d9d9df17d"
                        }


    # 函数get_url_list：根据网页内容提取URL地址，构造url list,返回一组地址 需要调试，
    def get_url_list(self):
        htm=self.parse_url(self.url_temp)
        html = etree.HTML(htm)
        tbody_list = html.xpath(".//table[@summary='forum_181']/tbody/tr/td/a/@href") #获取地址列表
        print("tbodyli是",tbody_list)
        # for url in tbody_list:
        #     url_list= "http://thz8.net/"+url if len(url) > 0 else None
        #     print("return的网址是", url_list)
        # return url_list
        url_list =["http://thz8.net/"+url if len(url) > 0 else None for url in (tbody_list)]
        return  url_list
        print("取得的网址是", url_list)

    # 函数parse_url：转码返回的请求，并return 首次返送请求主列表页面，然后转码
    def parse_url(self, url):    #获取返回的信息 OK
        print("Now parseing:", url)
        response = requests.get(url, headers=self.headers)
        rp =response.content.decode()
        print(response)
        return rp

    # 函数：get_connect_list 获取到列表信息，请求返回需要的页面信息，然后提取数据
        # 下载窗口链接地址提取"//*[@class='attnm']/a/@href"
        # 下载窗口种子下载地址连接提取"//*[@class ="f_c"]/div[2]/div[2]/a/@href"
    def get_connect_list(self, html_str):
        html = etree.HTML(html_str)
        # 分组
        item = {}
        connect_list = []

        item["title"] = html.xpath("//h1/span/text()")
        #item["massage"] = html.xpath("//td[@class='t_f']/text()")
        item["img"] = html.xpath("//td[@class='t_f']/img/@src")
        item["img"] ="http://thz8.net/" + item["img"][0] if len(item["img"])>0 else None
        line_list = html.xpath("//*[@class ='attnm']/a/@href")
        item["torrent"] = self.url_lis(line_list)
        #print("获取到的返回格式数据是", line_list)
        #connect_list.append(item)
        return item

    # 函数：url_lis转到种子下载窗口页面，获取实际的种子下载地址，返回
    def url_lis(self, line_list):
            line_list=str(line_list).replace("['","")
            line_list =line_list.replace("']","")
            url_l = "http://thz8.net/"+line_list if len(line_list) > 0 else None

            url1=self.parse_url(url_l)
            url2= etree.HTML(url1)
            url_line =url2.xpath("//div[@style = 'padding-left:10px;']/a/@href")
            #print("种子下载", url_line)
            return url_line

    # 函数：save_connect_list，将获取到的数据保存起来
    def save_connect_list(self, item):
        with open("taohuazu.txt", "a", encoding="utf-8") as f:
                connect_list = []
            #for connect in item
                connect_list.append(item)
                f.write(json.dumps(connect_list, ensure_ascii=False))
                f.write("\n")
                print("保存成功！")



    # url=[self.url_temp.format(i) for i in range() ]
    # //*[@id="filter_orderby_menu"]

    def main_run(self):
    #1.根据url地址的规律，构造url
        url_lists= self.get_url_list() #返获取地址
        #print("打印出取得的地址",url_lists)
    #2.发送请求,获取回应
        for url in url_lists:
            html_str = self.parse_url(url)  # 1、获取列表页面的返回数据，提取页面中需要的地址数据

    #3，提取数据
            connect_list = self.get_connect_list(html_str)

    #4.保存
            self.save_connect_list(connect_list)


if __name__=='__main__':
    thz = Taohuazu()
    thz.main_run()