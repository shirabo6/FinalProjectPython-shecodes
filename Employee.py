# employee

class Employee:
    
    def __init__(self, ID=None, name= None, age= None, phone_number = None):
        import re
        self.ID = ID
        self.name = name
        self.age = age
        self.phone_number = phone_number
        
        
    def update_ID_number(self):
        import re
        self.ID=str(input("please insert your ID number, 9 digits: "))
        pattern_ID = "\d{9}"
        while not re.search(pattern_ID,self.ID):
                print("invalid ID number, try again")
                self.ID = str(input("please insert your ID number, 9 digits: "))
        else:
            print("ID successfully updated")
            
    def update_name(self):
        import re
        self.name=str(input("please insert your name, first name and then last name: "))
        pattern_name = "\w+\s+\w"
        while not re.search(pattern_name,self.name):
            print("invalid name, try again")
            self.name=str(input("please insert your name, first name and then last name: "))
        else:
            print("name successfully updated")

    def update_phone_number(self):
        import re
        self.phone_number=str(input("please insert your phone number, no spaces: "))
        pattern_phone_number = "\d{10}"
        while not re.search(pattern_phone_number,self.phone_number):
            print("invalid phone number, try again")
            self.phone_number=str(input("please insert your phone number, no spaces: "))
        else:
            print("phone number successfully updated")

    def update_age(self):
        import re
        self.age=str(input("please insert your age: "))
        pattern_age = "\d"
        while not re.search(pattern_age,self.age):
            print("invalid age, try again")
            self.age=str(input("please insert your age: "))
        else:
            print("age successfully updated")

    def no_missing_data(self):
        if self.ID and self.age and self.phone_number and self.name:
            return True
        else:
            print("Parts of the data are missing")
            return False
        
        

            

    
