import json
import sys
import requests
from bs4 import BeautifulSoup
import url_list
import getopt

opts, args = getopt.getopt(sys.argv[1:], 'o:l:v:', ['output=', 'language=', 'variant=', 'http-proxy='])

lang = 'en'
proxy = None
output = 'result.json'
variant = None

for opt, optval in opts:
    if opt in ('-o', '--output'):
        output = optval
    elif opt == '--http-proxy':
        proxy = optval
    elif opt in ('-l', '--language'):
        lang = optval.lower()
    elif opt in ('-v', '--variant'):
        variant = optval

urls = url_list.get(lang, variant)

f = open(output, 'w')

codes = []

for url in urls:
    print('Fetching', url)
    rsp = requests.get(url, proxies={
        'http': proxy,
        'https': proxy,
    })
    result = json.loads(rsp.text)
    soup = BeautifulSoup(result['parse']['text']['*'], features='html.parser')

    for tr in soup.find('table', {'class': 'wikitable'}).find_all('tr', {'class': None}):
        vals = tr.find_all('td')
        row = []
        for val in vals:
            try:
                if val.contents[0] is not None:
                    text = val.contents[0]
                    try:
                        text = text.text
                    except AttributeError:
                        text = text.strip()
                    finally:
                        text = text.strip()
                else:
                    text = val.text.strip()
            except IndexError:
                text = val.text.strip()

            if len(text) > 0:
                row.append(text)
            else:
                row.append(None)
        if len(row) > 0:
            codes.append(row)

result = []
for airport in codes:
    result.append({
        'iata_code': airport[0],
        'icao_code': airport[1],
        'name': airport[2],
        'location': airport[3]
    })
f.write(json.dumps(result, indent=4))
f.close()

print('Result saved as {}'.format(output))
