#coding=utf-8
import requests
import json
import time
from lxml import etree

'''
http://www.auto1768.com/carWash/cityDetail.html?Jsource=ETCBK&cityName=池州市&cityTit=ETC车宝用户洗车网点&Code=341700&NewCode=1
'''
class MenDian:
    def __init__(self):
        self.headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        self.url = "http://www.auto1768.com/carWash/cityDetail.html?Jsource={}&cityName={}&cityTit={}&Code={}&NewCode=1"
        self.times = 0
        self.scctimes = 0

    def getUrlList(self):
        # 获取外部数据
        with open("./yunnan/yunnan.json",'r', encoding='UTF-8') as load_f:
            load_dict = json.load(load_f)
        UrlList = []
        # print(load_dict["keys"])
        for i in load_dict["keys"]:
            # print(i['id'],i['city'],i['name'],i['cityid'])
            url = self.url.format(i['id'],i['city'],i['name'],i['cityid'])
            UrlList.append((url,i['city']))   
        return UrlList

    def parse_url(self,url):
        self.times += 1
        print(url)
        print('开始' + str(self.times) + '次查询ING-----')
        response = requests.get(url,headers=self.headers,timeout=100) #发送请求
        html = response.content.decode() #获取html字符串
        # print(html)
        html = etree.HTML(html) #获取element 类型的html
        return html

    def get_info(self,url,city):
        '''获取一个页面的title和href'''
        html = self.parse_url(url)
        total_items = []
        div_temp_list = html.xpath("//div[@class='shopitem clearfix']") #分组，按照div标签分组
        for div in div_temp_list:
            com_name = div.xpath(".//div/p/text()")[0] if len(div.xpath(".//div/p/text()")[0]) > 0 else None
            com_addr = div.xpath(".//div/span[2]/text()")[0]  if len(div.xpath(".//div/p/text()")[0]) > 0 else None
            com_tel = div.xpath(".//div/span[1]/text()")[0] if len(div.xpath(".//div/p/text()")[0]) > 0 else None
            tempstr = com_name + ',' + com_tel + ',' + com_addr + ',' + city + '\n'
            print(tempstr)
            with open("./yunnan/yunnan1111.csv",'a', encoding='UTF-8') as ff:
                ff.write(tempstr)


    def run(self):
        # 1.读取文件生成每次请求的formdata
        UrlList = self.getUrlList()
        # 2. 遍历数据发起每一次请求
        for temp in UrlList:
            url = temp[0]
            self.get_info(url,temp[1])

if __name__ == "__main__":
    gogo = MenDian()
    gogo.run()