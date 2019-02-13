from mitmproxy import ctx
import codecs
import json

def response(flow):
    info = ctx.log.info
    url = 'https://api.farfetch.net/v1/search/products'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        #with codecs.open("farfetch.txt","a+",'utf-8') as f:
        with open("farfetch0.txt","a+") as f:
            entries = data.get("products").get("entries")
            for entry in entries:
                f.write(json.dumps(entry.get("id")) + ", ")
            f.close()
