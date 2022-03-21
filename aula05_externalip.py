import json
from urllib.request import urlopen

if __name__ == '__main__':
    url = 'https://ipinfo.io/json'
    rspns = urlopen(url)
    dtrcv = json.load(rspns)
    ip = dtrcv['ip']
    city = dtrcv['city']
    cntry = dtrcv['country']
    print('External IP details:')
    print(f'IP: {ip}\nCity: {city}\nCountry: {cntry}')
