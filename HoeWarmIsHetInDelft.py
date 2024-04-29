#!/usr/bin/env python3
from requests import get , ConnectionError
from sys import stderr
from time import time
from datetime import datetime
from validators import url

"""
the webpage frontend updates itself with a periodic GET requests 
to /clientraw.txt followed by JavaScript function Date.getTime()
EXAMPLE: GET https://weerindelft.nl/clientraw.txt?1713279404355
"""

URL = 'https://weerindelft.nl/clientraw.txt'

""" 
    * Weather display functions names should follow the syntax [action]_wd_[object]
    * Variables names follow the syntax wd_[object]
    * Variables names should be the same across all functions to implicitly denote usability 
"""


def logError(*args, **kwargs) -> None:
    return print(datetime.now(), *args, file=stderr, **kwargs)



def getTime() -> int: 
    # simulates Date().getTime() in Javascript
    return int(time() * 1000)



def request_wd_data(wd_url:str) -> str :

    # get the weather display data from web-server
    
    if not url(wd_url): 
        raise ValueError("Invalid URL")
        
    # avoid triggering detection rules over python user-agent header
    
    wd_url = wd_url.split('?')[0]
    #wd_url += '?' + str(getTime()) # simulate the interactive frontend behavior 
    headers = {"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
 
    response = get(wd_url, headers = headers)
    if response.status_code != 200: 
        raise ConnectionError("Uable to request " + wd_url)
    
    return response.text



def validate_wd_data(wd_data:str) -> bool:
    
    # ensure client rawdata data format follows clientraw format 
    # for more details: https://linyweather.net/plugins/wdParser/index.php

    try: 
        data = wd_data.split()
        return (data[ 0]  == '12345' and 
                data[-1]  == '!!C10.37S143!!' and 
                len(data) ==  178)

    except (ValueError, IndexError):
        logError('Invalid weather data', rawdata)
    
    return False



def get_wd_temperature(wd_data:str) -> float:
    
    # given valid WD data in clientraw format returns temperature

    wd_data = wd_data.split()
    return float(wd_data[4])
    



if __name__ == '__main__':

    def main (wd_url:str) -> int:

        # driver code of the script

        data = request_wd_data(wd_url)
        if not validate_wd_data(data): exit(1)
        temp = get_wd_temperature(data)

        print(round(temp),'degrees Celsius')
        return 0
    
    main(URL)
