from requests import get , ConnectionError
from sys import stderr
from time import time

# on my analysis of the webpage functionality
# I found that ajaxWDxy.js constantly requests and update the UI
# from the following path https://weerindelft.nl/clientraw.txt
# followed by the JavaScript function output Date.getTime()
# EXAMPLE: https://weerindelft.nl/clientraw.txt?1713279404355
# which is a text file that is easily parsed

def fault(*args, **kwargs) -> None:
# output to standard character error
    return print(*args, file=stderr, **kwargs)

# simulates Date().getTime in Javascript
def now() -> int: return int(time() * 1000)


URL = 'https://weerindelft.nl/clientraw.txt'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'

def get_temperature() -> int:
    # sometime balance-loaders and firewalls block python as a user-agent
    headers = {"User-agent": USER_AGENT}
    # simulate the interactive frontend behavior
    
    try: response = get(URL + '?' + str(now()), headers = headers).text
    except ConnectionError:
        fault("(!) Failed Connecting to weerindelft.nl Service")
        return None
    
    # attempt to parse the response
    try: return round(float(response.split(' ')[46]))
    except (ValueError, IndexError):
        fault("(!) Failed to Parse Respone:")
        fault("-----"*2 + "BEGIN RESPONE" + "-----"*2)
        fault(response)
        fault("-----"*2 + "END RESPONE" + "-----"*2)
        return None


if __name__ == '__main__':
    temp = get_temperature()
    if temp == None : exit(1)
    print(temp,'degrees Celsius')