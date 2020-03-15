
import requests
from bs4 import BeautifulSoup
import re


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/79.0.3945.88 Safari/537.36 "
}
url = 'https://www.taobao.com/market/nvzhuang/yurong.php?spm=a21bo.7723600.8224.2.35dc5ec9kDY4HJ'
url2 = 'https://www.taobao.com/market/nvxie/citiao/index.php?spm=a21bo.7723600.8555.1.3f975ec9oG9Xg3'
url3 = 'https://world.taobao.com'
url4 = 'https://www.taobao.com/market/nvxie/citiao/index.php?spm=a21bo.7723600.8555.1.3f975ec9oG9Xg3'
url5 = 'https://www.taobao.com/market/nanxie/citiao/shangwu.php?spm=a21bo.7723600.8555.148.3f975ec9oG9Xg3&pvid=80c850a1-c5b0-40bb-8aa1-4f9a15662f53&scm=1007.11287.5866.100200300000000'
url6 = 'https://s.taobao.com/list?spm=a21bo.7723600.8555.39.3f975ec9oG9Xg3&nofestival=0&q=厚底&bcoffset=&tab=all&loc=&sort=&source=&style=grid&bucket_id=&filter=&cat=50340023&sortn=&sort2=&fs=1&seller_type=taobao&nocombo=&oeid=&v=auction&cps=yes&rsclick=&stats_click=&cd=false&olu=yes'
url7 = 'https://s.taobao.com/search?spm=a21wu.241046-global.6977698868.122.41cab6cbX5Tv4m&q=男鞋&acm=lb-zebra-241046-2058600.1003.4.1797247&scm=1003.4.lb-zebra-241046-2058600.OTHER_14950684615043_1797247'
url8 = 'https://s.taobao.com/search?spm=a21wu.241046-global.6977698868.162.41cab6cbX5Tv4m&q=饰品配件&acm=lb-zebra-241046-2058600.1003.4.1797247&scm=1003.4.lb-zebra-241046-2058600.OTHER_14950680767554_1797247&cps=yes&ppath=20000%3A56080308'

resp = requests.get("get",url4,headers=headers)
html = resp.text
print(html)
# soup = BeautifulSoup(html,'html5lib')
# aling = soup.find('div',class_='scrollable-content')
#
# print(aling)

