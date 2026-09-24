from app.calculations import add,subtract,multiply,divide,BankAccount
import pytest


@pytest.fixture
def zero_bank_account():
    print("Creating bank account with zero balance")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)



@pytest.mark.parametrize("a, b, expected",[
    (3,2,5),
    (5,3,8),
    (7,1,8),
    (12, 8, 20)
])
def test_add(a, b, expected):
   print("Testing add function")
   sum = add(a, b)
   assert sum == expected 

def test_subtract():
   print("Testing subtract function")
   difference = subtract(5, 3)
   assert difference == 2

def test_multiply():
    print("Testing multiply function")
    product = multiply(2, 3)
    assert product == 6

def test_divide():
    print("Testing divide function")
    quotient = divide(6, 3)
    assert quotient == 2




def test_bank_set_intial_amount():
    print("Testing bank account initial amount")
    account = BankAccount(100)
    assert account.balance == 100

def test_bank_default_amount(zero_bank_account):

   assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(50)
    assert bank_account.balance == 0

def collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55

@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (100, 50, 50),
    (50, 25, 25),
    (10000,2000, 8000)
])
#fixture is passed as an argument to the test function
#fixture+ parametrize allows us to run the same test with different data sets
def test_bank_transaction(zero_bank_account, 
                          deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected