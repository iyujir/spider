import requests
import json

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

url = 'http://www.autoxiaoer.com/usr/shop/near'

deteilUrl = 'http://www.autoxiaoer.com/usr/shop/detail'

hasNext = True
pageNow = 1

while hasNext:
    formdata = {"token":"5684b18ee94b980ab80e2fc990dd88e055fd76fe","data":{"area":"迪庆藏族自治州","lng":113.223432,"lat":23.3221132,"cid":31,"scid":0,"page":pageNow,"pageSize":10,"ids":"","withService":1,"noRound":1,"shopNameOrService":"","fullSubtraction":-1,"channel":2}}
    response = requests.post(url, data = json.dumps(formdata), headers = headers)
    pageNow += 1
    new_dict = json.loads(response.text)
    shops = new_dict['data']
    shop_list = shops['shops']
    if len(shop_list) < 10:
        hasNext = False
    for oneshop in shop_list:
        id = oneshop['id']
        nextFormDate = {"token":"5684b18ee94b980ab80e2fc990dd88e055fd76fe","data":{"id":str(id),"lng":"113.223432","lat":"23.3221132","channel":2}}



        print(nextFormDate)
        tempres = requests.post(deteilUrl, data = json.dumps(nextFormDate), headers = headers)
        # print(tempres.content)
        thisdict = json.loads(tempres.text)

        eashop = thisdict['data']['detail']

        thisid = str(eashop['id'])
        name = eashop['name']
        province = eashop['province']
        city = eashop['city']
        district = eashop['district']
        address = eashop['address']

        userName = eashop['userName']
        memo = str(eashop['memo'])
        status = str(eashop['status'])

        telephone = str(eashop['telephone'])
        if telephone == "":
            telephone = str(eashop['phoneNo'])
        
        eashopsev = thisdict['data']['services']
        servicesDict = dict()
        for oneByOne in eashopsev:
            ser_name = oneByOne['name']
            ser_price = oneByOne['price']
            servicesDict[ser_name] = ser_price
        
        servicesStr = str(servicesDict)

        strs = thisid + "," + province + "," + district + ","+ address + "," + userName + "," + name + "," + telephone + "," + servicesStr + "\n"

        print(strs)
        with open("./czh/yunnan.csv",'a', encoding='UTF-8') as ff:
            ff.write(strs)



