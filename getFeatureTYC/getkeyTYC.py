#输入法条的关键词，使用word2vec获取法条关键词的同义词，注意:输入文书作为语料库，用文书的QW内容
import jieba
import xml.dom.minidom as par
import os
import gensim
import getftkey
import re
import difflib


from gensim.models import word2vec
def buildmodel(corpuspath,modelpath):
    print('build model......')
    corpus = []
    model = word2vec.Word2Vec(setCor(corpuspath,corpus),min_count=5)
    model.save(modelpath)
    print('built......')
    return model

def getQW(path):
    print('getQW:'+path)
    dom = par.parse(path)
    root = dom.documentElement
    childlist = root.getElementsByTagName('QW')
    qw = childlist[0]
    content = ''
    if qw:
        content = qw.getAttribute('value')
    return content

def setCor(dicpath,corpus):
    print('setCor:'+dicpath)
    filepathlist = os.listdir(dicpath)
    order = 0
    for filepath in filepathlist:
        print(order)
        content = getQW(dicpath+'\\'+filepath)
        contentcut = jieba.lcut(content)
        corpus.append(contentcut)
        order += 1
    return corpus

def get_similar_words_str(w, model, topn = 10):
    result_words = get_similar_words_list(w, model)
    return str(result_words)


def get_similar_words_list(w, model, topn = 10):
    result_words = []
    try:
        similary_words = model.most_similar(w,topn=10)
        # print(similary_words)
        for (word, similarity) in similary_words:
            result_words.append(word)
        # print(result_words)
    except:
        print("There are some errors!" + w)

    return result_words

def load_models(model_path):
    return gensim.models.Word2Vec.load(model_path)


#建立关键词库
def set_keyset():
    corpus_path ='D:\\nju\\task\\WS2013\\2013'
    model_path='D:\\nju\\task\\keymodel.model'
    buildmodel(corpus_path,model_path)
    model = load_models(model_path)
    ft_key = getftkey.getftKey()
    all_key = []
    # with open('D:\\南大\\学习\\codeTrain\\FTgetKey_trainclassier\\txt\\keyset.txt','w',encoding='utf-8') as f:
    #     for i in range(int(len(ft_key)/2)):
    #     # for key in ft_key:
    #         key = ft_key[i]
    #         if key not in all_key and len(key)>1:
    #             all_key.append(key)
    #             words = get_similar_words_str(key, model)
    #             print(key)
    #             print(words)
    #             sp = re.split('[\[\]\',]',words)
    #             for word in sp:
    #                 if word != '' and word != '\n' and len(word)>1:
    #                    if word not in all_key:
    #                       all_key.append(word)
                          # f.write(word+'\n')
    # for key in all_key:
    #     print(key)
    return all_key
set_keyset()