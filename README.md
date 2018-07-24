# Introduction
Banking system simulation - Python OOP exercise project

Followed tutorial on: https://www.udemy.com/python-oops-beginners/

# Components
## Classes
### Abstract Class
#### Account
```python
class Account(metaclass = ABCMeta):
	@abstractmethod
	def createAccount():
		return 0
	@abstractmethod
	def authenticate():
		return 0
	@abstractmethod
	def withdraw():
		return 0
	@abstractmethod
	def deposit():
		return 0
	@abstractmethod
	def displayBalance():
		return 0
```
#### SavingsAccount, inherit Account
```python
class SavingsAccount(Account):
	def __init__(self):
		self.savingsAccounts = {}

	def createAccount(self, name, initialDeposit):
		pass

	def authenticate(self, name, accountNumber):
		pass
			
	def withdraw(self, withdrawalAmount):
		pass
    
	def deposit(self, depositAmount):
		pass
    
	def displayBalance(self):
		pass
```
