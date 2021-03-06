# -*- coding: utf-8 -*-

# @Author  : Skye
# @Time    : 2018/1/9 10:39
# @desc    :

import requests
import webbrowser
import urllib
import re
import Global as g
# # 颜色兼容Win 10
from colorama import init,Fore
init()




def open_webbrowser(question):
    #print(urllib.quote(question.encode('utf8')))
    #webbrowser.open('https://wap.baidu.com/s?wd=' + urllib.quote(question.encode('utf8')))
    #webbrowser.open('https://www.baidu.com/' )
    return

def open_webbrowser_count(question,choices):
    print('\n-- 方法2： 题目+选项搜索结果计数法 --\n')
    print('Question: ' + question.encode('utf8'))
    for nokey in g.opposite:
        if nokey in (question.encode('utf8')):
            g.opp=False
            print('**请注意此题为否定题,选计数最少的**')

    counts = []
    for i in range(len(choices)):
        # 请求
        req = requests.get(url='http://www.baidu.com/s', params={'wd': question + choices[i]})
        content = req.text.encode('utf8')
        #print (type(content))
        index = content.find('百度为您找到相关结果约') + 11
        content = content[index:]
        index = content.find('个')
        count = content[:index].replace(',', '')
        count = re.sub("\D", "", count)
        counts.append(int(count))
        #print(choices[i] + " : " + count)
    output(choices, counts)

def count_base(question,choices):
    print('\n-- 方法3： 题目搜索结果包含选项词频计数法 --\n')
    # 请求
    req = requests.get(url='http://www.baidu.com/s', params={'wd':question})
    content = req.text.encode('utf8')
    #print(content)
    counts = []
    print('Question: '+question)
    #print(choices[0].encode('utf8'))
    for nokey in g.opposite:
        if nokey in (question.encode('utf8')):
            g.opp = False
            print('**请注意此题为否定题,选计数最少的**')
    for i in range(len(choices)):
        counts.append(content.count((choices[i].encode('utf8'))))
        #print(choices[i] + " : " + str(counts[i]))
    output(choices, counts)

    print(urllib.quote(question.encode('utf8')))
    webbrowser.open('https://wap.baidu.com/s?wd=' + urllib.quote(question.encode('utf8')))

def output(choices, counts):
    counts = list(map(int, counts))
    #print(choices, counts)
    #print counts
    # 计数最高
    if(len(counts)<=0):
        index_max =0
    else:
        index_max = counts.index(max(counts))

    # 计数最少
    if(len(counts)<=0):
        index_min = 0
    else:
        index_min = counts.index(min(counts))

    if index_max == index_min:
        print(Fore.RED + "高低计数相等此方法失效！" + Fore.RESET)
        return

    #print(choices[0].encode('utf8'))
    for i in range(len(choices)):
        if i == index_max:
            # 绿色为计数最高的答案
            if(g.opp == True):
                print(Fore.GREEN + "{0} : {1} ".format(choices[i].encode('utf8'), counts[i]) + Fore.RESET)
            else:
                print("{0} : {1}".format(choices[i].encode('utf8'), counts[i]))
        elif i == index_min:
            # 红色为计数最低的答案
            if(g.opp==False):
                print(Fore.MAGENTA + "{0} : {1}".format(choices[i].encode('utf8'), counts[i]) + Fore.RESET)
            else:
                print("{0} : {1}".format(choices[i].encode('utf8'), counts[i]))
        else:
            print("{0} : {1}".format(choices[i].encode('utf8'), counts[i]))
    opp=True


def run_algorithm(al_num, question, choices):
    if al_num == 0:
        open_webbrowser(question)
    elif al_num == 1:
        open_webbrowser_count(question, choices)
    elif al_num == 2:
        count_base(question, choices)

if __name__ == '__main__':
    question = '新装修的房子通常哪种化学物质含量会比较高?'
    choices = ['甲醛', '苯', '甲醇']
    run_algorithm(1, question, choices)


