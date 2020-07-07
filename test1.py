import time
import requests
import json



def req_air(a, d):
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

    response = requests.post(url=url, data=body, headers=headers)
    prices_list = json.loads(response.text)
    for item in prices_list['prices']:
        t = item['dDate']
        timearry = time.strptime(t, '%Y-%m-%d')
        r_time = int(time.mktime(timearry))
        if item['price'] is not None and r_time < 1596211200:
            print(t)


if __name__ == '__main__':

    city_dic = {'PAR': 'SHA', 'AMS': 'SHA', 'FRA': ['SHA', 'PVG', 'NKG']}
    keys_list = city_dic.keys()
    for a_city in keys_list:
        b_city = city_dic[a_city]
        if not isinstance(b_city, list):
            req_air(a_city, b_city)
        else:
            for d in b_city:
                req_air(a_city, d)
