import requests
import re

image = "https://cf.shopee.sg/file/f59349a86c923acc3cbd00e1b24350f2_tn&quot"

r = requests.get(image, allow_redirects=True)

open(re.escape(image), 'wb').write(r.content)

