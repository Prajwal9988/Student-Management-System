import sqlite3
#def studentData():
con=sqlite3.connect("student.db")
cursor=con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY , StdID text , firstname text , Surname text,Dob text, Age text, Gender text  , Address text , Mobile Text)")





con.commit()
con.close()
def addStdRec(StdID ,firstname ,Surname , Dob , Age , Gender ,Address ,Mobile ):
                 con=sqlite3.connect("student.db")
                 cur=con.cursor ()
                 cur.execute("INSERT into student values(NULL,?,?,?,?,?,?,?,?)",(StdID ,firstname ,Surname , Dob , Age , Gender ,Address ,Mobile))
                 con.commit()
                 con.close()

def viewData():
                 con=sqlite3.connect("student.db")
                 cur= con.cursor()
                 cur.execute("SELECT * FROM student")
                 row=cur.fetchall()
                 
                 con.close()
                 return row
def deleteRec(id):
                 con=sqlite3.connect("student.db")
                 cur=con.cursor()
                 cur.execute("DELETE FROM  student WHERE id=?",(id,))
                 
                 con.commit()
                 con.close()

def searchData(StdID=" ",firstname=" ",Surname=" ",Dob=" ",Age=" ",Gender=" ",Address=" ",Mobile=" "):
                con=sqlite3.connect("student.db")
                cur=con.cursor()
                cur.execute("SELECT * FROM student WHERE StdID=? OR firstname=? OR Surname=? OR Dob=? OR Age=? OR Gender=? OR Address=? OR Mobile=? ",(StdID,firstname,Surname,Dob,Age,Gender,Address,Mobile))
                rows=cur.fetchall()
                con.close()
                return rows
def update(id,StdID=" ",firstname=" ",Surname=" ",Dob=" ",Age=" ",Gender=" ",Address=" ",Mobile=" "):
                con=sqlite3.connect("student.db")
                cur=con.cursor()
                cur.execute("UPDATE student SET StdID=?,firstname=?,Surname=?,Dob=?,Age=?,Gender=?,Address=?,Address=?,Mobile=?,WHERE id=?",\
                            (StdID,firstname,Surname,Dob,Age,Gender,Address,Mobile,id))
                con.commit()
                con.close()
                
                
