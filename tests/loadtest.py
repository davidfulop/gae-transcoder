import time
import requests
import threading
from datetime import datetime

URL = 'https://transcoder-dot-media-test-1275.appspot.com'
PROJECT_ID = 'media-test-1275'
NUM_REQUESTS = 1
DELAY=.5

def download_file(i):
    startTime = datetime.now()
    print("Starting request # " + str(i) + " at " + str(startTime.time()) + "\n")
    requests.get(URL)
    endTime = datetime.now()
    duration = endTime - startTime
    print("Finished request # " + str(i) + " at " + str(endTime.time()) + " in " + str(duration) + "\n")

for i in range(0, NUM_REQUESTS):
    threading.Thread(target=download_file, args=[i]).start()
    time.sleep(DELAY)
