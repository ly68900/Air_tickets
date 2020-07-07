import requests
import xlwt
import json
import os

def req_info(a, d):
    body = '{"stype":2,"dCty":"' + a + '","aCty":"' + d + '","flag":1,"start":"","end":"","classLevels":["Y"],' \
                                                          '"head":{"cid":"09031126310322327181","ctok":"",' \
                                                          '"cver":"1.0","lang":"01","sid":"8888","syscode":"09",' \
                                                          '"auth":null,"extension":[{"name":"appId",' \
                                                          '"value":"100008344"},{"name":"aid","value":"66672"},' \
                                                          '{"name":"sid",' \
                                                          '"value":"1693366"},{"name":"protocal",' \
                                                          '"value":"https"}]},"contentType":"json"} '

    url = 'https://m.ctrip.com/restapi/flight/html5/swift/getLowestPriceCalendar?_fxpcqlniredt=09031126310322327181'

    headers = {
        "accept": "application/json",
        "content-type": "application/json;charset=UTF-8",
        "accept-encoding": "gzip, deflate, br",
        "origin": "https://flights.ctrip.com"

    }
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('prices')
    title = ['日期', '出发', '到达', '价格']
    data = ['']
    row = 0
    col = 0

    for t in title:
        worksheet.write(row, col, t)
        col += 1
    row = 1
    response = requests.post(url=url, data=body, headers=headers)
    prices_list = json.loads(response.text)

    for item in prices_list['prices']:
        col = 0
        if item['price'] is not None:
            data = [item['dDate'], a, d, item['price']]
            # print(data)
            for one in data:
                print('row:{},col:{}'.format(row, col))
                worksheet.write(row, col, one)
                col += 1
            row += 1
    file_name = '{} to {}'.format(a, d) + '.xls'
    if os.path.exists(file_name):
        os.remove(file_name)
    workbook.save(file_name)


if __name__ == '__main__':

    city_dic = {'PAR': 'SHA', 'AMS': 'SHA', 'FRA': ['SHA', 'PVG', 'NKG']}
    keys_list = city_dic.keys()
    for a_city in keys_list:
        b_city = city_dic[a_city]
        if not isinstance(b_city, list):
            req_info(a_city, b_city)
        else:
            for d in b_city:
                req_info(a_city, d)
