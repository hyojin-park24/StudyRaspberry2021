import urllib.request as urq
import urllib.parse as uparse
import datetime
import json

class naverSearch(object):
    #생성자
    def __init__(self):
        print('Naver Search API 생성')

    # 네이버 API 요청함수
    def getRequestUrl(self, url):
        req = urq.Request(url)
        req.add_header('X-Naver-Client-Id', '0FlGPmT7M61ipCY0R4Wu')
        req.add_header ('X-Naver-Client-Secret', 'MnMmAcySf9')

        try:
            res = urq.urlopen(req)
            if res.getcode() == 200: #okay
                print('[{0}]URL Request succeed'.format(datetime.datetime.now()))
                return res.read().decode('utf-8')
        except Exception as e:
            print(e)
            return None

    #네이버 검색 API 사용함수
    def getNaverSearchResult(self, sNode, search_word, page_start, display):
        base = 'https://openapi.naver.com/v1/search/'
        node = '{0}.json'.format(sNode)
        param = '?start={0}&display={1}&query={2}'.format(page_start, display, uparse.quote(search_word))
        url = base + node + param # Ex) http://openapi.naver.con....nodeval.json?start=1&display=100&query=코로나

        retData = self.getRequestUrl(url)
        if retData == None:
            return None
        else:
            return json.loads(retData)
