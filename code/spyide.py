#coding=utf-8
import requests

class Companys:
    # 公司数据爬虫类
    def __init__(self):
        #设置为电脑端的UA
        self.headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"}
        self.cccpplist=[
            "北京银行深圳分行用户洗车网点",
            "车享家（上海 深圳）用户洗车网点",
            "光大深圳用户洗车网点",
            "光大深圳全套精洗用户洗车网点",
            "广发深圳用户洗车网点",
            "广发深圳公关用户洗车网点",
            "华润通深圳用户洗车网点",
            "农业银行深圳分行用户洗车网点",
            "平安银行深圳分行财富客户用户洗车网点",
            "平安银行深圳分行平安会员宝银企盛大洗车卡用户洗车网点",
            "深圳蜂鸟（上海银行深圳分行洗车）用户洗车网点",
            "深圳农商行用户洗车网点",
            "深圳农商行公关用户洗车网点",
            "深圳农行打蜡项目用户洗车网点",
            "深圳邮储用户洗车网点",
            "深圳云车18项安全检测用户洗车网点",
            "深圳云车（平安总部）用户洗车网点",
            "深圳云车代步车用户洗车网点",
            "深圳云车划痕补漆用户洗车网点",
            "深圳云车科技洗车用户洗车网点",
            "太平财险深圳分公司用户洗车网点",
            "新北京银行深圳分行用户洗车网点",
            "邮储银行深圳分行公关券用户洗车网点",
            "招商银行深圳分行采购用户洗车网点",
            "浙商深圳用户洗车网点",
            "中国银行深圳分行（线上）用户洗车网点",
            "中国银行深圳龙岗分行用户洗车网点",
            "中国银行深圳市分行用户洗车网点"
        ]
        
    def get_total_url_list(self):
        '''获取所有的urllist'''
        url ="http://www.auto1768.com/carWash/cityDetail.html?Jsource=CEBSZ&cityName=深圳市&cityTit={}&Code=440300&NewCode=1"
        url_list = []
        for i in self.cccpplist: 
            url_list.append(url.format(i))
        return url_list

    def parse_url(self,url):
        '''一个发送请求，获取响应，同时etree处理html'''
        response = requests.get(url,headers=self.headers,timeout=10) #发送请求
        html = response.content.decode() #获取html字符串
        # html = etree.HTML(html) #获取element 类型的html
        # return html
        print(html)

    def run(self):
        url_list = self.get_total_url_list()
        for url in url_list:
            self.parse_url(url)

if __name__ == "__main__":
    gogo = Companys()
    gogo.run()