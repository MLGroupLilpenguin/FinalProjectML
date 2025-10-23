from retail_project.connectors.employee_connector import EmployeeConnector

ec=EmployeeConnector()
ec.connect()
em=ec.login("ht@gmail.com","123")
if em==None:
    print("Login Failed!")
else:
    print("Login succesful!")
    #test get all employee
    print("List of all employees")
    ds = ec.get_all_employees()
    for emp in ds:
        print(emp)
    id = 3
    emp = ec.get_detail_infor(id)
    if emp==None:
        print("Employee not found!",id)
    else:
        print("Employee found!",id)
        print(emp)