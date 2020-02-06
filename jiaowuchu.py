import requests
from lxml import etree
import re
from PIL import Image
import pytesser3
import os
import pandas as pd
from bs4 import BeautifulSoup
import pytesseract
import sys
sys.path.append('D:\\Web\\Flask\\verifycode')
import ocr

print("Content-type: text/html\n")
allScore = []
cnt = []
kcmc = []
result = []
xueqi = []
leibie = []
xuefen = []

def convertToHtml(result,title):
    d = {}
    index = 0
    for t in title:
        d[t]=result[index]
        index = index+1
    df = pd.DataFrame(d)
    df = df[title]
    h = df.to_html(index=False)
    return h

def fillScoreList(soup):
    data = soup.find_all('tr')
    for tr in data:
        singleScore = []
        ltd = tr.find_all('td')
        if len(ltd) != 13:
            continue
        for td in ltd:
            singleScore.append(td.string)
        allScore.append(singleScore)


def printScoreList(num):
    for i in range(num):
        u = allScore[i]
        cnt.append(i + 1)
        xueqi.append(u[3])
        kcmc.append(u[4])
        result.append(u[5])
        leibie.append(u[8])
        xuefen.append(u[10])

def login(user):
    allScore.clear()
    cnt.clear()
    kcmc.clear()
    result.clear()
    xueqi.clear()
    leibie.clear()
    xuefen.clear()
    while True:
        s = requests.session()
        Cookie = s.get('http://jwxt.upc.edu.cn/jwxt/').cookies
        Cookie = 'JSESSIONID' + '=' + Cookie['JSESSIONID']
        headers = {
            'Cookie': Cookie,
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)'
        }
        s.get('http://jwxt.upc.edu.cn/jwxt/', headers=headers)
        # 下载验证码
        with open('D:\\Web\\Flask\\verifycode\\captcha.jpg', 'wb') as f:
            f.write(s.get('http://jwxt.upc.edu.cn/jwxt/verifycode.servlet').content)
        # 手动输入验证码
        # captcha_code = input('输入验证码>>')
        # 自动识别验证码
        captcha_code = recognize_captcha().strip()
        data = {
            'USERNAME': user,
            'PASSWORD': user,
            'RANDOMCODE': captcha_code,
        }
        url = 'http://jwxt.upc.edu.cn/jwxt/Logon.do?method=logon'
        # 提交账号密码,验证码,,并登陆
        req =  s.post(url, data=data)
        page = etree.HTML(req.text)
        error = page.xpath('//span[@id="errorinfo"]/text()')
        print(error)
        if error == []:
            break
    url = 'http://jwxt.upc.edu.cn/jwxt/framework/main.jsp'
    req = s.get(url)
    url = 'http://jwxt.upc.edu.cn/jwxt/Logon.do?method=logonBySSO'
    s.get(url)
    r = s.post('http://jwxt.upc.edu.cn/jwxt/xszqcjglAction.do?method=queryxscj', data={'kksj': '2018-2019-1'})
    soup = BeautifulSoup(r.text, "lxml")
    fillScoreList(soup)
    printScoreList(len(allScore))
    title = [u'序号', u'开课学期', u'课程名称', u'成绩', u'课程类别', u'学分']
    return convertToHtml([cnt] + [xueqi] + [kcmc] + [result] + [leibie] + [xuefen], title)

def recognize_captcha():
    captcha_code = ocr.ocr()
    print(captcha_code)
    return captcha_code