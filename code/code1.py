#coding=utf-8
import requests
import json

class City:
    def __init__(self):
        self.headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        self.url = 'http://www.auto1768.com/carWash/queryCityByShop'
        self.times = 0
        self.scctimes = 0

    def getEachFromdate(self):
        # 获取外部数据
        with open("./type.json",'r', encoding='UTF-8') as load_f:
            load_dict = json.load(load_f)
        formdateList = []
        for i in load_dict:
            formdateList.append((i,load_dict[i]))   
        return formdateList

    def findTypeCity(self,temp):
        self.times += 1
        print('开始' + str(self.times) + '次查询ING-----')
        formdata = {
            "source":temp[0],
            "title":"",
            "ditch":"1"
        }
        response = requests.post(self.url, data = formdata, headers = self.headers)
        new_dict = json.loads(response.text)
        print(new_dict)
        if new_dict['resultCode'] == "200":
            self.scctimes += 1
            print('查询成功---' + str(self.scctimes) + '---次')
        else:
            return (None,None)

        tempre = (new_dict['source'],new_dict['result'])
        return tempre

    def run(self):
        # 1.读取文件生成每次请求的formdata
        formdateList = self.getEachFromdate()
        # 2. 遍历数据发起每一次请求
        for temp in formdateList:
            returnResult = self.findTypeCity(temp)
            if returnResult[0] == None:
                continue
            for province in returnResult[1]:
                shengfen = province['province']
                Citylist = province['citys']
                for oneCity in Citylist:
                    cityName = oneCity['cityName']
                    cityCode = oneCity['cityCode']
                    # print(temp[1],temp[0],shengfen,cityName,cityCode)
                    str = temp[0] + ',' + temp[1] + ',' + shengfen + ',' + cityName + ',' + cityCode + '\n'
                    with open("./shengda.csv",'a', encoding='UTF-8') as ff:
                        ff.write(str)

if __name__ == "__main__":
    gogo = City()
    gogo.run()