class AccountEnhanced:

    def __init__(self, accountNumber, name, age,
                 initialBalance, accountType):

        self.accountNumber = accountNumber
        self.name = name

        # Age validation
        if age < 18:
            self.age = 18
        else:
            self.age = age

        # Account type validation
        if accountType not in ["Savings", "Current"]:
            self.accountType = "Savings"
        else:
            self.accountType = accountType

        # Minimum balance rules
        if self.accountType == "Savings":
            minimumBalance = 500.0
        else:
            minimumBalance = 1000.0

        if initialBalance < minimumBalance:
            self.balance = minimumBalance
        else:
            self.balance = initialBalance

        self.status = "Active"
        self.pin = None

    def deposit(self, amount):
        # Check account status
        if self.status != "Active":
            return False

        # Check valid amount
        if amount <= 0:
            return False

        self.balance += amount
        return True

    def withdraw(self, amount, pin):
        # Check account status
        if self.status != "Active":
            return False

        # Verify PIN
        if not self.verifyPin(pin):
            return False

        # Check valid amount
        if amount <= 0:
            return False

        # Determine minimum balance
        if self.accountType == "Savings":
            minimumBalance = 500.0
        else:
            minimumBalance = 1000.0

        # Check minimum balance after withdrawal
        if self.balance - amount < minimumBalance:
            return False

        self.balance -= amount
        return True

    def closeAccount(self):
        if self.status == "Inactive":
            return False

        self.status = "Inactive"
        return True

    def reopenAccount(self):
        if self.status == "Active":
            return False

        self.status = "Active"
        return True

    def setPin(self, pin):
        # PIN must be exactly 4 digits
        if pin < 1000 or pin > 9999:
            return False

        self.pin = pin
        return True

    def verifyPin(self, pin):
        if self.pin is None:
            return False

        return self.pin == pin

    def hasPin(self):
        return self.pin is not None

    def getAccountNumber(self):
        return self.accountNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getBalance(self):
        return self.balance

    def getAccountType(self):
        return self.accountType

    def getStatus(self):
        return self.status

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age