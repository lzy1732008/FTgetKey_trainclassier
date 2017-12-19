import xml.dom.minidom as par

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


def getFTfromWS(path):
    dom = par.parse(path)
    root = dom.documentElement
    childlist = root.getElementsByTagName('QW')
    qw = childlist[0]
    CPFXGCList = qw.getElementsByTagName('CPFXGC')
    ft_list = []
    if CPFXGCList:
       CPFXGC = CPFXGCList[0]
       CUS_FLFT_FZ_RYList = CPFXGC.getElementsByTagName('CUS_FLFT_FZ_RY')
       if  CUS_FLFT_FZ_RYList:
            CUS_FLFT_RYlist = CUS_FLFT_FZ_RYList[0].getElementsByTagName('CUS_FLFT_RY')
            print(len(CUS_FLFT_RYlist))
            if CUS_FLFT_RYlist:
                print('2')
                for i in range(len(CUS_FLFT_RYlist)):
                    ft = (CUS_FLFT_RYlist[i].getAttribute('value'))
                    ft = str(ft).replace('《','')
                    ft = str(ft).replace('》', '')
                    ft = str(ft).replace('（', '')
                    ft = str(ft).replace('）', '')
                    ft = str(ft).replace('﹤', '')
                    ft = str(ft).replace('﹥', '')
                    ft_list.append(ft)
    return ft_list

