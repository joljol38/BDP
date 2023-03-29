import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

result = []

# seoul
for do in range(1, 26):
    Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=1&sido2=%d&txtsearch=' % do
    print(Kyochon_url)
    html = urllib.request.urlopen(Kyochon_url)
    soupKyochon = BeautifulSoup(html, 'html.parser')
    div = soupKyochon.find("div", {"class": "shopSchList"})
            
    for store in div.find_all('a'):
        store_name = store.find('strong').get_text()
        store_address = store.find('em').get_text().strip().split('\r')[0]
        store_sido = store_address.split()[0:2]
        result.append([store_name]+[store_sido]+[store_address])
# print(len(result))

# busan
for do in range(1, 17):
    Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=2&sido2=%d&txtsearch=' % do
    print(Kyochon_url)
    html = urllib.request.urlopen(Kyochon_url)
    soupKyochon = BeautifulSoup(html, 'html.parser')
    div = soupKyochon.find("div", {"class": "shopSchList"})
            
    for store in div.find_all('a'):
        store_name = store.find('strong').get_text()
        store_address = store.find('em').get_text().strip().split('\r')[0]
        store_sido = store_address.split()[0:2]
        result.append([store_name]+[store_sido]+[store_address])
# print(len(result))

# daegu
for do in range(1, 9):
    Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=3&sido2=%d&txtsearch=' % do
    print(Kyochon_url)
    html = urllib.request.urlopen(Kyochon_url)
    soupKyochon = BeautifulSoup(html, 'html.parser')
    div = soupKyochon.find("div", {"class": "shopSchList"})
            
    for store in div.find_all('a'): 
        store_name = store.find('strong').get_text()
        store_address = store.find('em').get_text().strip().split('\r')[0]
        store_sido = store_address.split()[0:2]
        result.append([store_name]+[store_sido]+[store_address])
# print(len(result))

# incheon
for do in range(1, 11):
    try :
        Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=4&sido2=%d&txtsearch=' % do
        print(Kyochon_url)
        html = urllib.request.urlopen(Kyochon_url)
        soupKyochon = BeautifulSoup(html, 'html.parser')
        div = soupKyochon.find("div", {"class": "shopSchList"})
            
        for store in div.find_all('a'):
            store_name = store.find('strong').get_text()
            store_address = store.find('em').get_text().strip().split('\r')[0]
            store_sido = store_address.split()[0:2]
            result.append([store_name]+[store_sido]+[store_address])
    except :
        pass
    
# print(len(result))

# gwangju
for do in range(1, 6):
    Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=5&sido2=%d&txtsearch=' % do
    print(Kyochon_url)
    html = urllib.request.urlopen(Kyochon_url)
    soupKyochon = BeautifulSoup(html, 'html.parser')
    div = soupKyochon.find("div", {"class": "shopSchList"})
            
    for store in div.find_all('a'):
        # if len(store) <= 3:
        #     break
        store_name = store.find('strong').get_text()
        store_address = store.find('em').get_text().strip().split('\r')[0]
        store_sido = store_address.split()[0:2]
        result.append([store_name]+[store_sido]+[store_address])
# print(len(result))

# daejeon
for do in range(1, 6):
    Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=6&sido2=%d&txtsearch=' % do
    print(Kyochon_url)
    html = urllib.request.urlopen(Kyochon_url)
    soupKyochon = BeautifulSoup(html, 'html.parser')
    div = soupKyochon.find("div", {"class": "shopSchList"})
            
    for store in div.find_all('a'):
        # if len(store) <= 3:
        #     break
        store_name = store.find('strong').get_text()
        store_address = store.find('em').get_text().strip().split('\r')[0]
        store_sido = store_address.split()[0:2]
        result.append([store_name]+[store_sido]+[store_address])
# print(len(result))

# ulsan
for do in range(1, 6):
    Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=7&sido2=%d&txtsearch=' % do
    print(Kyochon_url)
    html = urllib.request.urlopen(Kyochon_url)
    soupKyochon = BeautifulSoup(html, 'html.parser')
    div = soupKyochon.find("div", {"class": "shopSchList"})
            
    for store in div.find_all('a'):
        # if len(store) <= 3:
        #     break
        store_name = store.find('strong').get_text()
        store_address = store.find('em').get_text().strip().split('\r')[0]
        store_sido = store_address.split()[0:2]
        result.append([store_name]+[store_sido]+[store_address])
# print(len(result))

# sejong
for do in range(1, 17):
    try: 
        Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=8&sido2=%d&txtsearch=' % do
        print(Kyochon_url)
        html = urllib.request.urlopen(Kyochon_url)
        soupKyochon = BeautifulSoup(html, 'html.parser')
        div = soupKyochon.find("div", {"class": "shopSchList"})
            
        for store in div.find_all('a'):
            store_name = store.find('strong').get_text()
            store_address = store.find('em').get_text().strip().split('\r')[0]
            store_sido = store_address.split()[0:2]
            result.append([store_name]+[store_sido]+[store_address])
    except:
        pass   
# print(len(result))

# kyeonggi
for do in range(1, 45):
    Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=9&sido2=%d&txtsearch=' % do
    print(Kyochon_url)
    html = urllib.request.urlopen(Kyochon_url)
    soupKyochon = BeautifulSoup(html, 'html.parser')
    div = soupKyochon.find("div", {"class": "shopSchList"})
            
    for store in div.find_all('a'):
        # if len(store) <= 3:
        #     break
        store_name = store.find('strong').get_text()
        store_address = store.find('em').get_text().strip().split('\r')[0]
        store_sido = store_address.split()[0:2]
        result.append([store_name]+[store_sido]+[store_address])
# print(len(result))

# kangwon
for do in range(1, 19):
    try:
        Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=10&sido2=%d&txtsearch=' % do
        print(Kyochon_url)
        html = urllib.request.urlopen(Kyochon_url)
        soupKyochon = BeautifulSoup(html, 'html.parser')
        div = soupKyochon.find("div", {"class": "shopSchList"})
            
        for store in div.find_all('a'):
            store_name = store.find('strong').get_text()
            store_address = store.find('em').get_text().strip().split('\r')[0]
            store_sido = store_address.split()[0:2]
            result.append([store_name]+[store_sido]+[store_address])
    except:
        pass
# print(len(result))

# chungbuk
for do in range(1, 16):
    try: 
        Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=11&sido2=%d&txtsearch=' % do
        print(Kyochon_url)
        html = urllib.request.urlopen(Kyochon_url)
        soupKyochon = BeautifulSoup(html, 'html.parser')
        div = soupKyochon.find("div", {"class": "shopSchList"})
            
        for store in div.find_all('a'):
            store_name = store.find('strong').get_text()
            store_address = store.find('em').get_text().strip().split('\r')[0]
            store_sido = store_address.split()[0:2]
            result.append([store_name]+[store_sido]+[store_address])
    except :
        pass
# print(len(result))

# chungnam
for do in range(1, 18):
    try : 
        Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=12&sido2=%d&txtsearch=' % do
        print(Kyochon_url)
        html = urllib.request.urlopen(Kyochon_url)
        soupKyochon = BeautifulSoup(html, 'html.parser')
        div = soupKyochon.find("div", {"class": "shopSchList"})
            
        for store in div.find_all('a'):
            store_name = store.find('strong').get_text()
            store_address = store.find('em').get_text().strip().split('\r')[0]
            store_sido = store_address.split()[0:2]
            result.append([store_name]+[store_sido]+[store_address])
    except :
        pass
# print(len(result))

# jeonbuk
for do in range(1, 16):
    Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=13&sido2=%d&txtsearch=' % do
    print(Kyochon_url)
    html = urllib.request.urlopen(Kyochon_url)
    soupKyochon = BeautifulSoup(html, 'html.parser')
    div = soupKyochon.find("div", {"class": "shopSchList"})
            
    for store in div.find_all('a'):
        # if len(store) <= 3:
        #     break
        store_name = store.find('strong').get_text()
        store_address = store.find('em').get_text().strip().split('\r')[0]
        store_sido = store_address.split()[0:2]
        result.append([store_name]+[store_sido]+[store_address])
# print(len(result))

# jeonnam
for do in range(1, 23):
    try :
        Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=14&sido2=%d&txtsearch=' % do
        print(Kyochon_url)
        html = urllib.request.urlopen(Kyochon_url)
        soupKyochon = BeautifulSoup(html, 'html.parser')
        div = soupKyochon.find("div", {"class": "shopSchList"})
            
        for store in div.find_all('a'):
            store_name = store.find('strong').get_text()
            store_address = store.find('em').get_text().strip().split('\r')[0]
            store_sido = store_address.split()[0:2]
            result.append([store_name]+[store_sido]+[store_address])
    except :
        pass
# print(len(result))

# kyeonbuk
for do in range(1, 25):
    try:
        Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=15&sido2=%d&txtsearch=' % do
        print(Kyochon_url)
        html = urllib.request.urlopen(Kyochon_url)
        soupKyochon = BeautifulSoup(html, 'html.parser')
        div = soupKyochon.find("div", {"class": "shopSchList"})
            
        for store in div.find_all('a'):
        
            store_name = store.find('strong').get_text()
            store_address = store.find('em').get_text().strip().split('\r')[0]
            store_sido = store_address.split()[0:2]
            result.append([store_name]+[store_sido]+[store_address])
    except :
        pass
# print(len(result))

# keyongnam
for do in range(1, 23):
    Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=16&sido2=%d&txtsearch=' % do
    print(Kyochon_url)
    html = urllib.request.urlopen(Kyochon_url)
    soupKyochon = BeautifulSoup(html, 'html.parser')
    div = soupKyochon.find("div", {"class": "shopSchList"})
            
    for store in div.find_all('a'):
        # if len(store) <= 3:
        #     break
        store_name = store.find('strong').get_text()
        store_address = store.find('em').get_text().strip().split('\r')[0]
        store_sido = store_address.split()[0:2]
        result.append([store_name]+[store_sido]+[store_address])
# print(len(result))

# jeju
for do in range(1, 3):
    Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=17&sido2=%d&txtsearch=' % do
    print(Kyochon_url)
    html = urllib.request.urlopen(Kyochon_url)
    soupKyochon = BeautifulSoup(html, 'html.parser')
    div = soupKyochon.find("div", {"class": "shopSchList"})
            
    for store in div.find_all('a'):
        # if len(store) <= 3:
        #     break
        store_name = store.find('strong').get_text()
        store_address = store.find('em').get_text().strip().split('\r')[0]
        store_sido = store_address.split()[0:2]
        result.append([store_name]+[store_sido]+[store_address])
# print(len(result))

kyochon_tbl_seoul = pd.DataFrame(result, columns = ('store', 'sidogu', 'address'))
# kyochon_tbl_seoul
df1 = kyochon_tbl_seoul.explode('sidogu')
# df1
df2 = df1.iloc[::2,:]
# df2
df3 = df1.iloc[1::2,:]
# df3
merge = pd.concat([df2,df3],axis=1)
# merge
df4 = merge.iloc[:,[0,1,2,4]]
# df4
df4.columns = ['store','sido','address','gu']
# df4 = df4[['store', 'sido', 'gu', 'address']]
# df4
df4 = df4[['store', 'sido', 'gu', 'address']]
# df4
df4.to_csv('kyochon.csv')
