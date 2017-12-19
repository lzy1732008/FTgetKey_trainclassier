#创建关于法条的词典，利用频繁集
import jieba
import xml.dom.minidom as par
import os


def getAJJBQK(path):
    print('getAJJBQK:'+path)
    dom = par.parse(path)
    root = dom.documentElement
    childlist = root.getElementsByTagName('QW')
    qw = childlist[0]
    qwChild = qw.getElementsByTagName('AJJBQK')
    content = ''
    if qwChild:
        ajjbqk = qwChild[0]
        content = ajjbqk.getAttribute('value')
    return content

def setCor(dicpath):
    corpus = []
    print('setCor:'+dicpath)
    filepathlist = os.listdir(dicpath)
    corpuscontent = ''
    for filepath in filepathlist:
        content = getAJJBQK(dicpath+'\\'+filepath)
        corpuscontent += content
        contentcut = jieba.lcut(content)
        for c in contentcut:
            corpus.append(c)
    return corpus,corpuscontent

def searchCandidateSet(corpus,corpuscontent):
    candidate = {}
    point = 0
    while point < len(corpus)-1:
        s2 = str(corpus[point])+str(corpus[point+1])
        num2 = corpuscontent.count(s2,0,len(corpuscontent))
        if num2 >= 1:
            candidate[s2] = num2
            if point + 2 < len(corpus):
                s3 = s2+corpus[point+2]
                num3 = corpuscontent.count(s3)
                if num3 >= 1:
                    candidate[s3] = num3
                    if point + 3 <len(corpus):
                        s4 = s3 + corpus[point + 3]
                        num4 = corpuscontent.count(s4)
                        if num4 >= 1:
                            candidate[s4] = num4
        point += 1
    return candidate

def ifContain(key,rmchar):
    for c in rmchar:
        if str(key).startswith(c) or str.endswith(c):
            return True
    return False

def filterCandidate(candidate):
    rmchar = ['的','与','是','该','你','我','她','他','及','这']
    for (key,value) in candidate.items:
        if ifContain(key,rmchar):
             candidate.pop(key)
    print(str(candidate))
def createDic():
     dicpath = 'C:\\Users\\Dell\\Desktop\\2013_big'
     corpus, corpuscontent = setCor(dicpath)
     candidate = searchCandidateSet(corpus, corpuscontent)
     filterCandidate(candidate)


createDic()