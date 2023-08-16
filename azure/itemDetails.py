import logging
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def concurrentRequests(headers:dict, urls:list[str],cb):
    THREAD_POOL = 20
    session = requests.Session()
    session.mount(
        'https://',
        requests.adapters.HTTPAdapter(pool_maxsize=THREAD_POOL,
                                    max_retries=3,
                                    pool_block=True)
    )
    
    def get(url):
        response = session.get(url,headers=headers)
        logging.debug("request was completed in %s seconds [%s]", response.elapsed.total_seconds(), response.url)
        if response.status_code != 200:
            logging.error("request failed, error code %s [%s]", response.status_code, response.url)
        if 500 <= response.status_code < 600:
            # server is overloaded? give it a break
            time.sleep(5)
        return response
    
    def process(urls):
        with ThreadPoolExecutor(max_workers=THREAD_POOL) as executor:
            # wrap in a list() to wait for all requests to complete
            for response in list(executor.map(get, urls)):
                if response.status_code == 200:
                    cb(response.json())
    
     
    process(urls)