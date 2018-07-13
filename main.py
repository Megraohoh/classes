from company import Company 
from employees import Employees 


green_co = Company("Green", "14-Aug-2016")
print(green_co.company_name)

employee_jenny = Employees("Jenny", "accountant", "14-Aug-2016")
employee_tom = Employees("Tom", "hit_man", "14-Aug-2016")
employee_elizabeth = Employees("Elizabeth", "snitch", "14-Aug-2016")
print(employee_jenny.employee_name, employee_tom.employee_name, employee_elizabeth.employee_name)