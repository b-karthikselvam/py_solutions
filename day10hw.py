from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self,name,account_year):
        self.name=name
        self.account_year=account_year

    def account_age(self):
        return f"Your Account is {2025 - self.account_year} years Old!" 
    
#     def __str__(self):
#         return (f"""Name of the User: {self.name}
# Year of Account Creation: {self.account_year}
# {self.account_age()}
# Role of User:{self.get_role()}""")
    
    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def get_role(self):
        return "Admin"
    def __str__(self):
        return (f"""Hello Admin
Name of the User: {self.name}
Year of Account Creation: {self.account_year}
{self.account_age()}
Role of User:{self.get_role()}
******************************""") 
    
class Guest(User):
    def get_role(self):
        return "Guest"
    def __str__(self):
        return (f"""Hello Guest!
Name of the User: {self.name}
Year of Account Creation: {self.account_year}
{self.account_age()}
Role of User:{self.get_role()}
******************************""") 

admin = Admin("karthik",2013)
guest = Guest("Hariharan",2000)

print(admin)
print(guest)


    



