import xml.dom.minidom as par
import os
import jieba
import math
import re
#1、需要去除标点符号
#2、切分单元长度不需要4个--->3个
#3、一些候选词还需要过滤
def getAJJBQK(path):
    print('getAJJBQK:'+path)
    dom = par.parse(path)
    root = dom.documentElement
    childlist = root.getElementsByTagName('QW')
    qw = childlist[0]
    # qwChild = qw.getElementsByTagName('AJJBQK')
    # content = ''
    # if qwChild:
    #     ajjbqk = qwChild[0]
    #     content = ajjbqk.getAttribute('value')
    content = qw.getAttribute('value')
    return content

def setCor(dicpath):
    corpus = []
    print('setCor:'+dicpath)
    filepathlist = os.listdir(dicpath)
    corpuscontent = ''
    for filepath in filepathlist:
        content = getAJJBQK(dicpath+'/'+filepath)
        corpuscontent += content
        contentsp = re.split('[，。；．《》（）？：、＊／：:×&”\[\]]',content)
        for sp in contentsp:
            contentcut = jieba.lcut(sp)
            for c in contentcut:
                if(c.strip() != ''):
                   corpus.append(c.strip())
    return corpus,corpuscontent

def searchCandidateSet(corpus,corpuscontent):
    candidate = {}
    point = 0
    while point < len(corpus)-1:
        s2 = str(corpus[point])+str(corpus[point+1])
        if candidate.get(s2,-1) == -1:
           num2 = corpuscontent.count(s2)
           if num2 >= 1:
               candidate[s2] = num2
               if point + 2 < len(corpus):
                   s3 = s2 + corpus[point + 2]
                   if candidate.get(s3, -1) == -1:
                       num3 = corpuscontent.count(s3)
                       if num3 >= 1:
                           candidate[s3] = num3
        else:
            if point + 2 < len(corpus):
                s3 = s2 + corpus[point + 2]
                if candidate.get(s3, -1) == -1:
                    num3 = corpuscontent.count(s3)
                    if num3 >= 1:
                        candidate[s3] = num3
                # else:
                #    num3 = candidate.get(s3)
                # if num3 >= 1:
                #    candidate[s3] = num3
                   # if point + 3 <len(corpus):
                   #      s4 = s3 + corpus[point + 3]
                   #      if candidate.get(s4, -1) == -1:
                   #         num4 = corpuscontent.count(s4)
                   #      else:
                   #         num4 = candidate.get(s4)
                   #      if num4 >= 1:
                   #         candidate[s4] = num4
        point += 1
    return candidate

def ifContain(key,rmchar):
    for c in rmchar:
        if str(key).startswith(c) or str(key).endswith(c):
            return True
    return False

def filterCandidate(candidate):
    print('enter filterCandidate')
    rmchar = ['的','与','是','该','你','我','她','他','及','这','，','。','：','《','》','；','、','x','X','（','）']
    for (key,value) in dict(candidate).items():
        if ifContain(key,rmchar) or str(key).isalnum() or str(key).isspace():
             candidate.pop(key)


#互信息：p(x,y)*log(p(x,y)/(p(x)*p(y)))
def mutualFilter(candidate,corpus,corpuscontent):
    print('enter multualFilter')
    print('pop candidate value.......')
    for (key,value) in dict(candidate).items():
         pxy = value/len(corpus)
         px = 1
         keysp = jieba.cut(key)
         for sp in keysp:
             px *= corpuscontent.count(sp)/len(corpuscontent)
         multualInfo =   pxy*math.log(pxy/px,2)
         #0.5\0.2\0.1\0.05\0.0025的时候candadate最后为空
         if multualInfo <=0.0025 :
            print(key)
            candidate.pop(key)
    print('candidate value.......')
    for i in candidate:
        print('%s:%d'%(i,candidate[i]))

def createDic():
     dicpath = '/users/wenny/Documents/law/2013_BIG'
     corpus, corpuscontent = setCor(dicpath)
     candidate = searchCandidateSet(corpus, corpuscontent)
     filterCandidate(candidate)
     mutualFilter(candidate,corpus,corpuscontent)

def testcut():
    stk = '对拒不执行有关扶养费、抚养费、赡养费、财产分割、遗产继承、探望子女等判决或裁定的，由人民法院依法强制执行。有关个人和单位应负协助执行的责任。'
    print(jieba.lcut(stk))


def testftDic():
    ft = 'hyf.txt'
    with open(ft,'r',encoding='UTF-8') as f:
        content = f.readlines()
        corpus = []
        corpuscontent = content
        for c in content:
            sp = re.split('[，；、。]',c)
            for s in sp:
                scut = jieba.lcut(s)
                for sc in scut:
                    corpus.append(sc)
    candidate = searchCandidateSet(corpus,corpuscontent)
    print(corpus)
    filterCandidate(candidate)
    mutualFilter(candidate,corpus,corpuscontent)

#testftDic()

createDic()