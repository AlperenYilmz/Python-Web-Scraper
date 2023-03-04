import requests, os, time
from pathlib import Path


filename = 'linkos.txt'
try:
    with open(filename, 'r') as file:
        urls = file.readlines()
except FileNotFoundError:
    print(f"Error: The file {filename} does not exist.")
    exit()

for url in urls:
    url = url.strip()    # remove whitespaces
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()    # raise HTTPError for unsuccessful response
    except requests.exceptions.RequestException as err:
        print(f"Error: Unable to download {url}. Exception: {err}")
        continue        # skip URL if an error occurs

    html_content = response.text
    
    try:      # saving HTML content
        directory = 'html_files'
        Path(directory).mkdir(exist_ok=True)
        
        url=url.split("//")[-1]   # this removes https:// part of URL
        url_parts = url.split('/')
        for part_index in range(len(url_parts)-1):    # make directories until the final html file
            directory = os.path.join(directory, url_parts[part_index])
            Path(directory).mkdir(exist_ok=True)

        with open(f'{directory}{os.path.sep}{url_parts[-1]}.html', 'w+', encoding='utf-16') as outfile:
            outfile.write(html_content)
    except IOError:
        print(f"Error: Unable to write {url} content to file.")
    
    time.sleep(2)         # introduce a delay of 2 second between requests to avoid 403 error