import requests
import bs4
import keyboard

# Python DomainScraper Alfa version 1
# BY 1337FARHAN & MSRBQ
# All rights reserved to the owners of the script
# Contact jx@outlook.cl for furhter information



# Base URL
Bing = 'http://bing.com/search'

# To save the URLs
urls = []

# Find desired URLs
def lookup(div):
    for _ in div:
        url = _.find('cite')
        urls.append(url.text)
    return urls

# Loop through Bing pages for more results
def checker(ip: str, first, limit):
    count = 50

    # Create the request and get the response
    _params = {'q': f'ip:{ip} | ip:{ip}', 'responseFilter' : 'Webpages', 'count' : f'{count}', 'first' : f'{first}'}
    
    # _params = {'q': f'ip:{ip} | ip:{ip}', 'responseFilter' : 'Webpages', 'count' : f'{count}', 'first' : f'{first}'}
    #      " | " is used to force Bing to a spicific IP, 
    #      "responseFilter" to get only the webpages and make the job easier, 
    #      "count" the number of results per page {Maximum:50},
    #      "first" the anchor {where to start the search} ex. first=50 will skip the first 50 results and give the response {No maximum}

    r = requests.get(Bing, params= _params)

    # Parsing the source code
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    div = soup.findAll('div', {'class':'b_attribution'})

    # In case if the page is empty
    if not div:
        print(urls)
        print('Could not find anymore results.')
        exit()
    # Print results when the user limit is reached
    if first < limit:
        lookup(div)
        first = first + count
        checker(ip, first, limit)
    else:
        print(urls)
        exit()

    
ip = input('IP: ')
_limit = int(input('Number of limit (Must be a multiple of 50): '))

checker(ip, 0, limit=_limit)


