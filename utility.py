from sys import stderr
from time import time

# on my analysis of the webpage functionality
# I found that ajaxWDxy.js constantly requests and update the UI
# from the following path https://weerindelft.nl/clientraw.txt
# followed by the parameter Date.getTime()
# EXAMPLE: https://weerindelft.nl/clientraw.txt?1713279404355
# which is a text file that easily parsed

# just to log errors if needed
def fault(*args, **kwargs) -> None:
    return print(*args, file=stderr, **kwargs)

# simulates Date().getTime in Javascript
def now() -> int: return int(time() * 1000)