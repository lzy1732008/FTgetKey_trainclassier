#输入法条的关键词，使用word2vec获取法条关键词的同义词
import jieba
import xml.dom.minidom as par
import os
import gensim

from gensim.models import word2vec
def buildmodel(corpuspath,modelpath):
    print('build model......')
    corpus = []
    model = word2vec.Word2Vec(setCor(corpuspath,corpus),min_count=5)
    model.save(model_path)
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
    for filepath in filepathlist:
        content = getQW(dicpath+'\\'+filepath)
        contentcut = jieba.lcut(content)
        corpus.append(contentcut)
    return corpus

def get_similar_words_str(w, model, topn = 10):
    result_words = get_similar_words_list(w, model)
    return str(result_words)


def get_similar_words_list(w, model, topn = 10):
    result_words = []
    try:
        similary_words = model.most_similar(w,topn=10)
        print(similary_words)
        for (word, similarity) in similary_words:
            result_words.append(word)
        print(result_words)
    except:
        print("There are some errors!" + w)

    return result_words

def load_models(model_path):
    return gensim.models.Word2Vec.load(model_path)

if __name__=='__main__':
    corpus_path ='C:\\Users\\Dell\\Desktop\\FTTJ\\ws_1w'
    model_path='D:\\nju\\task\\keymodel.model'
    # buildmodel(corpus_path,model_path)
    model = load_models(model_path)
    w =u"对两周岁以上未成年的子女，父方和母方均要求随其生活，一方有下列情形之一的，可予优先考虑：（1）已做绝育手术或因其他原因丧失生育能力的；（2）子女随其生活时间较长，改变生活环境对子女健康成长明显不利的；（3）无其他子女，而另一方有其他子女的；（4）子女随其生活，对子女成长有利，而另一方患有久治不愈的传染性疾病或其他严重疾病，或者有其他不利于子女身心健康的情形，不宜与子女共同生活的。"
    w_cut = jieba.cut(w)
    # for s in w_cut:
    #     print(s)
        # words = get_similar_words_str(s,model)
        # print(s)
        # print(words)
    words = get_similar_words_str('未成年',model)
    print(words)


