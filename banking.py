# import for abstract method
from abc import ABCMeta, abstractmethod

# abstract methods
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


class SavingsAccount(Account):
	def __init__(self):
		self.savingsAccounts = {}

	def createAccount(self, name, initialDeposit):
		self.accountNumber = randint(10000, 99999)
		self.savingsAccounts[self.accountNumber] = [name, initialDeposit]

	def authenticate(self, name, accountNumber):
		# if account number is in data list
		if accountNumber in self.savingsAccounts.keys():
			# if account number and name matches
			if self.savingsAccounts[accountNumber][0] == name:
				print("Authentication Successful") 
				# set account number
				self.accountNumber = accountNumber
				return True
			# if account number and name doesn't match
			else:
				print("Authentication Failed")
				return False
		# if account doesn't exist in data list
		else:
			print("Authentication Failed")
			return False
			
	def withdraw(self, withdrawalAmount):
		pass
	def deposit(self, depositAmount):
		pass
	def displayBalance(self):
		pass