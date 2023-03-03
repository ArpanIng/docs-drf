import requests

url_endpoint = "https://httpbin.org/status/200"
url_endpoint = "https://httpbin.org/anything"

response = requests.get(url=url_endpoint, data={"hello": "world"})
print(response.text)
print(response.json())

# {
#     "args": {},
#     "data": "",
#     "files": {},
#     "form": {},
#     "headers": {
#         "Accept": "*/*",
#         "Accept-Encoding": "gzip, deflate",
#         "Host": "httpbin.org",
#         "User-Agent": "python-requests/2.28.2",
#         "X-Amzn-Trace-Id": "Root=1-6400c340-7e200e7e65fb54e615aff531",
#     },
#     "json": null,
#     "method": "GET",
#     "origin": "27.34.54.45",
#     "url": "https://httpbin.org/anything",
# }

{
    "args": {},
    "data": "",
    "files": {},
    "form": {},
    "headers": {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Host": "httpbin.org",
        "User-Agent": "python-requests/2.28.2",
        "X-Amzn-Trace-Id": "Root=1-6400c155-637c68dd5c7e3563174f727f",
    },
    "json": None,
    "method": "GET",
    "origin": "27.34.54.45",
    "url": "https://httpbin.org/anything",
}
