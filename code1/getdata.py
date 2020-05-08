import json


with open("./city.json",'r', encoding='UTF-8') as load_f:
    load_dict = json.load(load_f)
UrlList = []
all_data = load_dict["keys"]
for prov in all_data:
    prov_id = prov["id"]
    prov_name = prov["value"]
    prov_childs = prov["childs"]
    # print(prov_id,prov_name,prov_childs)

    for city in prov_childs:
        city_id = city["id"]
        city_name = city["value"]
        city_childs = city["childs"]
        str = prov_name + ',' + city_name + '\n'
        print(str)
        with open("./china/cdd_city.csv",'a', encoding='UTF-8') as ff:
            ff.write(str)
        # print(city_id,city_name,city_childs)
        # for dispart in city_childs:
        #     dispart_id = dispart["id"]
        #     dispart_name = dispart["value"]
        #     dispart_parentsid = dispart["parentId"]
        #     print(prov_name,city_name,city_id,dispart_name,dispart_id,dispart_parentsid)
