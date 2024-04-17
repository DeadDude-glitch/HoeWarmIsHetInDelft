#!/usr/bin/env python3
from requests import get , ConnectionError
from sys import stderr
from time import time
from datetime import datetime

"""
on my analysis of the webpage functionality
The webpage frontend updates itself with a periodic 
GET requests to /clientraw.txt followed by JavaScript function Date.getTime()
EXAMPLE: GET https://weerindelft.nl/clientraw.txt?1713279404355
"""

URL = 'https://weerindelft.nl/clientraw.txt?'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'

def logError(*args, **kwargs) -> None:
    # output to standard character error
    return print(datetime.now(),*args, file=stderr, **kwargs)

def getTime() -> int: 
    # simulates Date().getTime() in Javascript
    return int(time() * 1000)

def validateWeather(data:list) -> bool:
    # ensure client rawdata data format follows https://linyweather.net/plugins/wdParser/index.php
    return (data[ 0]  == '12345' and 
            data[-1]  == '!!C10.37S143!!' and 
            len(data) == 178)


def get_temperature(url:str) -> float:
    # sometime balance-loaders and firewalls block python as a user-agent
    # simulate the interactive frontend behavior and avoid triggering detection rules
    
    headers = {"User-agent": USER_AGENT}
    url += str(getTime())
    
    try: 
        response = get(url, headers = headers)
        if response.status_code != 200: raise ConnectionError
        data = response.text.split()
        if validateWeather(data): return float(data[4])

    except ConnectionError:
        logError("Uable to request", url)
    
    except (ValueError, IndexError):
        logError(f'Invalid weather data {response.text}')
    
    return None


if __name__ == '__main__':
    temp = get_temperature(URL)
    if temp == None : exit(1)
    print(round(temp),'degrees Celsius')