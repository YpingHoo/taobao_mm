import requests


def getPageInfo(page_num):
    page_url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'

    headers = {
        'origin': 'https://mm.taobao.com',
        'referer': 'https://mm.taobao.com/search_tstar_model.htm?spm=5679.126488.640745.2.182b584CpX6ln',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }

    datas = {
        'q':'',
        'viewFlag': 'A',
        'sortType': 'default',
        'searchStyle': '',
        'searchRegion': 'city:',
        'searchFansNum': '',
        'currentPage': page_num,
        'pageSize': '100',
    }

    page = requests.post(page_url, headers=headers, data=datas).json()
    mm_list = page['data']['searchDOList']
    totalpage = page['data']['totalPage']

    return totalpage, mm_list


def printInfo(mm_list):
    mm_page_total = 0
    for info in mm_list:
        name = info['realName']
        height = info['height']
        weight = info['weight']
        city = info['city']
        totalFavorNum = info['totalFavorNum']

        print("-----%s-----" % name)
        print("身高: %s " % height)
        print("体重: %s " % weight)
        print("城市: %s " % city)
        print("受欢迎指数: %s " % totalFavorNum)
        mm_page_total += 1
    return mm_page_total


def getMoreMM(num):
    totalpage = getPageInfo(1)[0]
    mm_total = 0
    for i in range(1, totalpage):
        mm_list = getPageInfo(i)[1]
        mm_page_total = printInfo(mm_list)
        mm_total += mm_page_total
        if i==num:
            break
    print("\n#####获取到%s位mm信息#####" % mm_total)


getMoreMM(2)
