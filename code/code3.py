
#coding=utf-8
import requests
import json

class City:
    def __init__(self):
        self.headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        self.url = 'http://ycpdapi.hotgz.com/CarRaisingOfficial/GetStore'
        self.times = 0
        self.scctimes = 0

    def getEachFromdate(self):
      # 获取外部数据
      formdateList = [a for a in range(1,30)]
      return formdateList

    def findTypeCity(self,temp):
        self.times += 1
        print('开始' + str(self.times) + '次查询ING-----')
        formdata = {
            "index":temp,
            "PrivanceID":"151215010000000014",
            "CityID":"170903010000026224",
            "ServiceID":"151217010000000035",
            "StoreTypeID": "0",
            "pagesize":"12"
        }
        response = requests.post(self.url, data = formdata, headers = self.headers)
        new_dict = json.loads(response.text)
        # print(new_dict['Code'])
        if new_dict['Code'] == 200:
            self.scctimes += 1
            print('查询成功---' + str(self.scctimes) + '---次')
        else:
            return None
        return new_dict['Data']

    def run(self):
        # 1.读取文件生成每次请求的formdata
        formdateList = self.getEachFromdate()
        # 2. 遍历数据发起每一次请求
        for temp in formdateList:
            returnResult = self.findTypeCity(temp)
            if returnResult == None:
                continue
            for tpdata in returnResult['list']:
                StoreName = tpdata['StoreName']
                Address = tpdata['Address']
                str = StoreName + ',' + Address + ',' + '\n'
                with open("./yangchesz.csv",'a', encoding='UTF-8') as ff:
                    ff.write(str)

if __name__ == "__main__":
    gogo = City()
    gogo.run()