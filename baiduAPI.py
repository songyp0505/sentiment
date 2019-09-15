import requests
import json

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like 09	Gecko) Chrome/55.0.2883.87 Safari/537.36'
 }
def get_token():
    ak = '8ZoGkIcx4LgIQUP3prRq0IM8'
    sk = 'ZNoGpX6MvPPc9G1szNZahnRvwQ9aDGyV'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(ak,sk)
    r = requests.get(host,headers=headers)
    r.encoding=r.apparent_encoding

def QGFX():
    access_token = "24.e477ef9a648d7fe36eae589de1353323.2592000.1571100179.282335-17247392"
    url_1 = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token='+str(access_token)
    url_2 =  'https://aip.baidubce.com/rpc/2.0/nlp/v2/comment_tag?charset=UTF-8&access_token='+str(access_token)
    data = {
        'text':"我爱你"
    }

    data = json.dumps(data)
    sentiment = requests.post(url_1, data)
    i = json.loads(sentiment.text)
    print(i['items'][0]['positive_prob'])

QGFX()
