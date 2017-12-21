# -*- coding: utf-8 -*-

import jieba.posseg as pos
import jieba.analyse as ana
import math

HYF = '中华人民共和国婚姻法'
ZZFY = '最高人民法院关于人民法院审理离婚案件处理子女抚养问题的若干具体意见'
FYZNYJ = "最高人民法院关于人民法院审理离婚案件如何认定夫妻感情确已破裂的若干具体意见"
WDJTJ = "最高人民法院关于人民法院审理未办结婚登记而以夫妻名义同居生活案件的若干意见"
HYFJS_2 = "最高人民法院关于适用中华人民共和国婚姻法若干问题的解释二"
HYFJS_1 = "最高人民法院关于适用中华人民共和国婚姻法若干问题的解释三"
HYFJS_3 = "最高人民法院关于适用中华人民共和国婚姻法若干问题的解释一"
MSSSF = '中华人民共和国民事诉讼法'
MFTZ = '中华人民共和国民法通则'
MSSSZJ = '最高人民法院关于民事诉讼证据的若干规定'
GATMS = '最高人民法院关于涉港澳民商事案件司法文书送达问题若干规定'
GX = '最高人民法院关于调整高级人民法院和中级人民法院管辖第一审民商事案件标准的通知'
MSSSFYJ = '最高人民法院关于适用中华人民共和国民事诉讼法若干问题的意见'
JYCX = '最高人民法院关于适用简易程序审理民事案件的若干规定'
SSFYJN = '诉讼费用交纳办法'

ftmcList = [HYF,ZZFY,FYZNYJ,WDJTJ,HYFJS_2,HYFJS_1,HYFJS_3,MSSSF,MFTZ,MSSSZJ,GATMS,GX,MSSSFYJ,JYCX,SSFYJN]

def getKeyFormftList(sentences):
    ft_key = {}
    # ft_key = []
    # word_flag = ['n', 'nr', 'v', 'nr', 'nt', 'l', 'a', 'm', 't', 'j']
    # n,nr,v,nr,nt,l,a,m,t,j
    for sentence in sentences:
        word_tfidf = {}
        cuttags = pos.cut(sentence)
        # print(sentence)
        for (word, flag) in cuttags:
            if flag != 'p' and flag != 'x' and word not in word_tfidf and len(word) > 1:
               tf, idf, mul = count_tfidf(sentence, word, sentences)
               word_tfidf[word] = mul

                # ft_key.append(word)
              # print('%s:%f,%f,%f--%s'%(word,tf,idf,mul,flag))
        #         word_tfidf[word] = mul
        # ft_key[sentence] = word_tfidf
        ft_key[sentence] = word_tfidf
    normailize(ft_key)
    return ft_key

def count_tfidf(sentence,word,sentences):
    all_time,file_haveword = count_word_in_allFile(word,sentences)
    tf = str(sentence).count(word)/len(pos.lcut(sentence))
    idf = math.log(len(sentences)/file_haveword)
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

def normailize(ft_key):
    print('enter normailize')
    max_num = 0
    min_num = 1000000
    for (ftnr,ftkey) in ft_key.items():
         for (key,value) in ftkey.items():
             if value>max_num:
                 max_num = value
             if value <min_num:
                 min_num = value

    for (ftnr, ftkey) in ft_key.items():
        print(ftnr)
        for (key, value) in ftkey.items():
             ftkey[key] = value/(max_num-min_num)
             # if ftkey[key]>= 0.3:
             #     print('%s:%f' % (key,ftkey[key]))
             print('%s:%f' % (key, ftkey[key]))


def getftKey():
    with open('D:\\南大\\学习\\codeTrain\\FTgetKey_trainclassier\\txt\\ftlist.txt','r',encoding='utf-8') as f:
        s = f.readline()
        allft = []
        while s:
            print(s)
            ftmc = s.split(',')[0]
            ts = int(s.split(',')[1])
            if ftmc in ftmcList:
                nr = 'ff'
                nr = getftnr('D:\\南大\\学习\\codeTrain\\FTgetKey_trainclassier\\laws\\'+ftmc+'_标准化.txt',ts)
                allft.append(nr)
                print(nr)
            s = f.readline()

    ft_key = getKeyFormftList(allft)
    normailize(ft_key)
    return ft_key

getftKey()