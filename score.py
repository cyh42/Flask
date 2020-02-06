import requests
import re
from bs4 import BeautifulSoup
import sys
import pandas as pd

print ("Content-type: text/html\n")
sys.setrecursionlimit(1000000)  # 解决递归限制
allScore = []
cnt = []
kcmc = []
result = []
xueqi = []
leibie = []
xuefen = []

def convertToHtml(result,title,red):
    d = {}
    index = 0
    for t in title:
        d[t]=result[index]
        index = index+1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    h = h + red
    return h

def fillScoreList(soup):
    data = soup.find_all('tr')
    for tr in data:
        singleScore = []
        ltd = tr.find_all('td')
        for td in ltd:
            singleScore.append(td.string)
        allScore.append(singleScore)


def printScoreList(num):
    print(allScore)
    for i in range(2, num):
        u = allScore[i]
        cnt.append(i-1)
        xueqi.append(u[1])
        kcmc.append(u[3])
        result.append(u[4])
        leibie.append(u[9])
        xuefen.append(u[5])

def cjcx():
    allScore.clear()
    cnt.clear()
    kcmc.clear()
    result.clear()
    xueqi.clear()
    leibie.clear()
    xuefen.clear()
    s = requests.session()
    r = s.get('https://cas.upc.edu.cn/cas/login')

    ltt = re.findall('<input type="hidden" id="lt" name="lt" value="(.*?)">', r.text, re.S)[0]
    lt = re.findall('(.*?)" />', ltt, re.S)[0]
    ess = re.findall('<input type="hidden" name="execution" value="(.*?)">', r.text, re.S)[0]
    es = re.findall('(.*?)" />', ess, re.S)[0]

    payload = {
        'rsa': '1346EEDF1F496FEE1DF74978442A0AE22404CFD15B8F010F78C15488A4ADA2E262CA129AE53A258E3E036FD295204CA834CCC0909BD988325701B54947D054CE6FF09061FD135EF0788A99D27004FBDB841AE11557946D44FD1D9AAF624DF9ECAC9A15FD7DE986DFB078639F64E93BB714412D184251D3119A216BCFE6054686',
        'ul': '10',
        'pl': '8',
        'lt': lt,
        'execution': es,
        '_eventId': 'submit'
    }
    s.post('https://cas.upc.edu.cn/cas/login', data=payload)
    s.get('https://i.upc.edu.cn/dcp/forward.action?path=/portal/portal&p=home')
    s.get('http://i.upc.edu.cn/dcp/forward.action?path=dcp/core/appstore/menu/jsp/redirect&appid=1180&ac=3')
    r = s.get('http://jwxt.upc.edu.cn/jsxsd/kscj/cjcx_list?kksj=2019-2020-1&kcxz=&kcmc=&xsfs=all')
    soup = BeautifulSoup(r.text, "lxml")
    red = soup.find_all('font')
    print(red[1].text)
    fillScoreList(soup)
    printScoreList(len(allScore))
    title = [u'序号', u'开课学期', u'课程名称', u'成绩', u'课程类别', u'学分']
    return convertToHtml([cnt] + [xueqi] + [kcmc] + [result] + [leibie] + [xuefen], title, red[1].text)