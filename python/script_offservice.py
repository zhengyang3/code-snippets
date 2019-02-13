import mitmproxy
import json

def response(flow):
    url = 'http://118.178.94.180/shop/api/v1/product/search'
    if flow.request.url.startswith(url):
        with open("offservice.txt","ab+") as f:
                f.write(flow.response.content + b"\n")
                f.close()
