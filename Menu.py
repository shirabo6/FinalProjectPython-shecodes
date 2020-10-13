# menu

from Employee import Employee
import Functions as F
F.FirstRun()
import Attendance as A

more = "YES"

########################################
while more == "YES":
    print("="*45)
    print('''Hi, what would you like to do?

                    1. Manage employees list
                    2. Add entery
                    3. Add exit
                    4. Print attendance log

                    ''')

    c1 = int(input())
    while c1 not in [1,2,3,4]:
        print("invalid choice, try again")
        c1 = int(input())
    print("="*45)
    ########################################



    ########################################   
    if c1 == 1:
        
        print(''' choose specificly:

                    1. Add an employee manualy
                    2. Add an employee from csv
                    3. Delete employee manualy
                    4. Delete employee form csv
                    5. Print  employees list
                    
                    ''')
        c2=int(input())
        while c2 not in [1,2,3,4,5]:
            print("invalid choice, try again")
            c2 = int(input())

        if c2==1:
            i= int(input("Employee's ID number is: "))
            F.Add_Employee(i)
            #F.Save_Data()
        elif c2==2:
            p= input("Insert csv file path: ")
            F.Add_Employee_csv(p)
            #F.Save_Data()
        elif c2==3:
            d=int(input("insert employees's ID: "))
            F.Delete_Employee(d)
            #F.Save_Data()
        elif c2==4:
            f= input("Insert csv file path: ")
            F.Delete_Employee_csv(f)
            #F.Save_Data()
        elif c2 ==5:
            F.PrintList()
    ########################################

        
    ########################################
    elif c1 == 2:
        i= int(input("Employee's ID number is: "))
        A.Add_Entery(i)
    ########################################

    ########################################
    elif c1 == 3:
        i= int(input("Employee's ID number is: "))
        A.Add_Exit(i)
    ########################################

    ########################################
    elif c1 == 4:
        print(''' choose specificly:

                    1. Print attendance report by Employee ID
                    2. Print attendance report by month
                    3. Print reports of all late workers
                    
                    
                    ''')
        c2=int(input())
        while c2 not in [1,2,3]:
            print("invalid choice, try again")
            c2 = int(input())

        if c2 == 1:
            i= int(input("Employee's ID number is: "))
            A.PrintByID(i)
        elif c2 == 2:
            m= int(input("for which month? (January=1,...,December=12) "))
            A.PrintByMonth(m)
        elif c2 == 3:
            A.PrintLateWorkers()
        
    ########################################

    more= input(''' Do you want to go back to the menu and select another task?

                type YES / NO
                
                ''' ).upper()
