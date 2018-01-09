# encoding:utf-8
englishString = 'A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may be interested in analyzing other texts from Project Gutenberg. You can browse the catalog of 25,000 free online books at http://www.gutenberg.org/catalog/, and obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian'

# not_douhao = englishString.replace(',', ' ')
# re_string = not_douhao.replace('http://www.gutenberg.org/catalog/', 'http www gutenberg org catalog')
# simple_string = re_string.split(' ')
# simple_dict = dict.fromkeys(simple_string, 1)
# for y in simple_dict:
#     simple_dict[y] = simple_string.count(y)
# re_dict = sorted(simple_dict.items(), lambda x,y:cmp(x[1],y[1]), reverse=True)[:3]
# for x in re_dict:
#     print x
#     print x[0],x[1]














# not_english = englishString.replace(',', ' ')
# not_hit = not_english.replace('http://www.gutenberg.org/catalog/', 'http www utenberg org catalog')
# list = not_hit.split(' ')
# dict = dict.fromkeys(list, 1)
# for key in dict:
#     dict[key] = list.count(key)
# new_dict = sorted(dict.items(), lambda x,y:cmp(x[1], y[1]), reverse=True)[:10]
# print dict
# print new_dict
# for x in new_dict:
#         print x[0], x[1]



