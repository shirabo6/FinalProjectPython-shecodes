# Attendance file


### list of all rashumot:
##import sqlite3
##conn = sqlite3.connect('TryEmp.db')
##c = conn.cursor()
##EmpListSTR= []
##for row in c.execute('''SELECT cast(ID_number as integer) FROM employees'''):
##       EmpListSTR.append(str(row[0])) 
##conn.close()
###print(EmpListSTR)

LogList = []


def Add_Entery(ID_number):
        n = str(ID_number)
        import sqlite3
        conn = sqlite3.connect('TryEmp.db')
        c = conn.cursor()
        EmpListSTR= []
        for row in c.execute('''SELECT cast(ID_number as integer) FROM employees'''):
              EmpListSTR.append(str(row[0]))
        conn.close()
        
        if n not in EmpListSTR:
            print("Employee is unrecognized")
        else:
            from datetime import datetime
            print("Welcome!\nhave a nice day!")
            Enter= datetime.now()
            Month= Enter.month
            Date= str(Enter.day) + '/' +str(Month) + '/' + str(Enter.year)
            print("You entered at: " + str(Enter.strftime( "%d/%m/%Y %H:%M:%S")))
            conn = sqlite3.connect('TryLog.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS enter
             (ID_number text, Month text, Date text , Enter text)''')
            c.execute("INSERT INTO enter VALUES (?,?,?,?)",(n, str(Month), str(Date) ,str(Enter)))
            conn.commit()
            conn.close()

            
def Add_Exit(ID_number):
        n = str(ID_number)
        import sqlite3
        conn = sqlite3.connect('TryEmp.db')
        c = conn.cursor()
        EmpListSTR= []
        for row in c.execute('''SELECT cast(ID_number as integer) FROM employees'''):
              EmpListSTR.append(str(row[0]))
        conn.close()

        if n not in EmpListSTR:
            print("Employee is unrecognized")
        else:
            from datetime import datetime
            print("GoodBye!\nhave a nice day!")
            Exit= datetime.now()
            Month= Exit.month
            Date= str(Exit.day) + '/' +str(Month) + '/' + str(Exit.year)
            print("You exited at: " + str(Exit.strftime( "%d/%m/%Y %H:%M:%S")))

            conn = sqlite3.connect('TryLog.db')
            c = conn.cursor()
            for row in c.execute(''' SELECT * FROM enter '''):
                   LogList.append([row[0],row[2],row[3]])            
            for rashuma in LogList:
                    if rashuma[0] == n and rashuma[1] == Date:
                            Enter = datetime.strptime(rashuma[2], '%Y-%m-%d %H:%M:%S.%f')
            if Exit and Enter:
                 TimeWorked = Exit - Enter
            conn.close()
        
            conn = sqlite3.connect('TryLog.db')
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS exit
             (ID_number text, Month text, Date text, Exit text , TimeWorked)''')
            c.execute("INSERT INTO exit VALUES (?,?,?,?,?)",(n, str(Month), str(Date) ,str(Exit), str(TimeWorked)))
            conn.commit()
            conn.close()
            
            


def PrintByID(ID):
        n = str(ID)
        import sqlite3
        conn = sqlite3.connect('TryEmp.db')
        c = conn.cursor()
        EmpListSTR= []
        for row in c.execute('''SELECT cast(ID_number as integer) FROM employees'''):
              EmpListSTR.append(str(row[0]))
        conn.close()

        Log=[]
        conn = sqlite3.connect('TryLog.db')
        c = conn.cursor()

        if n not in EmpListSTR:
            print("Employee is unrecognized")
        else:
               print("All Attendance log of: " + n)
               c.execute('''DROP TABLE IF EXISTS attendance''')
               c.execute('''CREATE TABLE IF NOT EXISTS attendance
                    (ID_number text, Month text, Date text,Enter text, Exit text , TimeWorked)''')
               c.execute('''INSERT INTO attendance SELECT enter.* , exit.Exit, exit.TimeWorked FROM enter 
                    INNER JOIN exit ON enter.ID_number = exit.ID_number AND exit.Date= enter.Date''')
               conn.commit()

               for row in c.execute('''SELECT * FROM attendance WHERE ID_number =''' +n +''' ORDER BY Date '''):
                      Log.append([n,row[2] , row[5]])  
               conn.close()

               from prettytable import PrettyTable
               t = PrettyTable(['ID number','Date' ,'Time worked'])
               for i in Log:
                   t.add_row([i[0] , i[1] , i[2]])
               print(t) 
                                
#PrintByID(207524968)

def PrintByMonth(month):
        Log=[]
        import sqlite3
        conn = sqlite3.connect('TryLog.db')
        c = conn.cursor()
        m = str(month)

        print("All Attendance log at month: " + m)
        c.execute('''DROP TABLE IF EXISTS attendance''')
        c.execute('''CREATE TABLE IF NOT EXISTS attendance
             (ID_number text, Month text, Date text,Enter text, Exit text , TimeWorked)''')
        c.execute('''INSERT INTO attendance SELECT enter.* , exit.Exit, exit.TimeWorked FROM enter 
             INNER JOIN exit ON enter.ID_number = exit.ID_number AND exit.Date= enter.Date''')
        conn.commit()

        for row in c.execute('''SELECT * FROM attendance WHERE Month =''' +m +''' ORDER BY Date '''):
               Log.append([row[0] ,row[2] , row[5]])  
        conn.close()

        from prettytable import PrettyTable
        t = PrettyTable(['ID number','Date' ,'Time worked'])
        for i in Log:
            t.add_row([i[0] , i[1] , i[2]])
        print(t) 

#PrintByMonth(8)


def PrintLateWorkers():

        Log=[]
        import sqlite3
        conn = sqlite3.connect('TryLog.db')
        c = conn.cursor()

        print("All Attendance of workers who came late, after 9:30: " )
        c.execute('''DROP TABLE IF EXISTS attendance''')
        c.execute('''CREATE TABLE IF NOT EXISTS attendance
             (ID_number text, Month text, Date text,Enter text, Exit text , TimeWorked)''')
        c.execute('''INSERT INTO attendance SELECT enter.* , exit.Exit, exit.TimeWorked FROM enter 
             INNER JOIN exit ON enter.ID_number = exit.ID_number AND exit.Date= enter.Date''')
        conn.commit()

        for row in c.execute('''SELECT * FROM attendance'''):
               h=int(row[3][11:13])
               m=int(row[3][14])
               if (h==9 and m>=3) or (h>9):
                      Log.append([row[0] ,row[2] , row[3]])  
        conn.close()

        from prettytable import PrettyTable
        t = PrettyTable(['ID number','Date' ,'Enter Time'])
        for i in Log:
            t.add_row([i[0] , i[1] , i[2]])
        print(t)

#PrintLateWorkers()


 











                
        










