class TestAccountEnhanced:

@staticmethod 
def display_account(account):
    pin_status = "Yes" if account.pin is not None else "No"
    status = "Active" if account.is_active else "Inactive"

    print(
        f"Account #{account.account_number} | "
        f"{account.name} ({account.age} yrs) | "
        f"{account.account_type} | "
        f"₹{account.balance:.1f} | "
        f"{status} | "
        f"PIN: {pin_status}"
    )

@staticmethod
def main():

    print("=" * 60)
    print(" ENHANCED ACCOUNT TEST (BOOLEAN RETURNS)")
    print("=" * 60)

    # ---------------------------------------------------------
    # Test 1: Valid Account Creation
    # ---------------------------------------------------------
    print(">>> Test 1: Valid Account Creation")

    account1 = Account(
        "John Doe",
        25,
        "Savings",
        1000
    )

    TestAccountEnhanced.display_account(account1)

    # ---------------------------------------------------------
    # Test 2: Invalid Age
    # ---------------------------------------------------------
    print(">>> Test 2: Invalid Age (under 18)")
    print("Creating account with age 16")

    account2 = Account(
        "Young Kid",
        16,
        "Savings",
        500
    )

    print(f"Age auto-corrected to: {account2.age}")
    TestAccountEnhanced.display_account(account2)

    # ---------------------------------------------------------
    # Test 3: Invalid Account Type
    # ---------------------------------------------------------
    print(">>> Test 3: Invalid Account Type")
    print('Creating account with type "Invalid"')

    account3 = Account(
        "Test User",
        25,
        "Invalid",
        500
    )

    print(f"Account type defaulted to: {account3.account_type}")
    TestAccountEnhanced.display_account(account3)

    # ---------------------------------------------------------
    # Test 4: Minimum Balance Enforcement on Creation
    # ---------------------------------------------------------
    print(">>> Test 4: Minimum Balance Enforcement on Creation")
    print("Creating Savings account with ₹300 (below minimum)")

    account4 = Account(
        "Bob Wilson",
        25,
        "Savings",
        300
    )

    print(f"Balance auto-corrected to minimum: ₹{account4.balance:.1f}")
    TestAccountEnhanced.display_account(account4)

    # ---------------------------------------------------------
    # Test 5: Withdrawal with Minimum Balance
    # ---------------------------------------------------------
    print(">>> Test 5: Withdrawal with Minimum Balance")

    account5 = Account(
        "Alice Brown",
        30,
        "Current",
        1000
    )

    account5.set_pin("1234")

    TestAccountEnhanced.display_account(account5)

    # Successful withdrawal
    result = account5.withdraw(200)

    print(
        f"Withdrawing ₹200.0: "
        f"{'SUCCESS' if result else 'FAILED'}"
    )

    print(f"New balance: ₹{account5.balance:.1f}")

    print("After withdrawal:", end=" ")
    TestAccountEnhanced.display_account(account5)

    # Failed withdrawal because of minimum balance
    result = account5.withdraw(900)

    print(
        f"Withdrawing ₹900.0 (would leave ₹-100): "
        f"{'SUCCESS' if result else 'FAILED (Minimum balance violation)'}"
    )

    print(f"Current balance: ₹{account5.balance:.1f}")

    # ---------------------------------------------------------
    # Test 6: Account Status Management
    # ---------------------------------------------------------
    print(">>> Test 6: Account Status Management")

    account6 = Account(
        "Charlie Green",
        35,
        "Savings",
        2000
    )

    print("Initial:", end=" ")
    TestAccountEnhanced.display_account(account6)

    # Close account
    result = account6.close_account()

    print(
        f"Closing account: "
        f"{'SUCCESS' if result else 'FAILED'}"
    )

    print("After close:", end=" ")
    TestAccountEnhanced.display_account(account6)

    # Try depositing into closed account
    result = account6.deposit(500)

    print(
        f"Depositing ₹500.0 to closed account: "
        f"{'SUCCESS' if result else 'FAILED (Account inactive)'}"
    )

    # Reopen account
    result = account6.reopen_account()

    print(
        f"Reopening account: "
        f"{'SUCCESS' if result else 'FAILED'}"
    )

    print("After reopen:", end=" ")
    TestAccountEnhanced.display_account(account6)

    # ---------------------------------------------------------
    # Test 7: PIN Protection
    # ---------------------------------------------------------
    print(">>> Test 7: PIN Protection")

    account7 = Account(
        "Diana Prince",
        28,
        "Savings",
        1500
    )

    # Set PIN
    result = account7.set_pin("1234")

    print(
        f"Setting PIN 1234: "
        f"{'SUCCESS' if result else 'FAILED'}"
    )

    # Correct PIN
    result = account7.withdraw_with_pin(200, "1234")

    print(
        f"Withdrawing ₹200.0 with correct PIN (1234): "
        f"{'SUCCESS' if result else 'FAILED'}"
    )

    print(f"New balance: ₹{account7.balance:.1f}")

    # Incorrect PIN
    result = account7.withdraw_with_pin(100, "9999")

    print(
        f"Withdrawing ₹100.0 with incorrect PIN (9999): "
        f"{'SUCCESS' if result else 'FAILED (Incorrect PIN)'}"
    )

    # Account without PIN
    account8 = Account(
        "No PIN User",
        25,
        "Savings",
        1000
    )

    result = account8.withdraw_with_pin(100, None)

    print(
        f"Withdrawing ₹100.0 with PIN not set: "
        f"{'SUCCESS' if result else 'FAILED (PIN not set)'}"
    )

    # ---------------------------------------------------------
    # Test 8: All Accounts Summary
    # ---------------------------------------------------------
    print(">>> Test 8: All Accounts Summary")

    TestAccountEnhanced.display_account(account1)
    TestAccountEnhanced.display_account(account2)
    TestAccountEnhanced.display_account(account3)
    TestAccountEnhanced.display_account(account4)
    TestAccountEnhanced.display_account(account5)
    TestAccountEnhanced.display_account(account6)
    TestAccountEnhanced.display_account(account7)

    print("=" * 60)
    print(" ENHANCED TEST COMPLETED!")
    print("=" * 60)
```

if **name** == "**main**":
TestAccountEnhanced.main()
