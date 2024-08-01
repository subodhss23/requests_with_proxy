import requests
import random

timeout_in_seconds = 10

# list of proxy servers from US that has uptime of 100%
url = "https://proxylist.geonode.com/api/proxy-list?country=US&filterUpTime=100&limit=500&page=1&sort_by=lastChecked&sort_type=desc"
response = requests.get(url)
response_data = response.json()

# dictionary to store proxy IPs and ports
proxies_dict = {}
for item in response_data['data']:
    proxies_dict[item['ip']] = item['port']
# print(proxies_dict)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

# Example of a header more advanced set of HTTP headers
advanced_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
    "Te": "trailers",
    "Connection": "keep-alive"
}

# a list of proxies in the format required by requests
proxies_list_http = [{"http": f"http://{ip}:{port}" }for ip, port in proxies_dict.items()]

# Select a random proxy from the list
selected_proxy = random.choice(proxies_list_http)

# URL to send the request to <replace the URL of your choice>
url = "https://news.ycombinator.com/news"
try:
    response = requests.get(url, headers=headers, proxies=selected_proxy)
    print(response.status_code)
    print(response.text)
except Exception as error:
    print("An error has occured")
    print(error)