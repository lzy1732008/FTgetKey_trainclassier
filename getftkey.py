# -*- coding: utf-8 -*-

import jieba.posseg as pos
import jieba.analyse as ana
ftmcList = ['中华人民共和国婚姻法','最高人民法院关于人民法院审理离婚案件处理子女抚养问题的若干具体意见_标准化','最高人民法院关于人民法院审理离婚案件如何认定夫妻感情确已破裂的若干具体意见',
        '最高人民法院关于适用中华人民共和国婚姻法若干问题的解释二','最高人民法院关于适用中华人民共和国婚姻法若干问题的解释三','最高人民法院关于适用中华人民共和国婚姻法若干问题的解释一']
HYF = './laws/中华人民共和国婚姻法_标准化.txt'
ZZFY = './laws/最高人民法院关于人民法院审理离婚案件处理子女抚养问题的若干具体意见_标准化.txt'
FYZNYJ = "./laws/最高人民法院关于人民法院审理离婚案件如何认定夫妻感情确已破裂的若干具体意见_标准化.txt"
WDJTJ = "./laws/最高人民法院关于人民法院审理未办结婚登记而以夫妻名义同居生活案件的若干意见_标准化.txt"
HYFJS_2 = "./laws/最高人民法院关于适用中华人民共和国婚姻法若干问题的解释二_标准化.txt"
HYFJS_1 = "./laws/最高人民法院关于适用中华人民共和国婚姻法若干问题的解释三_标准化.txt"
HYFJS_3 = "./laws/最高人民法院关于适用中华人民共和国婚姻法若干问题的解释一_标准化.txt"

def getKeyFormftList(sentences):

    word_tfidf = {}
    word_flag = ['n', 'nr', 'v', 'nr', 'nt', 'l', 'a', 'm', 't', 'j']
    # n,nr,v,nr,nt,l,a,m,t,j
    for sentence in sentences:
        cuttags = pos.cut(sentence)
        print(sentence)
        for (word, flag) in cuttags:
            tf, idf, mul = count_tfidf(sentence, word, sentences)
            if mul>  3 and flag != 'p':
              print('%s:%f,%f,%f--%s'%(word,tf,idf,mul,flag))


def count_tfidf(sentence,word,sentences):
    all_time,file_haveword = count_word_in_allFile(word,sentences)
    tf = str(sentence).count(word)/all_time
    idf = len(sentences)/file_haveword
    mul = tf*idf
    return tf,idf,mul

def count_word_in_allFile(word,sentences):
    count = 0
    file_haveword = 0
    for s in sentences:
        count += str(s).count(word)
        if word in s :
            file_haveword += 1
    return count,file_haveword

def getftnr(ftname,ts):
    with open(ftname,'r',encoding='utf-8') as f:
        i = 1
        s = f.readline()
        while i < ts :
            f.readline()
            i += 1
        content = f.readline()
        start = (str(content).find('条'))
        ftnr = content[start+1:]
    return ftnr

def getftKey():
    with open('./txt/ftlist.txt','r',encoding='utf-8') as f:
        s = f.readline()
        allft = []
        while s:
            ftmc = s.split(',')[0]
            ts = int(s.split(',')[1])
            if ftmc in ftmcList:
                nr = 'ff'
                nr = getftnr('./laws/'+ftmc+'_标准化.txt',ts)
                allft.append(nr)
            s = f.readline()
    getKeyFormftList(allft)


getftKey()