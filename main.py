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



  
  
  
