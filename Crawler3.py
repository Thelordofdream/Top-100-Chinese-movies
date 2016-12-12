# coding=utf-8
# http://movie.douban.com/tag/%E5%8A%A8%E4%BD%9C?start=0&type=T
import urllib2
import re

import time


def store_set(input_set, file_name):
    fw = open(file_name, 'w')
    fw.writelines(input_set)
    fw.close()


j = 0
list = []
type = "喜剧"
zone = "日本"
grade = 7.5
for i in range(0, 2000, 20):
    # url = 'http://movie.douban.com/tag/%E5%8A%A8%E4%BD%9C?'
    url = 'http://movie.douban.com/tag/%s?' % (type + '%20' + zone)
    hash = 'start=%d&type=S' % i
    url = url + hash
    print i / 20 + 1
    # 读取url内容
    content = urllib2.urlopen(url).read()
    # 转换编码
    # content = content
    # 读取分数
    score = re.findall(r'<span class="rating_nums">(.*?)</span>', content)
    # 读取电影信息
    info = re.findall(r' <p class="pl">(.*?)</p>', content)
    # 读取电影名称
    title = re.findall(r' <a class="nbg".*?title="(.*?)">', content)
    # 读取电影链接
    URL = re.findall(r' <a class="nbg" href="(.*?)".*?>', content)
    for i in range(0, len(score)):
        # 大于7.5分的电影
        if score[i] != "":
            if float(score[i]) >= grade:
                if info[i].find(type) > 0:
                    j += 1
                    movie = title[i] + "   " + score[i]
                    print movie
                    # print len(match2)
                    list.extend(movie + "   " + URL[i] + '\n')
                elif info[i].find("...") > 0:
                    content0 = urllib2.urlopen(URL[i]).read()
                    info0 = re.findall(r' <span property="v:genre">(.*?)</span>', content0)
                    if type in info0:
                        j += 1
                        movie = title[i] + "   " + score[i]
                        print movie
                        # print len(match2)
                        list.extend(movie + "   " + URL[i] + '\n')
    time.sleep(0.5)

store_set(list, str(grade) + '分以上的' + zone + type + '电影.txt')
print ('总共抓取电影数据' + str(j) + '条')
print 'done'
