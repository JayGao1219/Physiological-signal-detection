import time
import sqlite3

def raw(item,begin,end):
    if item:
        return True
    return False

def timeheart(item,begin,end):
    if begin and end:
        beginArray=time.strptime(begin,"%Y-%m-%d %H:%M:%S")
        beginStamp=time.mktime(beginArray)
        endArray=time.strptime(end,"%Y-%m-%d %H:%M:%S")
        endStamp=time.mktime(endArray)
        if (item[0]<beginStamp) or (item[0]>endStamp):
            return False
        pass
    if item[6]<10 or item[6]>250:
        return False
    return True

def getData(dbname,table,indexOf,fun=raw,begin='',end='',createFile='test'):
    mydb=sqlite3.connect(dbname)
    cursor=mydb.cursor()
    data=cursor.execute(
        "SELECT * FROM %s;"%(table)
    )
    with open(createFile+'.csv','w') as f:
        cur=''
        for item in indexOf:
            cur+=item+','
        cur=cur[:-1]
        f.write('%s\n'%(cur))
        for item in data:
            cur=''
            #检验数据的合法性
            if fun(item,begin,end)==False:
                continue
            for index in indexOf:
                cur+=str(item[indexOf[index]])+','
            cur=cur[:-1]
            f.write('%s\n'%(cur))

if __name__=='__main__':
    getData('./Gadgetbridge','MI_BAND_ACTIVITY_SAMPLE',{'time':0,'heart':6},timeheart)

