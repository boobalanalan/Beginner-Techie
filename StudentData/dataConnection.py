import mysql.connector

def getConnection():
    con=mysql.connector.connect(host="localhost",user="root",password="",port="3306",database="student")
    cursor=con.cursor()
    #q="select * from std1"
    #cursor.execute(q)
    #rec=cursor.fetchall()
    #for row in rec:
        #print(row[0],"",row[1],"",row[2],"",row[3])

