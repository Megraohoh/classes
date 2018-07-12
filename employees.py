# Create a class that contains information about employees of a company and define methods to get/set employee name, job title, and start date.
class Employees():
    """This represents employees of a company
    """
    def __init__(self, employee_name, job_title, start_date):
        self.employee_name = employee_name
        self.job_title = job_title
        self.start_date = start_date

    def set_employee_name():
        self.employee_name = employee_name

    def get_employee_name(): 
        return self.employee_name   

    def set_employee_job_title():
        self.job_title = job_title

    def get_employee_job_title():
        return self.job_title

    def set_employee_start_date():
        self.start_date = start_date

    def get_employee_start_date():
        return self.start_date


class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    # Add the remaining methods to fill the requirements above