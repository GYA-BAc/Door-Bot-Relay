"""
The bot reciever, meant to connect to the hoster
"""

# frequency to check for ping
CHECK_INTERVAL = 5 # seconds

import requests
import time

from env import EXTERNAL_URL

# compare this number to the one on the server,
# if the server is greater, then there was a new ping
current_pings = 0

if __name__ == "__main__":

    while True:
        time.sleep(CHECK_INTERVAL)

        if (int(requests.get(EXTERNAL_URL).text) > current_pings):
            # print(requests.get(EXTERNAL_URL).text)
            current_pings += 1

            # do stuff here

# print(requests.get(EXTERNAL_URL).text)