# -*- coding: utf-8 -*-

import jieba.posseg as pos
import jieba.analyse as ana


def getftKey():
    sentence1 = '因胁迫结婚的，受胁迫的一方可以向婚姻登记机关或人民法院请求撤销该婚姻。受胁迫的一方撤销婚姻的请求，应当自结婚登记之日起一年内提出。被非法限制人身自由的当事人请求撤销婚姻的，应当自恢复人身自由之日起一年内提出。'
    sentence2 = '禁止包办、买卖婚姻和其他干涉婚姻自由的行为。禁止借婚姻索取财物。禁止重婚。禁止有配偶者与他人同居。禁止家庭暴力。禁止家庭成员间的虐待和遗弃。'
    sentence3 = '夫妻应当互相忠实，互相尊重；家庭成员间应当敬老爱幼，互相帮助，维护平等、和睦、文明的婚姻家庭关系。'
    sentence5 = '结婚必须男女双方完全自愿，不许任何一方对他方加以强迫或任何第三者加以干涉。'
    sentence6 = '结婚年龄，男不得早于二十二周岁，女不得早于二十周岁。晚婚晚育应予鼓励。'
    sentence7 = '有下列情形之一的，禁止结婚：（一）直系血亲和三代以内的旁系血亲；（二）患有医学上认为不应当结婚的疾病。'
    sentence8 = '要求结婚的男女双方必须亲自到婚姻登记机关进行结婚登记。符合本法规定的，予以登记，发给结婚证。取得结婚证，即确立夫妻关系。未办理结婚登记的，应当补办登记。'
    sentence9 = '登记结婚后，根据男女双方约定，女方可以成为男方家庭的成员，男方可以成为女方家庭的成员。'
    sentence10 = '有下列情形之一的，婚姻无效：（一）重婚的；（二）有禁止结婚的亲属关系的；(三）婚前患有医学上认为不应当结婚的疾病，婚后尚未治愈的；（四）未到法定婚龄的。'
    sentence11 = '无效或被撤销的婚姻，自始无效。当事人不具有夫妻的权利和义务。同居期间所得的财产，由当事人协议处理；协议不成时，由人民法院根据照顾无过错方的原则判决。对重婚导致的婚姻无效的财产处理，不得侵害合法婚姻当事人的财产权益。当事人所生的子女，适用本法有关父母子女的规定。'
    sentence12 = '夫妻在婚姻关系存续期间所得的下列财产，归夫妻共同所有：（一）工资、奖金；（二）生产、经营的收益；（三）知识产权的收益；（四）继承或赠与所得的财产，但本法第十八条第三项规定的除外；（五）其他应当归共同所有的财产。夫妻对共同所有的财产，有平等的处理权。'
    sentence13 = '有下列情形之一的，为夫妻一方的财产：（一）一方的婚前财产；（二）一方因身体受到伤害获得的医疗费、残疾人生活补助费等费用；（三）遗嘱或赠与合同中确定只归夫或妻一方的财产；（四）一方专用的生活用品；（五）其他应当归一方的财产。'
    sentence14 = '夫妻可以约定婚姻关系存续期间所得的财产以及婚前财产归各自所有、共同所有或部分各自所有、部分共同所有。约定应当采用书面形式。没有约定或约定不明确的，适用本法第十七条、第十八条的规定。夫妻对婚姻关系存续期间所得的财产以及婚前财产的约定，对双方具有约束力。夫妻对婚姻关系存续期间所得的财产约定归各自所有的，夫或妻一方对外所负的债务，第三人知道该约定的，以夫或妻一方所有的财产清偿。'
    sentence15 = '夫妻有互相扶养的义务。一方不履行扶养义务时，需要扶养的一方，有要求对方付给扶养费的权利。'
    sentence16 = '父母对子女有抚养教育的义务；子女对父母有赡养扶助的义务。父母不履行抚养义务时，未成年的或不能独立生活的子女，有要求父母付给抚养费的权利。子女不履行赡养义务时，无劳动能力的或生活困难的父母，有要求子女付给赡养费的权利。禁止溺婴、弃婴和其他残害婴儿的行为。'

    sentences = [sentence1, sentence2, sentence3, sentence5, sentence6, sentence7, sentence8, sentence9, sentence10,
                 sentence11, sentence12, sentence13, sentence14, sentence15, sentence16]

    ft_key_identify  =  {"1":[]}
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


getftKey()