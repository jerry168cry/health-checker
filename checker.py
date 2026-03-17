import urllib.request
import urllib.error
import time

# List of public APIs to test
API_ENDPOINTS = [
    "https://api.github.com",
    "https://pokeapi.co/api/v2/",
    "https://jsonplaceholder.typicode.com/posts/1"
]

def check_api_status(url):
    try:
        start_time = time.time()
        # Pretend to be a normal browser
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=5)
        latency = round((time.time() - start_time) * 1000, 2)
        
        if response.getcode() == 200:
            print(f"[SUCCESS] {url} is online. Latency: {latency}ms")
        else:
            print(f"[WARNING] {url} returned status code {response.getcode()}")
            
    except urllib.error.URLError as e:
        print(f"[ERROR] Failed to connect to {url}. Reason: {e.reason}")

if __name__ == "__main__":
    print("--- Starting API Health Check ---")
    for api in API_ENDPOINTS:
        check_api_status(api)
    print("--- Check Completed ---")
