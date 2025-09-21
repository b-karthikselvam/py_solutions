class Account:
    def __init__(self,name:str,balance:int):
        self._name = name
        self._balance = balance
    def __add__(self,other):
        return self._balance + other._balance
    
    def show_output(self):
        return (f"""Name:{self._name}
Balance:{self._balance}
""")
    
class SavingsAccount(Account):
    def __init__(self,name:str,balance:int):
        super().__init__(name,balance)
    
    def calculate_interest(self):
        return f"Interest in Savings Account {self._balance * 0.05}"

class CurrentAccount(Account):
    def __init__(self,name:str,balance:str):
        super().__init__(name,balance)

    def calculate_interest(self):
        return f"Interest in Current Account {self._balance * 0.02}"
    

sa = SavingsAccount("Ravi",10000)
ca = CurrentAccount("Anjali",15000)

print(sa.show_output(),sa.calculate_interest())
print(ca.show_output(),ca.calculate_interest())
print(f'Total Balance = {sa+ca}')
    




    



    