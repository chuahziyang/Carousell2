import json
import re
import os



class product():
    def __init__(self, Description, Title,Price, link):
        self.desc = Description
        self.title = Title
        self.price = Price
        links = []
        for i in link:
            match = re.search("&quot;(.*tn&quot)",i["name"])
        self.link = links


with open('run_results.json',encoding="utf8") as json_file:
    data = json.load(json_file)
    print(data)

    os.chdir("../Files")

    for i in data['list1']:
        item = product(i["Description"],"Placeholder", i["selection2"], i["selection1"])
        os.mkdir(item.title)
        for image in item.link:
            pass