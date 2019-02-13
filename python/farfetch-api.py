import requests
import json
import time

real_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IkE3MEFCRTNBNEFBQzIxQzY5MjEwNjdEMkQ3MEFEQUY1MjMwMzUwOUUiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJwd3EtT2txc0ljYVNFR2ZTMXdyYTlTTURVSjQifQ.eyJuYmYiOjE1NDk5NDM3MzgsImV4cCI6MTU0OTk0NDkzOCwiaXNzIjoiaHR0cDovL2ZhcmZldGNoLmNvbSIsImF1ZCI6WyJodHRwOi8vZmFyZmV0Y2guY29tL3Jlc291cmNlcyIsImFwaSJdLCJjbGllbnRfaWQiOiJDRjkzRDhGNEFGMzI0N0Y1OTRENUE5MTRBMjYxRDQwNyIsImNsaWVudF91aWQiOiIxMDAwNCIsImNsaWVudF90ZW5hbnRJZCI6IjEwMDAwIiwiY2xpZW50X2d1ZXN0IjoiMTI3OTg1MTU2Iiwic2NvcGUiOlsiYXBpIl19.RM6IJYjYl5-d_jn-zoVOdKYVB9ii46o4bX4ya2Mf5V7aMAa7gmPtmqXCwbiPj5VqFc3Fl6m0b5NGd-JPQyYjYvEFy8xkrc3dXqrjB9dbjLCn37kD3ZOH-0iJfor0WeGD80q0GmKpT5gpQN-A1vu4ySpRXb51emd4IV0jSncbdZ18GbJvF-KAu7aXSv72kVfonv9KI9awQf84Lk0V04wq8-3TdZj7JiqMfjHVxwPMYAObUPm1n1l0el2b8G5rPD325lLgaInRBVc55XW1ZdcSdTAEPkPVIJAUT4EUfbHloZlEz0BHpStQiLKjk3HikJe7XE59rY1X-7_MMDBNuJ1tBg"

headers = {
        'Authorization': 'Bearer '+real_token,
        'Cache-Control': 'no-cache, no-store',
        'FF-Country': 'IT',
        'FF-Currency': 'EUR',
        'Accept-Language': 'it-IT',
        'User-Agent': 'Farfetch/2.5.8 (OPPO OPPO R9s; Android 6.0.1; Scale/3.00)',
        'X-FFBenefits': "",
        'Host': 'api.farfetch.net',
        'Accept-Encoding': 'gzip',
        'X-NewRelic-ID': 'VQUCV1ZUGwEFUFhWBQAC',
        'Connection': 'keep-alive'
        }

headers2 = {
        'Accept-Language':'it_IT',
        'User-Agent':'Farfetch/2.5.8 (OPPO OPPO R9s; Android 6.0.1; Scale/3.00)',
        'X-Castle-Client-Id':'2b0c01f9-251b-46c8-8bd7-0c92dc580c37',
        'Content-Type':'application/x-www-form-urlencoded',
        'Content-Length':'151',
        'Host':'api.farfetch.net',
        'Connection':'Keep-Alive',
        'Accept-Encoding':'gzip',
        'X-NewRelic-ID':'VQUCV1ZUGwEFUFhWBQAC'
        }

token_body = {
        'grant_type':'client_credentials',
        'scope':'api',
        'client_id':'CF93D8F4AF3247F594D5A914A261D407',
        'client_secret':'B0C1BB6BAEA941549D410D1387E769D2',
        'GuestUserId':'127985156'
        }

#r2 = requests.post("https://api.farfetch.net/ext/auth/connect/token", data=token_body, headers=headers2)
#code = r2.status_code
#print(code)
#tmp2 = r2.json()
#access_token = tmp2.get('access_token')
#print(access_token)
#time.sleep(100)

json_data = open('farfetch0.txt','rb').read()
data = json.loads(json_data)
for goodid in data:
    print(goodid)
    r =requests.get("https://api.farfetch.net/v1/products/"+goodid , headers=headers)
    code = r.status_code
    if code == 401:
        print("401 ======")
        r2 = requests.post("https://api.farfetch.net/ext/auth/connect/token", data=token_body, headers=headers2)
        code2 = r2.status_code
        print("get token status is :"+str(code2))
        tmp2 = r2.json()
        real_token = tmp2.get('access_token')
        headers["Authorization"] = 'Bearer '+real_token
        print("token in new header is:"+headers.get('Authorization'))
        r =requests.get("https://api.farfetch.net/v1/products/"+goodid , headers=headers)
    tmp = r.json()
    result = {
            "brandStyleId":tmp.get('brandStyleId'),
            "variants":tmp.get('variants')
            }
    #with codecs.open("farfetch.txt","a+",'utf-8') as f:
    with open("farfetch.txt","a+") as f:
        #jsonStr = json.dumps(dict(result))
        jsonStr = json.dumps(result)
        f.write(jsonStr)
        f.write(",\n")
        f.close()
        #time.sleep(0.2)
