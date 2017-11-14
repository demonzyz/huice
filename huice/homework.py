# coding=utf-8
import re
'''
切割字符串
统计每个单词出现次数    
按次数排序
输出前5
'''


# 1
def findTopWords1(text, num=1):
    list = text.split()
    dic = dict.fromkeys(list, 0)
    for key in dic.keys():
        dic[key] = list.count(key)
    return sorted(dic.items(), key=lambda items: items[1], reverse=True)[:5]
    # return sorted(dic.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)[:5]

# 2
def findTopWords2(text, num=1):
    list= text.split()
    dict, newDict = {}, {}
    for i in range(len(list)):
        dict.setdefault(list[i], list.count(list[i]))
    for j in range(0, num):
        tmp = sorted(dict.iteritems(), key=lambda items: items[1], reverse=True)[j]
        newDict.setdefault(tmp[0], tmp[1])
    return newDict

# 3
def findTopWords3(text, num=1):
    lst = re.split('[0-9\W]+', text)
    words = set(lst)
    d = {}
    for word in words:
        d[word] = lst.count(word)
    del d['']
    result = []
    for key, value in sorted(d.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        result.append((key, value))
    return result[:num]


text = '''
A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may be interested in analyzing other texts from Project Gutenberg. You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian
'''
topWords = findTopWords1(text, 5)
print topWords

topWords = findTopWords3(text, 5)
print topWords