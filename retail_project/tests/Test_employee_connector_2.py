
from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.models.employee import Employee

ec=EmployeeConnector()
ec.connect()
emp=Employee()
emp.EmployeeCode="EMP888"
emp.Name="Long"
emp.Phone="0123456789"
emp.Email="he@gmail.com"
emp.Password="123"
emp.IsDeleted=0
result=ec.insert_one_employee(emp)
if result >0:
    print("Insert Successful!")
else:
    print("Insert Failed!")