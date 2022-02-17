
def getEntityFromTags(mySentList,myTagList):
    '''
    从tagList中获取sentList中的实体
    '''
    entityList=[]
    tmpEntity=""
    for tagI,_ in enumerate(myTagList):
        if tagI>=len(mySentList):
            break
        if myTagList[tagI]=="B":
            if len(mySentList[tagI])>1:
                tmpEntity=mySentList[tagI]+" "
            else:
                tmpEntity=mySentList[tagI]
        elif myTagList[tagI]=="I":
            if len(mySentList[tagI])>1:
                tmpEntity+=" "+mySentList[tagI]
            else:
                tmpEntity+=mySentList[tagI]
        else:
            if len(tmpEntity)>0:
                entityList.append(tmpEntity)
            tmpEntity=""
    return entityList

if __name__=="__main__":
    
    mySentList=['[START]', '时', '需', '要', '了', '解', '注', '意', '的', '各', '项', '规',
       '范', '对', '接', '流', '程', '从', '开', '发', '到', '测', '试', '到', '发',
       '布', '提', '供', '实', '际', '接', '入', '例', '子', '方', '便', '后', '续',
       '各', '类', '子', '系', '统', '对', '接', '[END]']
    myTagList=['START', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B',
        'I', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
        'O', 'O', 'O', 'O', 'O', 'O', 'O', 'END', 'PAD', 'PAD', 'PAD',
        'PAD', 'PAD', 'PAD', 'PAD', 'PAD', 'PAD', 'PAD', 'PAD', 'PAD',
        'PAD', 'PAD', 'PAD', 'PAD', 'PAD', 'PAD', 'PAD', 'PAD']
    print(getEntityFromTags(mySentList,myTagList))