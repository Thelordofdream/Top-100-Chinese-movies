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
for i in range(0, 1000, 20):
    # url = 'http://movie.douban.com/tag/%E5%8A%A8%E4%BD%9C?'
    type = "动作"
    url = 'http://movie.douban.com/tag/%s?' % type
    hash = 'start=%d&type=S' % i
    url = url + hash
    print i / 20 + 1
    # 读取url内容
    content = urllib2.urlopen(url).read()
    # 转换编码
    # content = content
    # 读取电影名称
    title = re.findall(r' <a class="nbg".*?title="(.*?)">', content)
    # 读取电影信息
    info  = re.findall(r' <p class="pl">(.*?)</p>', content)
    # 读取分数
    score = re.findall(r'<span class="rating_nums">(.*?)</span>', content)
    # print len(match2)
    for i in range(0, len(score)):
        # 大于8分的电影
        if score[i] != "":
            if float(score[i]) >= 7.5:
                if info[i].find("中国大陆") > 0 or info[i].find("香港") > 0 or info[i].find("台湾") > 0 or info[i].find("澳门") > 0:
                    if info[i].find("中国大陆)") < 0 and info[i].find("香港)") < 0 and info[i].find("台湾)") < 0 and \
                                    info[i].find("澳门)") < 0 and info[i].find("(中国大陆") < 0 and info[i].find("(香港") < 0 and \
                                    info[i].find("(台湾") < 0 and info[i].find("(澳门") < 0:
                        j += 1
                        movie = title[i] + "   " + score[i]
                        print movie
                        list.extend(movie + '\n')
    time.sleep(1)

store_set(list, '7.5分以上的中国' + type + '电影.txt')
print ('总共抓取电影数据' + str(j) + '条')
print 'done'
