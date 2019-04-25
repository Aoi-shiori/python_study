import requests
from lxml import etree
import json


url_temp = "http://thz8.net/forum-181-1.html"
headers = {"Host":"thz8.net",
                            "Proxy-Connection": "keep-alive",
                            "Cache-Control": "max-age=0",
                            "Upgrade-Insecure-Requests": "1",
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36",
                            "DNT": "1",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                            "Accept-Encoding": "gzip, deflate",
                            "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
                            "Cookie":"WMwh_2132_saltkey=bblF5LBV; WMwh_2132_lastvisit=1554903667; UM_distinctid=16a07bf526f555-09d84eb7595497-61507e2b-7e9000-16a07bf5270816; HstCfa2810755=1554908170936; HstCmu2810755=1554908170936; __dtsu=2DE7B66B597C7B58E6624D7202972FB1; CNZZDATA1254190848=1529662506-1554907571-http%253A%252F%252Ft.thzdz.us%252F%7C1555836313; HstCnv2810755=25; Hm_lvt_acfaccaaa388521ba7e29a5e15cf85ad=1555710661,1555711398,1555785934,1555839590; HstCns2810755=36; HstCla2810755=1555839631309; HstPn2810755=8; HstPt2810755=162; yunsuo_session_verify=0d93d8b672b8aca8d3ee8d0967767041; WMwh_2132_st_t=0%7C1555839232%7C1baa2aa18774ab94d1453875b50ee7df; WMwh_2132_forum_lastvisit=D_220_1555711586D_182_1555711591D_69_1555711963D_203_1555712697D_181_1555839232; WMwh_2132_sendmail=1; Hm_lpvt_acfaccaaa388521ba7e29a5e15cf85ad=1555840120; WMwh_2132_lastact=1555839233%09misc.php%09secqaa; WMwh_2132_secqaa=405693.30eb43e47d9d9df17d"}



print("now parseing:",url_temp )
response = requests.get(url_temp, headers=headers)
htm_str = response.content.decode()
print(htm_str)



