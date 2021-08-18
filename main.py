
import pandas as pd
import DBconnection
import pyodbc
import pandas as pd
import numpy as np
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame, Table, Spacer, TableStyle

def logic_file(path):
    d=pd.read_csv(path)
    d.reset_index(drop=True, inplace=True)
    return d

def studReg():
    regDone = False
    sID = ''
    password = ''
    while (not regDone):
        try:
            sID = str(input("Type student ID: ")).strip().upper()
        except ValueError:
            continue
        try:
            password = str(input("Type student password:")).strip().upper()
        except ValueError:
            continue

        pstr2 = Enco(password)
        ## insert user into DB
        DBconnection.Insert_sDB(sID, pstr2)
        regDone = True
        print("##############################")
        print('Student is Registered Successfully')
        print("##############################\n")
        id = DBconnection.get_Sid(pstr2)

    student_info = DBconnection.student_info(id[0][0])
    #### Back up the new record
    Write_Csv_Student(student_info)


def  instReg():
    regDone = False
    sID = ''
    password = ''
    while (not regDone):
        try:
            instID = int(input("Type instructor ID: "))
        except ValueError:
            continue
        try:
            password = str(input("Type instructor password:")).strip().upper()
        except ValueError:
            continue

        pstr3 = Enco(password)
        ## insert user into DB
        DBconnection.Insert_instDB(instID, pstr3)
        regDone = True
        print("##############################")
        print(' Instructor is Registered Successfully')
        print("##############################\n")
        id=DBconnection.get_Instid(pstr3)

    inst_info = DBconnection.inst_info(id[0][0])
    #Back up the new record
    Write_Csv_Instructor(inst_info)


def adminReg():
    regDone = False
    ID = ''
    password = ''
    while (not regDone):
        try:
            ID = str(input("Enter LogIn ID: ")).strip().upper()
        except ValueError:
            continue
        try:
            password = str(input("Enter the password:")).strip().upper()
        except ValueError:
            continue

        pstr1 = Enco(password)
        ## insert user into DB
        DBconnection.Insert_adminDB(ID, pstr1)
        regDone = True
        print("##############################")
        print('Registered Successfully')
        print("##############################\n")
        id = DBconnection.get_Adminid(pstr1)

    admin_info = DBconnection.admin_info(id[0][0])
    # Back up the new record
    Write_Csv_Admin(admin_info)

def studRole():
    while True:
        print(" Please enter your LogIn ID and Password ")
        Done = False
        id = -1
        while (not Done):
            try:
                studID = int(input(" Enter LogIn ID: "))
            except ValueError:
                continue
            try:
                ps = str(input(" Enter password: ")).strip().upper()
            except ValueError:
                continue

            login_results = DBconnection.select_Studpasswords(studID)
            enPass = Enco(ps)
            if len(login_results) == 0:
                print('There is no such user')
            else:
                print("User name found, checking password .....")
                found = False
                for pas in login_results:
                    if (pas[0] == enPass):
                        found = True
                        id = DBconnection.get_Sid(enPass)
                        break
                if found:
                    Done = True
        print("Login successful welcome to student portal")
        print("student ID: " + str(id[0][0]))

        cont = True
        while cont:
            print(" Select following options: 1.Add course 2. exit")
            try:
                op = int(input("Chosen option: "))
            except ValueError:
                continue
            if op == 1:
                try:
                    courseID = str(input(" Enter Course ID : ")).strip().upper()
                except ValueError:
                    continue

                DBconnection.Insert_StudentClassDB(studID, courseID)
                print("##############################")
                print('Course added Successfully')
                print("##############################\n")

            else:
                exit()
            decisionMade = False
            while (not decisionMade):
                print('Do you like to go to continue? [y/n]')
                try:
                    decision = str(input(" Decision: ")).strip()
                except ValueError:
                    continue
                if decision == 'y':
                    decisionMade = True
                    cont = True
                elif decision == 'n':
                    decisionMade = True
                    cont = False
                else:
                    print('Unacceptable decision')
        break

def instRole():
    while True:
        print(" Please enter your LogIn ID and Password ")
        Done = False
        id = -1
        while (not Done):
            try:
                instID = int(input(" Enter LogIn ID: "))
            except ValueError:
                continue
            try:
                ps = str(input(" Enter password: ")).strip().upper()
            except ValueError:
                continue

            login_results = DBconnection.select_Instpasswords(instID)
            enPass = Enco(ps)
            if len(login_results) == 0:
                print('There is no such user')
            else:
                print("User name found, checking password .....")
                found = False
                for pas in login_results:
                    if (pas[0] == enPass):
                        found = True
                        id = DBconnection.get_Instid(enPass)
                        break
                if found:
                    Done = True
        print("Login successful welcome to instructors portal")
        print("Instructor ID: " + str(id[0][0]))

        cont = True
        while cont:
            print(" Select following options: 1.Update Grades 2. exit")
            try:
                op = int(input("Chosen option: "))
            except ValueError:
                continue
            if op == 1:
                try:
                    studentID = int(input(" Enter student  ID : "))
                except ValueError:
                    continue
                try:
                    g = str(input(" Enter grade : ")).strip().upper()
                except ValueError:
                    continue

                student_info=DBconnection.Update_StudentGradeDB(studentID, g)
                print("##############################")
                print('Grade updated Successfully')
                print("##############################\n")
                #### Back up the new record
                Write_Csv_Grades(student_info)
            else:
                exit()
            decisionMade = False
            while (not decisionMade):
                print('Do you like to go to continue? [y/n]')
                try:
                    decision = str(input(" Decision: ")).strip()
                except ValueError:
                    continue
                if decision == 'y':
                    decisionMade = True
                    cont = True
                elif decision == 'n':
                    decisionMade = True
                    cont = False
                else:
                    print('Unacceptable decision')
        break

def adminRole():
    while True:
        print(" Select choice 1-Register 2-Log in ")
        try:
            op = int(input("Chosen option: "))
        except ValueError:
            continue
        if op == 1:
            adminReg()
        elif op == 2:
            print(" Please enter your LogIn ID and Password ")
            Done = False
            id = -1
            while (not Done):
                try:
                    adminID = str(input(" Enter LogIn ID: ")).strip().upper()
                except ValueError:
                    continue
                try:
                    ps = str(input(" Enter password: ")).strip().upper()
                except ValueError:
                    continue

                login_results = DBconnection.select_Adminpasswords(adminID)
                enPass = Enco(ps)
                if len(login_results) == 0:
                    print('There is no such user')
                else:
                    print("User name found, checking password .....")
                    found = False
                    for pas in login_results:
                        if (pas[0] == enPass):
                            found = True
                            id = DBconnection.get_Adminid(enPass)
                            break
                    if found:
                        Done = True
            print("Login successful")
            print("Admin Id: " + str(id[0][0]))

            cont = True
            while (cont):
                print("Do you want 1.create student 2. create instructor 3.print report 4.exit")
                try:
                    op = int(input("Chosen option: "))
                except ValueError:
                    continue
                if op == 1:
                    studReg()
                elif op == 2:
                    instReg()
                elif op==3:
                    Write_Csv_report()
                else:
                    exit()
                decisionMade = False
                while ( not decisionMade):
                    print('Do you like to go to continue? [y/n]')
                    try:
                        decision = str(input(" Decision: ")).strip()
                    except ValueError:
                        continue
                    if decision == 'y':
                        decisionMade = True
                        cont = True
                    elif decision == 'n':
                        decisionMade = True
                        cont = False
                    else:
                        print('Unacceptable decision')
        break


# Encode the password
def Enco(password):
        d = logic_file('chyper-code.csv')
        counter =len(password)
        enPass = []
        while (counter>0):
            for idx, ch in enumerate(password):
                counter -= 1
                for i in d.loc[:, 'USER_TYPE']:
                    if ch==i:
                        system_convert_ch = d.loc[d['USER_TYPE'] == i, 'SYSTEM_CONVERT'].iloc[0]
                        enPass.insert(idx, system_convert_ch)

        pstr1 = ""
        # traverse in the list to make string
        for c in enPass:
            pstr1 += c
        return pstr1
#Export pdf file as a report with selected tables in database
def Write_Csv_report():
        # Report DataFrame
        connection = pyodbc.connect('DRIVER={SQL Server};'
                                    'SERVER=DESKTOP-5KRGIGR;'
                                    'DATABASE=AcademicControlSystem;'
                                    'Trusted_Connection=yes;')
        df = pd.read_sql('''SELECT s.ID as StudentID, s.grade as SudentGrade, i.ID as InstructorID FROM AcademicControlSystem.dbo.Student as s, AcademicControlSystem.dbo.Instructor as i
                    ''', con=connection)

        # Style Table
        df = df.reset_index()
        df = df.rename(columns={"index": ""})
        data = [df.columns.to_list()] + df.values.tolist()
        table = Table(data)
        table.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
        ]))

        # Components that will be passed into a Frame
        story = [Paragraph("My Report", getSampleStyleSheet()['Heading1']),
                 Spacer(1, 20),
                 table]

        # Use a Frame to dynamically align the compents and write the PDF file
        c = Canvas('report.pdf')
        f = Frame(inch, inch, 6 * inch, 9 * inch)
        f.addFromList(story, c)
        c.save()
#---------------------------------------------------------------------------------------
def Write_Csv_Grades(student_info):
        try:
            file_backup = open('data/HotBackupGrades.csv', mode='a')
            strToWrite = ''
            for item in student_info:
                strToWrite = ','.join([str(item[i]) for i in range(len(item))])
                strToWrite += '\n'
                file_backup.write(strToWrite)
                file_backup.flush()

        except FileNotFoundError:
            print("File not found")
            print("\n")
            input("Press any key:")
        finally:
            file_backup.close()


#---------------------------------------------------------------------------------------------

def Write_Csv_Student(upuser):
    try:
        file_backup = open('data/HotBackupStudent.csv', mode='a')
        strToWrite = ''
        for item in upuser:
            strToWrite = ','.join([str(item[i]) for i in range(len(item))])
            strToWrite += '\n'
            file_backup.write(strToWrite)
            file_backup.flush()

    except FileNotFoundError:
        print("File not found")
        print("\n")
        input("Press any key:")
    finally:
        file_backup.close()

def Write_Csv_Instructor(upuser):
    try:
        file_backup = open('data/HotBackupInstructor.csv', mode='a')
        strToWrite = ''
        for item in upuser:
            strToWrite = ','.join([str(item[i]) for i in range(len(item))])
            strToWrite += '\n'
            file_backup.write(strToWrite)
            file_backup.flush()

    except FileNotFoundError:
        print("File not found")
        print("\n")
        input("Press any key:")
    finally:
        file_backup.close()

def Write_Csv_Admin(upuser):
    try:
        file_backup = open('data/HotBackupAdmin.csv', mode='a')
        strToWrite = ''
        for item in upuser:
            strToWrite = ','.join([str(item[i]) for i in range(len(item))])
            strToWrite += '\n'
            file_backup.write(strToWrite)
            file_backup.flush()

    except FileNotFoundError:
        print("File not found")
        print("\n")
        input("Press any key:")
    finally:
        file_backup.close()

def Print_start_program():
    print('************************')
    print("Welcome to the academic portal")
    print('************************\n')
    print("************************")
    print("Choose option")
    print("************************")

def Start ():
    Print_start_program()
    while True:
        print(" Are you... 1.Admin 2.Student 3.Instructor ")
        try:
            op = int(input("Chosen option: "))
        except ValueError:
            continue
        if op == 1:
            adminRole()
        elif op == 2:
            studRole()
        elif op == 3:
            instRole()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
