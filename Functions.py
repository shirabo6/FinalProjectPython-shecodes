# functions

from Employee import Employee
             

EmpList=[]
EmpListSTR = []
    
def PrintList():
    emp=[]
    import sqlite3
    conn = sqlite3.connect('TryEmp.db')
    c = conn.cursor()

    for row in c.execute('''SELECT * FROM employees '''):
        emp.append([row[0] ,row[1] , row[2], row[3]])
    conn.close
    
    from prettytable import PrettyTable
    t = PrettyTable(['ID number', 'Name', 'Age' , 'Phone Number'])
    for i in emp:
        t.add_row([i[0], i[1], i[2], i[3]])
    print(t)
  
def Add_Employee(ID_number):

    emp=[]
    import sqlite3
    conn = sqlite3.connect('TryEmp.db')
    c = conn.cursor()

    for row in c.execute('''SELECT * FROM employees '''):
        emp.append(row[0])
    conn.close
    a= str(ID_number)
    while a in emp:
        print("Employee already exist")
        return None

    print("when adding a new Employee, Make sure to fill all data required")

    ID_number = Employee()
    ID_number.update_ID_number()
    ID_number.update_name()
    ID_number.update_age()
    ID_number.update_phone_number()

    if ID_number.ID and ID_number.age and ID_number.name and ID_number.phone_number:
        # insert into database
        import sqlite3
        conn = sqlite3.connect('TryEmp.db')
        c = conn.cursor()
        sql = "INSERT INTO employees VALUES(?,?,?,?)"
        val= []
        val.append((str(ID_number.ID),str(ID_number.name),str(ID_number.age),str(ID_number.phone_number)))
        c.executemany(sql, val)
        conn.commit()
        conn.close()

        n = str(ID_number.ID)
        EmpListSTR.append(n)
        EmpList = []
        EmpList.append(ID_number)
        
    else:
        print("Parts of the data are missing")
        
def Add_Employee_csv(path_file):
    import csv
    import re
    # pattern to check the validity of the data
    pattern_ID = "\d{9}"
    pattern_name = "\w+\s+\w"
    pattern_age = "\d"
    pattern_phone_number = "\d{10}"
    #
    print("this function used to read from csv files. delimiter is ,")
    with open(path_file , "r") as csv_file:
        csv_read= csv.reader(csv_file, delimiter=",")
        line = 0
        for row in csv_read:
            if line == 0:
                print(f'Column names are {", ".join(row)}')
                line+=1
            else:
                line+=1 
                if row[0] and re.search(pattern_ID,row[0]):
                    emp=[]
                    import sqlite3
                    conn = sqlite3.connect('TryEmp.db')
                    c = conn.cursor()
                    for R in c.execute('''SELECT * FROM employees '''):
                        emp.append(R[0])
                    conn.close
                    a= str(row[0])
                    # check whether employee already exists
                    while a in emp:
                        print("Employee already exists")
                    else:
                        ID_number =Employee()
                        ID_number.ID = str(row[0])
                        if row[1] and re.search(pattern_name ,row[1]):
                            ID_number.name = str(row[1])
                        else:
                            print("Employee's name is missing or not valid")
                        if row[2] and re.search(pattern_age,row[2]):
                            ID_number.age = str(row[2])
                        else:
                            print("Employee's age is missing or not valid")
                        if row[3] and re.search(pattern_phone_number,row[3]):
                            ID_number.phone_number = str(row[3])
                        else:
                            print("Employee's phone_number is missing or not valid")

                        if ID_number.ID and ID_number.age and ID_number.name and ID_number.phone_number:
                        # insert into database
                            import sqlite3
                            conn = sqlite3.connect('TryEmp.db')
                            c = conn.cursor()
                            sql = "INSERT INTO employees VALUES(?,?,?,?)"
                            val= []
                            val.append((str(ID_number.ID),str(ID_number.name),str(ID_number.age),str(ID_number.phone_number)))
                            c.executemany(sql, val)
                            conn.commit()
                            conn.close()
                            
                            n = str(ID_number.ID)
                            EmpListSTR.append(n)
                            EmpList = []
                            EmpList.append(ID_number)
                            print("Employee successfully added")

                else:
                    print("ID number is not valid, can not add Employee")


def Delete_Employee(ID_number):
    n = str(ID_number)
    try:
        import sqlite3
        conn = sqlite3.connect('TryEmp.db')
        c = conn.cursor()
        st= '''DELETE FROM employees WHERE ID_number = ? '''
        c.execute(st, (n,))
        conn.commit()
        conn.close()

    except ValueError:
        print("Employee's ID do not found, thus can not be removed")
    else:
        print("Employee removed")
        
def Delete_Employee_csv(path_file):
    import csv
    with open(path_file , "r") as csv_file:
        csv_read= csv.reader(csv_file, delimiter=",")
        line = 0
        for row in csv_read:
            if line == 0:
                print(f'Column names are {", ".join(row)}')
                line+=1
            else:
                n = str(row[0])
                try:
                    import sqlite3
                    conn = sqlite3.connect('TryEmp.db')
                    c = conn.cursor()
                    st= '''DELETE FROM employees WHERE ID_number = ? '''
                    c.execute(st, (n,))
                    conn.commit()
                    conn.close()
                except ValueError:
                    print("Employee's ID do not found, thus can not be removed")
                else:
                    print("Employee removed")
                    
##def Save_Data():
##    # Save EmpList to a database 
##    import sqlite3
##    conn = sqlite3.connect('TryEmp.db')
##    c = conn.cursor()
##    
##    c.execute('''CREATE TABLE IF NOT EXISTS employees
##                 ( ID_number text, Name text, Age text, Phone_number text)''')
##
##    sql = "INSERT INTO employees VALUES(?,?,?,?)"
##    val= []
##    count=0
##    for i in EmpList:
##        count+=1
##        val.append((str(i.ID),str(i.name),str(i.age),str(i.phone_number)))
##    #print(val)
##    c.executemany(sql, val)
##    conn.commit()
##    #print('We have inserted', c.rowcount, 'records to the table.')
##    conn.close()

def FirstRun():
    import sqlite3
    conn = sqlite3.connect('TryEmp.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees
                 ( ID_number text, Name text, Age text, Phone_number text)''')
    conn.commit()
    conn.close()

    

'''
# check:

Add_Employee(111111111)
Add_Employee_csv('workers.csv')
PrintList()

#Delete_Employee_csv('workers.csv')
#Delete_Employee(111111111)
PrintList()
Save_Data()
   
'''
        
        
            
    
  
