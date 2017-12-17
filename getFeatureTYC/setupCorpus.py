import jieba
import xml.dom.minidom as par
import os
#分词
#去除停用词
#是否能去除指定词性的词？？

def getAJJBQK(path):
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

def setCor(dicpath,corpus):
    os.chdir(dicpath)
    filepathlist = os.listdir(dicpath)
    for filepath in filepathlist:
        content = getAJJBQK(filepath)
        contentcut = jieba.lcut(content,cut_all=True)
        corpus.append(content)
    return corpus

