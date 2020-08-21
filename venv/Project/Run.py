import json
import re
import os

import requests

def remove(string):
    return string.translate(str.maketrans({"\\": r"\\",
                                           "/": ""}))

class product():
    def __init__(self, Description, Title,Price, link):
        self.desc = Description
        self.title = Title
        self.price = Price
        links = []
        for i in link:
            match = re.search("&quot;(.*tn&quot)",i["name"])
            links.append(match.group(1))
        self.link = links
        print(self.link)


with open('run_results_new.json',encoding="utf8") as json_file:
    data = json.load(json_file)
    print(data)

    os.chdir("../Files")

    for i in data['list1']:
        item = product(i["Description"],i["Title"], i["selection2"], i["selection1"])
        os.mkdir(remove(item.title))
        print(os.getcwd())
        os.chdir(remove(item.title))
        i = 0
        for image in item.link:
            print(image)
            r = requests.get(image, allow_redirects=True)
            open(str(i), 'wb').write(r.content)
            i += 1

        os.chdir("../")
        print(os.getcwd())

