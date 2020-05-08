#coding=utf-8
import requests
import json


class City:
    def __init__(self):
        self.headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        self.url = 'https://open.chediandian.com/wash/ent-list/get-list'
        self.times = 0
        self.scctimes = 0
        self.now_len = 1
        self.city = ''

    def getEachFromdate(self):
      # 获取外部数据
      formdateList = [a for a in range(1,200)]
      # formdateList = [a for a in range(0,10)]
      return formdateList

    def getCityList(self):
        with open("./city.json",'r', encoding='UTF-8') as load_f:
            load_dict = json.load(load_f)
        cityList = []
        all_data = load_dict["keys"]
        for one_data in all_data:
            prov = one_data["prov"]
            city = one_data["city"]
            cityList.append((prov,city))       
        return cityList

    def findTypeCity(self,temp,city):
        self.times += 1
        print('开始' + str(self.times) + '次查询ING-----')
        formdata = {
            "serviceIds":"300006386",
            "commentStar":"0",
            "mainBusiness":"-1",
            "city":city,
            "district": "",
            "keyword":"",
            "lng":"114.02597366",
            "lat": "22.54605355",
            "pageIndex":temp
        }
        print(self.url)
        response = requests.post(self.url, data = formdata, headers = self.headers)
        new_dict = json.loads(response.text)
        # print(new_dict['EntList'])
        if new_dict['Code'] == 1:
            self.scctimes += 1
            print('查询成功---' + str(self.scctimes) + '---次')
        else:
            return None
        return new_dict['EntList']

    def run(self):
        cityList = self.getCityList()
        temp = 1
        for city in cityList:
            prov_name = city[0]
            print(prov_name)
            while self.now_len >= 1:
                returnResult = self.findTypeCity(temp,city[1])
                temp += 1
                self.now_len = len(returnResult)
                print(self.now_len)
                for tpdata in returnResult:
                    EntName = tpdata['EntName']
                    Mobile = tpdata['Mobile']
                    Address = tpdata['Address']
                    WorkTime = tpdata['WorkTime']
                    str = city[0] + "," + city[1] + "," + EntName + "," + Mobile + "," + Address + "," + WorkTime + "\n"
                    print(str)
                    with open("./china/111.csv",'a', encoding='UTF-8') as ff:
                        ff.write(str)
            self.now_len = 1
            temp = 1


if __name__ == "__main__":
    gogo = City()
    gogo.run()