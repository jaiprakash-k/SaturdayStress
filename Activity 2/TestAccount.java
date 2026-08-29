public class TestAccount {

    public static void main(String[] args) {

        System.out.println("==================================================");
        System.out.println("  GLOBAL DIGITAL BANK - ACCOUNT TEST");
        System.out.println("==================================================");

        // 1. Creating Account
        System.out.println(">>> 1. Creating Account");

        Account account1 = new Account(
                1001,
                "John Doe",
                25,
                1000.0,
                "Savings"
        );

        System.out.println("Account created!");
        System.out.println(
                "Account #" + account1.getAccountNumber()
                + " | " + account1.getName()
                + " (" + account1.getAge() + " yrs)"
                + " | " + account1.getAccountType()
                + " | ₹" + account1.getBalance()
                + " | " + account1.getStatus()
        );

        // 2. Deposit Money
        System.out.println(">>> 2. Deposit Money");

        boolean depositResult = account1.deposit(500.0);

        System.out.println(
                "Depositing ₹500.0: "
                + (depositResult ? "SUCCESS" : "FAILED")
        );

        System.out.println("New balance: ₹" + account1.getBalance());

        boolean invalidDeposit = account1.deposit(-100.0);

        System.out.println(
                "Depositing ₹-100.0: "
                + (invalidDeposit
                    ? "SUCCESS"
                    : "FAILED (Invalid amount)")
        );

        // 3. Withdraw Money
        System.out.println(">>> 3. Withdraw Money");

        boolean withdrawResult = account1.withdraw(200.0);

        System.out.println(
                "Withdrawing ₹200.0: "
                + (withdrawResult ? "SUCCESS" : "FAILED")
        );

        System.out.println("New balance: ₹" + account1.getBalance());

        boolean insufficientWithdrawal = account1.withdraw(2000.0);

        System.out.println(
                "Withdrawing ₹2000.0: "
                + (insufficientWithdrawal
                    ? "SUCCESS"
                    : "FAILED (Insufficient balance)")
        );

        System.out.println("Current balance: ₹" + account1.getBalance());

        // 4. Creating Another Account
        System.out.println(">>> 4. Creating Another Account");

        Account account2 = new Account(
                1002,
                "Jane Smith",
                30,
                2000.0,
                "Current"
        );

        System.out.println(
                "Account #" + account2.getAccountNumber()
                + " | " + account2.getName()
                + " (" + account2.getAge() + " yrs)"
                + " | " + account2.getAccountType()
                + " | ₹" + account2.getBalance()
                + " | " + account2.getStatus()
        );

        // 5. All Accounts
        System.out.println(">>> 5. All Accounts");

        System.out.println(
                "Account #" + account1.getAccountNumber()
                + " | " + account1.getName()
                + " (" + account1.getAge() + " yrs)"
                + " | " + account1.getAccountType()
                + " | ₹" + account1.getBalance()
                + " | " + account1.getStatus()
        );

        System.out.println(
                "Account #" + account2.getAccountNumber()
                + " | " + account2.getName()
                + " (" + account2.getAge() + " yrs)"
                + " | " + account2.getAccountType()
                + " | ₹" + account2.getBalance()
                + " | " + account2.getStatus()
        );

        System.out.println("==================================================");
        System.out.println("  TEST COMPLETED!");
        System.out.println("==================================================");
    }
}