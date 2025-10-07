class Employee:

    id:int

    name:str

    department:str

    salary:int

    def set_employee(self,id,name,department,salary):

        self.id = id

        self.name = name

        self.department = department

        self.salary = salary

    def display_employee(self):

        print(self.id,self.name,self.department,self.salary)

employee_instance = Employee()

employee_instance.set_employee(100,"ram","cs",23444)
    


