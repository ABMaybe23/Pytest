import pytest
from pybank.bank import Account, InsufficientAmount

@pytest.fixture
def linus_account():
    '''Returns an Account instance with customer name Linus and balance of zero'''
    return Account(name = "Linus")

@pytest.mark.parametrize("deposit,withdrawal,expected", [
    (2500, 800, 1700),
    (950, 75, 875),
])
def test_transactions(linus_account, deposit, withdrawal, expected):
    linus_account.deposit(deposit)
    linus_account.withdraw(withdrawal)
    assert linus_account.balance == expected
