def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
       self.balance += amount
       
    def withdraw(self, amount):
            self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1
    
        