import requests
import bs4
import time

print('''
# Python DomainScraper Alfa version 1
# BY 1337FARHAN & MSRBQ
# All rights reserved to the owners of the script
# Contact jx@outlook.cl for furhter information
# Note: the number of results is based on a search engine and might not be 100% accurate.
#       you can increase the limit to make sure all actual results have been scraped.
''')

time.sleep(3)

# Base URL
Bing = 'http://bing.com/search'

# Find desired URLs
urls = []


def lookup(div):

    for _ in div:
        url = _.find('cite')
        urls.append(url.text)
    return urls

def domainFilter(urls):
    _urls = []

    for url in urls:
        url = url.split('/', 3)
        try:
            if url[2]:
                _url = url[2]
        except:
            _url = url[0]
        _urls.append(_url)
    urls = set(_urls[:])
    return urls;

def fileSave(save):
    global urls
    _urls = domainFilter(urls)
    with open('Output.txt', 'w') as outfile:
        if save is True:
            for url in _urls:
                outfile.writelines(url + '\n')
        else:
            for url in _urls:
                print(url)


# Building the request for each call


def Req(ip: str, save: bool, first=0, limit=150):
    count = 50

    # Create the request and get the response
    _params = {'q': f'ip:{ip} | ip:{ip}', 'responseFilter': 'Webpages',
               'count': f'{count}', 'first': f'{first}'}

    r = requests.get(Bing, params=_params)

    # Parsing the source code
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    div = soup.findAll('div', {'class': 'b_attribution'})

    if first < limit:
        lookup(div)
        first = first + count
        Req(ip, save, first, limit)

    else:
        fileSave(save)


ip = input('IP: ').strip()
_limit = int(input('Number of limit (Must be a multiple of 50): ').strip())
_save = input('Save to output.txt - Y/n? ').strip()

if _save.lower() == 'y':
    _save = True
else:
    _save = False

Req(ip, _save, 0, limit=_limit)
