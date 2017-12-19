import difflib
import os
import wsutil.wsfun as wsfun
import getFeatureTYC.getkeyTYC as feature
import threading
#计算最小编辑距离
def difflib_leven(str1, str2):
    leven_cost = 0
    s = difflib.SequenceMatcher(None, str1, str2)
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        # print('{:7} a[{}: {}] --> b[{}: {}] {} --> {}'.format(tag, i1, i2, j1, j2, str1[i1: i2], str2[j1: j2]))

        if tag == 'replace':
            leven_cost += max(i2 - i1, j2 - j1)
        elif tag == 'insert':
            leven_cost += (j2 - j1)
        elif tag == 'delete':
            leven_cost += (i2 - i1)
    return leven_cost/max(len(str1),len(str2))

#从文书中寻找Key的相似词,利用滑动窗口
def get_similar_word_count(key,content):
    sum = 0
    win = len(key)+2
    i = win - 1
    while i < len(content)-win:
        dis = difflib_leven(content[i:i + win - 1], key)
        if dis <= 0.5:
            sum += 1
           # print(content[i:i + win - 1])
            i = i + win - 1
        else:
            i+= 1
    return sum



def setdata(wsstart,wsend):
    print('thread %s is running...' % threading.current_thread().name)

    dicpath = 'C:\\Users\\Dell\\Desktop\\FTTJ\\ws_1w'
    dic = os.listdir(dicpath)
    keys = feature.set_keyset()

    ftlist = []
    with open('../txt/ftlist_China.txt','r',encoding='utf-8') as f:
        s = f.readline()
        while s:
            ftlist.append(s)
            s = f.readline()
    with open('D:\\南大\\学习\\codeTrain\\FTgetKey_trainclassier\\txt\\data'+str(wsstart)+'.txt','w',encoding='utf-8') as f:
         for i in range(wsstart,wsend-1):
             write_s = ''
             print('order:%s'%(i))
             content = wsfun.getQW(dicpath+'\\'+dic[i])
             #对每个关键词在文书中找相似词出现的频率
             for key in keys:
                 write_s += str(get_similar_word_count(key,content))+','
             #统计文书的法条情况
             wsftlist = wsfun.getFTfromWS(dicpath +'\\'+dic[i])
             for ft in ftlist:
                 flag = 0
                 for wsft in wsftlist:
                     if ft == wsft:
                         write_s += '1,'
                         flag = 1;
                         break;
                 if flag == 0:
                     write_s += '0,'
             write_s+='\n'
             f.write(write_s)
    print('特征词个数：%d'%(len(keys)))
    print('法条个数：%d'%(len(ftlist)))
    print('thread %s ended.' % threading.current_thread().name)



def threadfun():
    t1 = threading.Thread(target=setdata,args=(0,2000),name = 'thread1')
    t2 = threading.Thread(target=setdata,args=(2000,4000), name='thread2')
    t3 = threading.Thread(target=setdata,args=(4000,6000), name='thread3')
    t4 = threading.Thread(target=setdata,args=(6000,8000), name='thread4')
    t5 = threading.Thread(target=setdata,args=(8000,10000),name='thread5')
    t6 = threading.Thread(target=setdata,args=(10000,12000), name='thread6')
    t7 = threading.Thread(target=setdata,args=(12000,14000), name='thread7')
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()







threadfun()



