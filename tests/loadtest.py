import time
import requests
import threading

URL = 'https://transcoder-dot-media-test-1275.appspot.com'
PROJECT_ID = 'media-test-1275'
NUM_REQUESTS = 100 
DELAY=.1

def download_file(i):
    print("Starting request # " + str(i) + "\n")
    requests.get(URL)
    print("Finished request # " + str(i) + "\n")

for i in range(0, NUM_REQUESTS):
    threading.Thread(target=download_file, args=[i]).start()
    time.sleep(DELAY)
