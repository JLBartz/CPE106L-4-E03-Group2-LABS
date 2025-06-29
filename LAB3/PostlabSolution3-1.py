"""
File: bank.py
This module defines the Bank class.
"""

import pickle
import random
from savingsaccount import SavingsAccount

class Bank:
    """This class represents a bank as a collection of savings accounts."""

    def __init__(self, fileName=None):
        """Creates a new dictionary to hold the accounts.
        If a file name is provided, loads the accounts from a file."""
        self.accounts = {}
        self.fileName = fileName
        if fileName is not None:
            with open(fileName, 'rb') as fileObj:
                while True:
                    try:
                        account = pickle.load(fileObj)
                        self.add(account)
                    except EOFError:
                        break

    def __str__(self):
        """Returns the string representation of the bank sorted by account holder's name."""
        sortedAccounts = sorted(self.accounts.values())
        return "\n".join(map(str, sortedAccounts))

    def makeKey(self, name, pin):
        """Returns a key for the account."""
        return name + "/" + pin

    def add(self, account):
        """Adds the account to the bank."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes and returns the account, or None if it doesn't exist."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns the account, or None if it doesn't exist."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes and returns the interest on all accounts."""
        total = 0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def getKeys(self):
        """Returns a sorted list of keys (optional)."""
        return sorted(self.accounts.keys())

    def save(self, fileName=None):
        """Saves pickled accounts to a file."""
        if fileName is not None:
            self.fileName = fileName
        elif self.fileName is None:
            return
        with open(self.fileName, 'wb') as fileObj:
            for account in self.accounts.values():
                pickle.dump(account, fileObj)

# Test utilities

def createBank(numAccounts=5):
    """Returns a new bank with random accounts."""
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia", "Ken", "Jill", "Jack")
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank

def testAccount():
    """Test function for savings account."""
    account = SavingsAccount("Ken", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.getBalance())
    print(account.deposit(-50))
    print("Expect 600:", account.getBalance())
    print(account.withdraw(100))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(-50))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(100000))
    print("Expect 500:", account.getBalance())

def main(number=5, fileName=None):
    """Creates and prints a bank either from file or randomly."""
    if fileName:
        bank = Bank(fileName)
    else:
        bank = createBank(number)
    print(bank)

if __name__ == "__main__":
    main()
