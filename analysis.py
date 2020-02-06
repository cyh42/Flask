import requests
import json

def search(username, psw):
    sum = 0
    xf = 0
    list = []
    A = 0
    B = 0
    C = 0
    D = 0
    E = 0
    s = requests.session()
    data = {'username': username, 'password': psw}
    s.post("https://zhxyapp.upc.edu.cn/wap/login/commit.html?mpid=27", data=data)
    data = {'xn': '2016-2017', 'kcmc': '', 'type': '1'}
    r = s.post('https://zhxyapp.upc.edu.cn/extensions/wap/score/search.html', data=data)
    sJOSN = r.text
    sValue = json.loads(sJOSN)
    temp = sValue['data']['scores']['1']
    for i in range(len(temp)):
        dict = temp[i]
        if dict['KCLBMC'] == '必修':
            xf = xf + float(dict['XF'])
            sum = sum + float(dict['ZCJ']) * float(dict['XF'])
        if float(dict['ZCJ']) >= 95:
            A = A + 1
        elif float(dict['ZCJ']) >= 90:
            B = B + 1
        elif float(dict['ZCJ']) >= 85:
            C = C + 1
        elif float(dict['ZCJ']) >= 80:
            D = D + 1
        elif float(dict['ZCJ']) >= 75:
            E = E + 1
    list.append(round(sum / xf, 2))

    data = {'xn': '2016-2017', 'kcmc': '', 'type': '1'}
    r = s.post('https://zhxyapp.upc.edu.cn/extensions/wap/score/search.html', data=data)
    sJOSN = r.text
    sValue = json.loads(sJOSN)
    temp = sValue['data']['scores']['2']
    for i in range(len(temp)):
        dict = temp[i]
        if dict['KCLBMC'] == '必修':
            xf = xf + float(dict['XF'])
            sum = sum + float(dict['ZCJ']) * float(dict['XF'])
        if float(dict['ZCJ']) >= 95:
            A = A + 1
        elif float(dict['ZCJ']) >= 90:
            B = B + 1
        elif float(dict['ZCJ']) >= 85:
            C = C + 1
        elif float(dict['ZCJ']) >= 80:
            D = D + 1
        elif float(dict['ZCJ']) >= 75:
            E = E + 1
    list.append(round(sum / xf, 2))

    data = {'xn': '2016-2017', 'kcmc': '', 'type': '1'}
    r = s.post('https://zhxyapp.upc.edu.cn/extensions/wap/score/search.html', data=data)
    sJOSN = r.text
    sValue = json.loads(sJOSN)
    temp = sValue['data']['scores']['3']
    for i in range(len(temp)):
        dict = temp[i]
        if dict['KCLBMC'] == '必修':
            xf = xf + float(dict['XF'])
            sum = sum + float(dict['ZCJ']) * float(dict['XF'])
        if float(dict['ZCJ']) >= 95:
            A = A + 1
        elif float(dict['ZCJ']) >= 90:
            B = B + 1
        elif float(dict['ZCJ']) >= 85:
            C = C + 1
        elif float(dict['ZCJ']) >= 80:
            D = D + 1
        elif float(dict['ZCJ'])>= 75:
            E = E + 1
    list.append(round(sum / xf, 2))

    data = {'xn': '2017-2018', 'kcmc': '', 'type': '1'}
    r = s.post('https://zhxyapp.upc.edu.cn/extensions/wap/score/search.html', data=data)
    sJOSN = r.text
    sValue = json.loads(sJOSN)
    temp = sValue['data']['scores']['1']
    for i in range(len(temp)):
        dict = temp[i]
        if dict['KCLBMC'] == '必修':
            xf = xf + float(dict['XF'])
            sum = sum + float(dict['ZCJ']) * float(dict['XF'])
        if float(dict['ZCJ']) >= 95:
            A = A + 1
        elif float(dict['ZCJ']) >= 90:
            B = B + 1
        elif float(dict['ZCJ']) >= 85:
            C = C + 1
        elif float(dict['ZCJ']) >= 80:
            D = D + 1
        elif float(dict['ZCJ']) >= 75:
            E = E + 1
    list.append(round(sum / xf, 2))

    data = {'xn': '2017-2018', 'kcmc': '', 'type': '1'}
    r = s.post('https://zhxyapp.upc.edu.cn/extensions/wap/score/search.html', data=data)
    sJOSN = r.text
    sValue = json.loads(sJOSN)
    temp = sValue['data']['scores']['2']
    for i in range(len(temp)):
        dict = temp[i]
        if dict['KCLBMC'] == '必修':
            xf = xf + float(dict['XF'])
            sum = sum + float(dict['ZCJ']) * float(dict['XF'])
        if float(dict['ZCJ']) >= 95:
            A = A + 1
        elif float(dict['ZCJ']) >= 90:
            B = B + 1
        elif float(dict['ZCJ']) >= 85:
            C = C + 1
        elif float(dict['ZCJ']) >= 80:
            D = D + 1
        elif float(dict['ZCJ']) >= 75:
            E = E + 1
    list.append(round(sum / xf, 2))

    data = {'xn': '2017-2018', 'kcmc': '', 'type': '1'}
    r = s.post('https://zhxyapp.upc.edu.cn/extensions/wap/score/search.html', data=data)
    sJOSN = r.text
    sValue = json.loads(sJOSN)
    temp = sValue['data']['scores']['3']
    for i in range(len(temp)):
        dict = temp[i]
        if dict['KCLBMC'] == '必修':
            xf = xf + float(dict['XF'])
            sum = sum + float(dict['ZCJ']) * float(dict['XF'])
        if float(dict['ZCJ']) >= 95:
            A = A + 1
        elif float(dict['ZCJ']) >= 90:
            B = B + 1
        elif float(dict['ZCJ']) >= 85:
            C = C + 1
        elif float(dict['ZCJ']) >= 80:
            D = D + 1
        elif float(dict['ZCJ']) >= 75:
            E = E + 1
    list.append(round(sum / xf, 2))

    data = {'xn': '2018-2019', 'kcmc': '', 'type': '1'}
    r = s.post('https://zhxyapp.upc.edu.cn/extensions/wap/score/search.html', data=data)
    sJOSN = r.text
    sValue = json.loads(sJOSN)
    temp = sValue['data']['scores']['1']
    for i in range(len(temp)):
        dict = temp[i]
        if dict['KCLBMC'] == '必修':
            xf = xf + float(dict['XF'])
            sum = sum + float(dict['ZCJ']) * float(dict['XF'])
        if float(dict['ZCJ']) >= 95:
            A = A + 1
        elif float(dict['ZCJ']) >= 90:
            B = B + 1
        elif float(dict['ZCJ']) >= 85:
            C = C + 1
        elif float(dict['ZCJ']) >= 80:
            D = D + 1
        elif float(dict['ZCJ']) >= 75:
            E = E + 1
    list.append(round(sum / xf, 2))
    list.append(A)
    list.append(B)
    list.append(C)
    list.append(D)
    list.append(E)
    return list

if __name__ == '__main__':
    search()