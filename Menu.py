# menu

from Employee import Employee
import Functions as Functions
Functions.FirstRun()
import Attendance as Attendance


########################################
def Manage_employees_list():
    
        print(''' choose specificly:

                    1. Add an employee manualy
                    2. Add an employee from csv
                    3. Delete employee manualy
                    4. Delete employee form csv
                    5. Print  employees list
                    
                    ''')
        SecondUserChoice =int(input())
        while SecondUserChoice not in [1,2,3,4,5]:
            print("invalid choice, try again")
            SecondUserChoice = int(input())
            
        if SecondUserChoice==1:
            ID= int(input("Employee's ID number is: "))
            return Functions.Add_Employee(ID)
        elif SecondUserChoice==2:
            path= input("Insert csv file path: ")
            return Functions.Add_Employee_csv(path)
        elif SecondUserChoice==3:
            ID=int(input("insert employees's ID: "))
            return Functions.Delete_Employee(ID)
        elif SecondUserChoice==4:
            path= input("Insert csv file path: ")
            return Functions.Delete_Employee_csv(path)
        elif SecondUserChoice ==5:
            return Functions.PrintList()
########################################
       
########################################
def Add_entery():
        ID= int(input("Employee's ID number is: "))
        return Attendance.Add_Entery(ID)
########################################

########################################
def Add_exit():
    ID= int(input("Employee's ID number is: "))
    return Attendance.Add_Exit(ID)
########################################

########################################
def Print_attendance_log():
    print(''' choose specificly:

                1. Print attendance report by Employee ID
                2. Print attendance report by month
                3. Print reports of all late workers
                
                
                ''')
    SecondUserChoice=int(input())
    while SecondUserChoice not in [1,2,3]:
        print("invalid choice, try again")
        SecondUserChoice = int(input())

    if SecondUserChoice == 1:
        ID= int(input("Employee's ID number is: "))
        return Attendance.PrintByID(ID)
    elif SecondUserChoice == 2:
        month= int(input("For which month? (January=1,...,December=12) "))
        return Attendance.PrintByMonth(month)
    elif SecondUserChoice == 3:
        return Attendance.PrintLateWorkers()
    
########################################

# a dictionary maps the first choice options and call the fitted function
FirstChoice = {1: Manage_employees_list ,
               2: Add_entery,
               3: Add_exit,
               4: Print_attendance_log}

########################################
def __main__():
        # run main code
        more = "YES"
        while more == "YES":
            
            print("="*45)
            print('''Hi, what would you like to do?

                            1. Manage employees list
                            2. Add entery
                            3. Add exit
                            4. Print attendance log

                            ''')

            FirstUserChoice = int(input())
            print("="*45)
            
            def InvalidFirstChoice():
                    print("invalid choice, try again")
                    FirstUserChoice = int(input())
                    FirstChoice.get(FirstUserChoice,InvalidFirstChoice)()
                    
                    
            FirstChoice.get(FirstUserChoice,InvalidFirstChoice)()
            ########################################

            more= input(''' Do you want to go back to the menu and select another task?

                        type YES / NO
                        
                        ''' ).upper()






