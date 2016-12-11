# coding=utf-8
import requests
import time
from bs4 import BeautifulSoup


# 获得指定起始排名的电影url
def get_url(root_url, start):
    return root_url + "?start=" + str(start) + "&filter="


# 根据传入的url，获取电影排名及评分，代码如下
def get_review(page_url):
    # 存放电影信息的列表
    movies_list = []
    # 请求url，返回response对象
    response = requests.get(page_url)
    # 指定lxml解析器解析html文档
    soup = BeautifulSoup(response.text, "lxml")
    # 获取包含所有电影信息的节点
    soup = soup.find('ol', 'grid_view')
    # 循环获取单个节点
    for tag_li in soup.find_all('li'):
        dict = {}
        # 地区
        num = 0
        for string in tag_li.find_all('p')[0].stripped_strings:
            if num == 1:
                zone = string.encode('utf-8').split("/")[1]
                if zone.find("中国") > 0 or zone.find("台湾") >0 or zone.find("香港") > 0 or zone.find("澳门") > 0:
                    dict['zone'] = zone.replace("\xc2\xa0", "")
                    # 排名
                    dict['rank'] = tag_li.find('em').string
                    # 名称
                    dict['name'] = tag_li.find_all('span', 'title')[0].string
                    # 评分
                    dict['score'] = tag_li.find('span', 'rating_num').string
                    ## 有的电影短评为空，为防止抓取到一半出错，需判断是否为空
                    #if tag_li.find('span', 'inq'):
                    #    dict['desc'] = tag_li.find('span', 'inq').string
                    movies_list.append(dict)
            num += 1


    return movies_list


if __name__ == "__main__":
    root_url = "https://movie.douban.com/top250"
    start = 0
    num = 0
    while start < 250:
        movies_list = get_review(get_url(root_url, start))
        for movie_dict in movies_list:
            num += 1
            print num
            print("电影排名：" + movie_dict['rank'].encode('utf-8') )
            print("电影名字：" + movie_dict.get('name').encode('utf-8'))
            print("电影地区：" + movie_dict.get('zone'))
            print("电影评分：" + movie_dict.get('score').encode('utf-8'))
            # print("电影评论：" + movie_dict.get('desc', '无评词').encode('utf-8'))
            print('------------------------------------------------------')
        start += 25
        time.sleep(5)
