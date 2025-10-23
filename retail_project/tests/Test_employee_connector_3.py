
from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.models.employee import Employee

ec=EmployeeConnector()
ec.connect()
emp=Employee()
emp.ID = 7
emp.EmployeeCode="EMP757"
emp.Name="Long2"
emp.Phone="01256789"
emp.Email="he2@gmail.com"
emp.Password="123"
emp.IsDeleted=0
result=ec.update_one_employee(emp)
if result >0:
    print("Insert Successful!")
else:
    print("Insert Failed!")