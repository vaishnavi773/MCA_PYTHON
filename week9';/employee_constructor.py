class Employee:
    company_name="ABCD"
    Location="calicut"
    def __init__(self,id,name,salary):
        self.emp_id=id
        self.emp_name=name
        self.emp_salary=salary
    def detail(self):
        print(self.emp_id,self.emp_name,self.emp_salary)
      
emp1= Employee(101,"Manu",50000)
print("company name=",Employee.company_name,"\nlocation=",Employee.Location)  
emp2= Employee(102,"Hari",25000)
emp1.detail()
emp2.detail()

    
