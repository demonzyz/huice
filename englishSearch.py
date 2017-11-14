# coding=utf-8

englishString = 'A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may be interested in analyzing other texts from Project Gutenberg. You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian'

# 去掉englishString字符串中的逗号
rp_comma = englishString.replace(',','')
# print rp_comma.split(" ")

# 将englishString字符串中的网址变成字符串
rp_web = rp_comma.replace('http://www.gutenberg.org/catalog/','http www gutenberg org catalog ')
# print rp_web.split(" ")
# rp_colon = rp_comma.replace(':',' ')
# print rp_colon.split(" ")
# rp_doubleSlash = rp_colon.replace('/',' ')
# print rp_doubleSlash.split(" ")

# 去掉englishString字符串中的句号
rp_period = rp_web.replace('.','')
# print rp_period.split(" ")

# 字符串变列表list
ex_englishString = rp_period.split(" ")
# print type(ex_englishString[1])
# print type(ex_englishString)

# 列表变字典,key为字符串,value默认赋值
stringDict = dict.fromkeys(ex_englishString, 1)
print ("New Dictionary : %s" %  str(stringDict))

# 通过stringDict字典中的key值出现在ex_englishString中的次数,统计出现次数
for key in stringDict:
    stringDict[key] = ex_englishString.count(key)

# 将stringDict字典按照value的值进行降序排列,并输出前5个
count_stringDict = sorted(stringDict.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
for i in range(5):
    print count_stringDict[i]

print sorted(stringDict.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)


# print ("New Dictionary : %s" %  str(stringDict))