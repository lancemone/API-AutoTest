s = 'A small sample of texts from Project Gutenberg appears in the NLTK corpus collection. However, you may be interested in analyzing ' \
    'other texts from Project Gutenberg. You can browse the catalog of 25,000 free online books at http :// www . gutenberg . org / catalog /, and ' \
    'obtain a URL to an ASCII text file. Although 90% of the texts in Project Gutenberg are in English, it includes material in over 50 other ' \
    'languages, including Catalan, Chinese, Dutch, Finnish, French, German, Italian'


def get_m(st):
    s = str(st)
    word = s.split(' ')
    dic = {}
    for key in word:
        if key in dic.keys():
            v = dic.get(key, 0)
            v = v + 1
            dic[key] = v
        else:
            dic[key] = 1
    return sorted(dic.items(), key=lambda item: item[1])


a = get_m(s)
print(a)
