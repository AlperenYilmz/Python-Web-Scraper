import requests
from bs4 import BeautifulSoup

url = 'https://www.classcentral.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
reqs = requests.get(url, headers=headers)
soup = BeautifulSoup(reqs.content, 'html.parser')

subpages=[]
for link in soup.find_all("a"):
    data=link.get('href')
    if data not in subpages:
        subpages.append(data)
    else:
        continue

subpages_copy=[]

for sbpg in subpages:
    if sbpg.startswith('/'):
        sbpg=url+sbpg
        subpages_copy.append(sbpg)
    else:
        subpages_copy.append(sbpg)

with open(r'C:/Users/alper/Documents/PycharmProjects/CodingAllstars/linkos.txt', 'w') as fp:
    for el in subpages_copy:
        fp.write(el+"\n")