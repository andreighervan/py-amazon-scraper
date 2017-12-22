import os

current_dir = os.path.dirname(os.path.realpath(__file__))

# Database
database = "amazon_crawler"
host = "localhost"
user = "postgres"
password = "123QQsuccess"

# Redis
redis_host = "localhost"
redis_port = 6379
redis_db = 0

# Request
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
}
allowed_params = ["node", "rh", "page"]

# Proxies

proxies = [
    "13.78.125.167:8080",
    "46.254.203.15:8080",
    "192.116.142.153:8080",
    "178.49.136.84:8080",
    "89.22.175.43:8080",
    "171.97.80.22:8080",
    "200.117.239.89:8080"

    # check out https://proxybonanza.com/?aff_id=629
    # for a quick, easy-to-use proxy service
]

# Crawling Logic
start_file = os.path.join(current_dir, "start-urls.txt")
max_requests = 2 * 10 ** 6  # two million
max_details_per_listing = 9999

# Threads
max_threads = 200

# Logging & Storage
log_stdout = True
image_dir = "/tmp/crawl_images"
export_dir = "/tmp"
