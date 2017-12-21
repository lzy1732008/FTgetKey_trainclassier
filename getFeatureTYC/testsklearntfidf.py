from sklearn.feature_extraction.text import  TfidfVectorizer as tfidf
import os
import getftkey
import wsutil.wsfun as wsfun
import jieba
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

corpus = []
for ft in ftmcList:
    with open('../laws/'+ft+'_标准化.txt','r',encoding='UTF-8') as f:
          content = f.read()
          corpus.append(content)
