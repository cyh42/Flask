import requests
import xlrd
import json
import cgi
import pandas as pd
import time

print ("Content-type: text/html\n")

j = 0

data = xlrd.open_workbook('85.xls')
table = data.sheets()[0]
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数

aList = []
cnt = []
Name = []
Number = []
Score = []
gpa = []
title = [u'排名', u'姓名', u'学号', u'学分绩', u'gpa']

def takeSecond(elem):
    return elem[2]

def paixu():
    aList.sort(key=takeSecond, reverse=True)
    for i in range(len(aList)):
        cnt.append(i + 1)
        Name.append(aList[i][0])
        Number.append(aList[i][1])
        Score.append(aList[i][2])
        gpa.append(aList[i][3])

def convertToHtml(result, title, time):
    d = {}
    index = 0
    for t in title:
        d[t]=result[index]
        index = index+1
    df = pd.DataFrame(d)
    df = df[title]
    # print(df)
    h = df.to_html(index=False)
    h = h + str(round(time, 3)) + 's'
    # print(h)
    return h

def Rank():
    time_start = time.time()
    aList.clear()
    cnt.clear()
    Name.clear()
    Number.clear()
    Score.clear()
    gpa.clear()
    for i in range(1, nrows):
        try:
            name = table.cell(i, 3).value
            username = table.cell(i, 9).value
            password = table.cell(i, 10).value
            s = requests.session()
            payload = {'username': username, 'password': password}
            postMessage = s.post("https://zhxyapp.upc.edu.cn/wap/login/commit.html", data=payload)
            try:
                data = {'xn': '2018-2019', 'kcmc': '', 'type': '1'}
                r = s.post('https://zhxyapp.upc.edu.cn/extensions/wap/score/search.html', data=data)
                sJOSN = r.text
                sValue = json.loads(sJOSN)
                r = sValue['data']['scores']['1']
                aList.append([name, username, sValue['data']['xfjd'], sValue['data']['gpa']])
                j = j + 1
                r = s.get('https://zhxyapp.upc.edu.cn/wap/login/loginout.html')
            except:
                continue
        except:
            continue
    paixu()
    # print(convertToHtml([Name] + [Number] + [Score] + [gpa], title))
    time_end = time.time()
    totally_cost = time_end - time_start
    h = convertToHtml([cnt] + [Name] + [Number] + [Score] + [gpa], title, totally_cost)
    # print(time_end, time_start)
    # print(h)
    return h