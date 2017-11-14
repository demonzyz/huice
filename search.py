# coding=utf-8

englishString = 'A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may be interested in analyzing other texts from Project Gutenberg. You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian'

# 去掉englishString字符串中的逗号
rp_comma = englishString.replace(',','')
# print rp_comma.split(" ")

# 将englishString字符串中的网址变成字符串
rp_web = rp_comma.replace('http://www.gutenberg.org/catalog/','http www gutenberg org catalog')

# 去掉englishString字符串中的句号
rp_period = rp_web.replace('.','')

# 字符串变list列表
englishList = rp_period.split(" ")

# list列表变字典,key为字符串,value默认赋值
stringDict = dict.fromkeys(englishList, 1)

# 通过stringDict字典中的key值出现在ex_englishString中的次数,统计出现次数复制给value
for key in stringDict:
    stringDict[key] = englishList.count(key)

# 将stringDict字典按照value的值进行降序排列,并输出前5个
count_stringDict = sorted(stringDict.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

# 将得到的元祖通过(key,value)形式分离出来后,进行整合输出
for i in range(5):
    key = count_stringDict[i][0]
    value = count_stringDict[i][1]
    print "总共出现==>%d次<==,单词[%s]" % (value,key)

# 将得到元祖转换成list后,输出
# for i in range(5):
#     key = list(count_stringDict[i])[0]
#     value = list(count_stringDict[i])[1]
#     print "总共出现==>%d次<==,单词[%s]" % (value,key)
