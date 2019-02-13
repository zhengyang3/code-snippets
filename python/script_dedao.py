from mitmproxy import ctx
import json

def response(flow):
    info = ctx.log.info
    url = 'https://m.igetget.com/hybrid/api/ebook/list'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        books = data.get('data')
        for book in books:
            info(str(book))
