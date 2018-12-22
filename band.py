import sqlite3

def getData(dbname,table,indexOf,createFile='test'):
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
            for index in indexOf:
                cur+=str(item[indexOf[index]])+','
            cur=cur[:-1]
            f.write('%s\n'%(cur))

if __name__=='__main__':
    getData('./Gadgetbridge','MI_BAND_ACTIVITY_SAMPLE',{'time':0,'heart':6})

