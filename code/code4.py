#coding=utf-8
import requests
import json
import time
from lxml import etree


'''
    获取全部的herf
'''

'''
http://www.auto1768.com/carWash/cityDetail.html?Jsource=ETCBK&cityName=池州市&cityTit=ETC车宝用户洗车网点&Code=341700&NewCode=1
'''

class DaZong:

    def __init__(self,part_id,page_num):
        self.headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Cookie": "showNav=#nav-tab|0|1; navCtgScroll=0; navCtgScroll=200; showNav=#nav-tab|0|1; _lxsdk_cuid=16c221a349fc8-0ffe94fa6babc5-c343162-100200-16c221a349f8c; _lxsdk=16c221a349fc8-0ffe94fa6babc5-c343162-100200-16c221a349f8c; _hc.v=6d45e5ab-9df8-8016-09c3-b6adce73e458.1563940239; s_ViewType=10; cy=7; cye=shenzhen; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_s=16c85337bd9-162-047-ee5%7C%7C738"}
        
        self.url = '''http://www.dianping.com/search/keyword/7/65_%E6%B4%97%E8%BD%A6/r{}p{}'''
        self.times = 0 # 统计获取次数
        self.scctimes = 0 # 统计获取的sccess times
        self.part_id = part_id # 城市的id
        self.page_num = page_num # 获取的页面数量

    def parse_url(self,url):
        self.times += 1
        response = requests.get(url,headers=self.headers,timeout=5) #发送请求
        html = response.content.decode() #获取html字符串
        print(html)
        html = etree.HTML(html) #获取element 类型的html
        return html
    
    def constsruct_url_list(self):
        urlList = []
        for page in range(1,self.page_num+1):
            urlList.append(self.url.format(self.part_id,page))
        return urlList

    def getNextUrlList(self,url):
        '''
        获取下一城级别的url list
        '''
        html = self.parse_url(url)
        li_temp_list = html.xpath("//div[@id='shop-all-list']/ul/li") # 分组，按照li标签分组
        # print(li_temp_list)
        for liTemp in li_temp_list:
            href = liTemp.xpath("./div[@class='pic']/a/@href")
            print(href)
        return []

    def run(self):
        part_url_list = self.constsruct_url_list()
        for url in part_url_list:
            nextUrlList = self.getNextUrlList(url)


if __name__ == "__main__":
    dazong = DaZong(31,1)
    dazong.run()