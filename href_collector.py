import requests
from bs4 import BeautifulSoup

url = 'https://www.classcentral.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
reqs = requests.get(url, headers=headers)
soup = BeautifulSoup(reqs.content, 'html.parser')

subpages=[]   # creating a list for relative urls

for link in soup.find_all("a"):   # finding links in relative urls
    data=link.get('href')
    if data not in subpages:    # checking for duplications
        subpages.append(data)
    else:
        continue

subpages_copy=[]    # creating final list for relative+absolute urls

for sbpg in subpages:
    if sbpg.startswith('/'):   # checking if the url is relative url, which starts with "/", else, copy it as it is
        sbpg=url+sbpg
        subpages_copy.append(sbpg)
    else:
        subpages_copy.append(sbpg)

with open(r'C:/Users/alper/Documents/PycharmProjects/CodingAllstars/linkos.txt', 'w') as fp:   # path can be changed as demanded
    for el in subpages_copy:
        fp.write(el+"\n")
