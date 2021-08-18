import pyodbc
#--------------------------------------------------------------------------------

def Insert_sDB(sID,pstr1):

    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO AcademicControlSystem.dbo.Student (ID, Password) values (?,?)", [(sID),(pstr1)])
    connection.commit()
    connection.close()
#--------------------------------------------------------------------------------
def Insert_instDB(instID,pstr1):

    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO AcademicControlSystem.dbo.Instructor (ID, Password) values (?,?)", [(instID),(pstr1)])
    connection.commit()
    connection.close()
#--------------------------------------------------------------------------------
def Insert_adminDB(instID,pstr1):

    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO AcademicControlSystem.dbo.Admin (ID, Password) values (?,?)", [(instID),(pstr1)])
    connection.commit()
    connection.close()
#--------------------------------------------------------------------------------
def Insert_StudentClassDB (sID, courseID):
    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO AcademicControlSystem.dbo.Student_Class (StudentID,CourseID) values (?,?)", [(sID), (courseID)])
    connection.commit()
    connection.close()

#------------------------------------------------------------------------
def select_Instpasswords(ID):
    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("SELECT Password FROM AcademicControlSystem.dbo.Instructor WHERE ID= ?;", (ID,))
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results
#-------------------------------------------------------------------
def select_Adminpasswords(ID):
    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("SELECT Password FROM AcademicControlSystem.dbo.[Admin] WHERE ID= ?;", (ID,))
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results
#-------------------------------------------------------------------

def select_Studpasswords(ID):
    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("SELECT Password FROM AcademicControlSystem.dbo.Student WHERE ID= ?;", (ID,))
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results
#-------------------------------------------------------------------
def get_Sid(p):

    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("SELECT ID FROM AcademicControlSystem.dbo.Student WHERE Password =?", (p,))
    id = cursor.fetchall()
    connection.close()
    return  id

#-----------------------------------------------------------------------
def get_Instid(p):
    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("SELECT ID FROM AcademicControlSystem.dbo.Instructor WHERE Password =?", (p,))

    id = cursor.fetchall()
    connection.close()
    return  id
#-----------------------------------------------------------------------
def get_Adminid(p):
    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("SELECT ID FROM AcademicControlSystem.dbo.Admin WHERE Password =?", (p,))

    id = cursor.fetchall()
    connection.close()
    return  id
#-----------------------------------------------------------------------
def student_info(id):
    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM AcademicControlSystem.dbo.Student WHERE ID= ?;", (id,))
    info = cursor.fetchall()
    connection.commit()
    connection.close()
    return info
#------------------------------------------------------------
def admin_info (id):
    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM AcademicControlSystem.dbo.Admin WHERE ID= ?;", (id,))
    info = cursor.fetchall()
    connection.commit()
    connection.close()
    return info
#-------------------------------------------------
def inst_info(id):
    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM AcademicControlSystem.dbo.Instructor WHERE ID= ?;", (id,))
    info = cursor.fetchall()
    connection.close()
    return info
#--------------------------------------------------------------------
def Update_StudentGradeDB(sID,g):
    connection = pyodbc.connect(  'DRIVER={SQL Server};'
                                  'SERVER=DESKTOP-5KRGIGR;'
                                  'DATABASE=AcademicControlSystem;'
                                  'Trusted_Connection=yes;')
    cursor = connection.cursor()

    cursor.execute("UPDATE AcademicControlSystem.dbo.Student SET grade = ? WHERE ID = ? ",  [(g), (sID)] )
    cursor.execute("SELECT * FROM AcademicControlSystem.dbo.Student")
    info = cursor.fetchall()
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    connection.close()
    return info