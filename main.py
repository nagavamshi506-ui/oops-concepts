#create a class
class student:
  #class variouble
  college='kits college'
  #defining the init
  #self refers to the  current object
  #name and age are the arguments
  def __init__(self,name,age,roll_no):
    #current object data
    #instance variouble
    self.name=name
    self.age=age
    self.roll_no=roll_no
    #creating methods
  def fullname(self):
    print(f"naga{self.name}")
name='vamshi'
age=20
roll_no=257301
#creating the object
#student1 is the object
#the student1 object will acces the student class properties
student1=student(name,age,roll_no)
student2=student('pavann',20,21)
#calling the method for fullname
student1.fullname()
print(f'roll_no:-{student1.roll_no}')
print(f'age:-{student1.age}')
print(student1.college)
print("-"*20)
print(f'Nmae:-{student2.name}')
print(f'roll_no:-{student2.roll_no}')
print(f'age:-{student2.age}')
print(student2.college)


# encapsulation for student data
#student marks update
class student:
  def __init__(self,name,marks):
    self.__name=name
    self.__marks=marks
  def get_marks(self):
    print(self.__marks)
  def updatemarks(self,new_marks):
    if new_marks <=100 and new_marks>0:
      self.__marks=new_marks
    else:
      print('invaild data')
student1=student('vamshi',100)
student1.get_marks()
student1.updatemarks(800)
student1.updatemarks(80)
student1.get_marks()



#inheritance
class Bank_account:
  def __init__(self,account_holder,balance):
    self.account_holder=account_holder
    self.balance=balance
    print(f'account holder name = {self.account_holder}')
    print(f'{account_holder} balance is = {self.balance}')
  def deposit(self,money):
    print(f' balance = {self.balance} ')
    if money>0:
      self.balance+=money
      print(f'balance after deposit = {self.balance}')
    else:
      print('invalid deposit')
  def withdraw(self,money):
    if money <= self.balance:
      self.balance-=money
      print(f'after withdraw the balance = {self.balance}')
    else:
      print('insufficent balance')
class savings_account(Bank_account):
  def calculate_intrest(self,intrest_rate):
    intrest= (self.balance*intrest_rate/100)
    print(intrest)
class current_account(Bank_account):
  def over_draft(self,withdraw_amount,overdraft_limit):
    if withdraw_amount<self.balance:
      self.balance = self.balance-withdraw_amount
      print(f'overdraft_limit is {overdraft_limit}')
      print(f'remaining balance is {self.balance}')
    elif withdraw_amount<= self.balance + overdraft_limit:
          overdraft_limit-=(withdraw_amount-self.balance)
          self.balance = (self.balance - withdraw_amount)
          print(f'remaining overdraft_limit is {overdraft_limit}')
          print(f'the balance = {self.balance}')
    else:
      print('insufficent_funds')
student1=savings_account('vamshi',3000)
student1.deposit(2000)
student1.withdraw(1000)
student1.calculate_intrest(5)
student2=current_account('shiva',4000)
student2.over_draft(2000,2000)


#polymorphism
class full_time_employee:
  def __init__(self,no_of_months,salary):
    self.no_of_months=no_of_months
    self.salary=salary
  def calculate_salary(self):
    if self.no_of_months >= 1 and self.no_of_months < 12:
      print(self.salary * self.no_of_months)
    else:
      print('invaild months')
class part_time_employee(full_time_employee):
  def __init__(self,hours,hours_rate):
    self.hours = hours
    self.hours_rate = hours_rate
  def calculate_salary(self):
    if self.hours>0 and self.hours<=24:
      print(self.hours*self.hours_rate)
    else:
      print('invaild hours')
class contract_based(full_time_employee):
  def __init__(self,days,daily_rate):
    self.days=days
    self.daily_rate=daily_rate
  def calculate_salary(self):
    if self.days >0 and self.days<=364:
      print(self.days*self.daily_rate)
    else:
      print('invaild data')
#objects
vamshi=full_time_employee(5,20000)
pranay=part_time_employee(4,2000)
shiva=contract_based(30,3000)

employee=[vamshi,pranay,shiva]
for emp in employee:
  emp.calculate_salary()



#abstraction


from abc import ABC, abstractmethod
class payment(ABC):
  @abstractmethod
  def process_payment(self,amount):
    pass
  def validate_payment(self,amount):
    if amount<0:
      print('insufficent money')
    else:
      print(f'the amount is {amount}')
class upi_payment(payment):
  def process_payment(self,amount):
    if amount > 10000 :
      print ('limit exceed')
    elif amount <=0:
      print('invaild money')
    else:
      print(f'the upi_payment is {amount}')
class card_payment(payment):
  def process_payment(self,amount):
    if amount > 50000:
      print('limit exceed')
    elif amount <=0:
      print('invaild money')
    else:
      print(f'the card_payment is {amount}')
class hand_payment(payment):
  def process_payment(self,amount):
    if amount > 5000:
      print('limit exceed')
    elif amount <=0:
      print('invaild money')
    else:
      print(f'the hand_payment is {amount}')
person1 = upi_payment()
person2 = card_payment()
person3 = hand_payment()

person1.process_payment(6000)
person2.process_payment(16000)
person3.process_payment(6000)


      
      

#simple task to implement all four pillars of oop concepts
from abc import ABC , abstractmethod
class bank_account(ABC):
  def __init__ (self,balance,account_holder,account_number):
    self.__balance = balance
    self.account_holder=account_holder
    self.account_number = account_number
  @abstractmethod
  def charges_collection(self):
    pass
  def show_balance(self):
    print(f'balance before any transaction = {self.__balance}')
  def deposit(self,money):
    if money > 0:
     self.__balance+=money
    elif money <=0:
      print('invaild money')
    print(f'account balance = {self.__balance}')
    
  def get_balance(self):
    return self.__balance
    
  def withdraw(self,money):
    if money <=0:
      print('invaild money')
    elif money<=self.__balance:
      self.__balance-=money
      print(f'the remaining balance = {self.__balance}')
      print(f'amount withdraw = {money}')
    else:
      print('insufficent balance')
      
  def reduce_balance(self,amount):
    self.__balance-=amount
    
  def add_balance(self,amount):
    self.__balance+=amount
    
class savings_account(bank_account):
  def charges_collection(self):
    self.reduce_balance(10)
    print('charges had been collected = $10')
  def calculate_intrest(self,intrest_rate,time):
    intrest=(self.get_balance() * intrest_rate * time)/100
    print(f'the intrest amount = {intrest}')

    
class current_account(bank_account):
  def __init__(self,balance,account_holder,account_number,overdraft_limit):
    super().__init__(balance,account_holder,account_number)
    self.overdraft_limit=overdraft_limit
  
  def overdraft(self,withdraw):
    if withdraw <=0:
      print('invaild money')

    elif withdraw <= self.get_balance():
      self.reduce_balance(withdraw)
      print(f'amount withdrawed = {withdraw}')
      print(f'bank balance = {self.get_balance()} ')
      print(f'remainimg overdraft_limit = {self.overdraft_limit}')

    elif self.get_balance() <= 0 and withdraw <= self.overdraft_limit:
      self.overdraft_limit-= withdraw
      self.reduce_balance(withdraw)
      print(f'amount withdrawed = {withdraw}')
      print(f'bank balance = {self.get_balance()} ')
      print(f'remainimg overdraft_limit = {self.overdraft_limit}')
      
    elif withdraw <= (self.get_balance()+ self.overdraft_limit):
      extra=(withdraw-self.get_balance())
      self.overdraft_limit-=(withdraw-self.get_balance())
      self.reduce_balance(withdraw)
      print(f'amount withdrawed = {withdraw}')
      print(f'bank balance = {self.get_balance()} ')
      print(f'remainimg overdraft_limit = {self.overdraft_limit}')
      
    elif withdraw>(self.get_balance() + self.overdraft_limit):
      print('insufficent balance')
  def charges_collection(self):
    self.reduce_balance(10)
    print('the charges had been collected = $10')
  def show_balance(self):
    print(f'balance after some transaction = {self.get_balance()}')




# Test 1: Create accounts
s1 = savings_account(1000, "Tony", 101)
s1.show_balance()

# Test 2: Deposit valid money
s1.deposit(500)

# Test 3: Deposit invalid money
s1.deposit(-200)

# Test 4: Withdraw valid money
s1.withdraw(300)

# Test 5: Withdraw more than balance
s1.withdraw(5000)

# Test 6: Calculate interest
s1.calculate_intrest(5, 2)

# Test 7: Collect charges
s1.charges_collection()
s1.show_balance()

# Test 8: Current account overdraft
c1 = current_account(1000, "Ravi", 102, 500)
c1.overdraft(1200)

# Test 9: Use remaining overdraft
c1.overdraft(200)

# Test 10: Exceed remaining overdraft
c1.overdraft(200)

# Test 11: Invalid overdraft withdrawal
c1.overdraft(-100)

# Test 12: Test method overriding
c1.show_balance()

# Test 13: Test encapsulation
print(s1.get_balance())

# Test 14: Try direct private attribute access
print(s1.__balance)

# Test 15: Test abstraction
b1 = bank_account(1000, "Sam", 103)
      
  




    
      
  



  
  
  
