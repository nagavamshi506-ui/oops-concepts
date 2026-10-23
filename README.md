# oops-concepts
technology may grow rapidly with ai 
right now in any software the manual code is very rare every thing has done with ai but i still believe in core concepts
so that's why i started learning the oops concepts 

2026

learn about
class
objects
methods,init,self
class methods and class varioubles

learn about encapsulation
the methods and varioubles are work together to prevent direct data access through the class
the data can be accessed and manipulated through the methods created in the class
and '--' used for the data prvacy

#inheritance
today i learn about inheritance 
a child class that can use the methods and attributes of the parent class called inheritance
i had implemented inheritance code for bank_account methods

#structure

parent class(account_holder,balance)

  methods deposit,withdraw
  
childclass(parent class)

  methods to find intrest for balance
  
child class(parent class)

   methods :-to set overdraft limit for balance


#polymorphism
i understand that polymorphism means that same method name but diff functionality

and method_overriding

same method name defined in the child class which already created in the parent class 
which overrides the parent method


#abstraction
i learned about abstraction in python

it will hide unnecessary implementation details and show required data

abc use for abstract class and 
@abstractmethod use to abstract the method 

when a method is abstract in parent class

the child which is inherit from the parent class it should use the method which abstract in the parent class

developers use when they forget to define the methods in the child class


#task to implement four pillars
i had done a small task to implement the four pillars of the oop
created simple banking system using four oop concepts

Concepts implemented:

Encapsulation: Protecting account balance using private attributes and getter methods.
Inheritance: Reusing common functionality through the parent bank_account class.
Polymorphism: Implementing method overriding by redefining show_balance() in the current_account class.
Abstraction: Using ABC and @abstractmethod to define required behavior for account types.

Features implemented:

Deposit and withdrawal
Interest calculation
Overdraft facility
Account balance management
Testing the project:

Created test cases to verify expected outputs for different banking operations.

Tested edge cases, including invalid deposits, insufficient balance, and overdraft limits.
This hands-on task helped me understand how OOP concepts work in practice rather than just learning their definitions.
