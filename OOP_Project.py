class Bank():
    balance = 0
    loan_amount = 0
    user_accounts = {}
    admin_accounts = {}
    loan = True


class user_details():
    def __init__(self, name, password) -> None:
        self.name = name
        self.password = password


class User(user_details, Bank):
    def __init__(self, name, Ac_number, password) -> None:
        self.name = name
        self.password = password
        self.Ac_number = Ac_number
        if Ac_number not in Bank.user_accounts:
            Bank.user_accounts[Ac_number] = {
                "name": name, "password": password, "balance": 0, 'transaction_history': []}
        self.balance = 0
        self.loan = 0
        super().__init__(name, password)


    def check_balance(self):
        print(f"\nYour total BALANCE is: {
              Bank.user_accounts[self.Ac_number]["balance"]}\n")

    def deposit(self, amount):
        if amount > 0:
            Bank.balance += amount
            rem = Bank.user_accounts[self.Ac_number]["balance"]
            rem += amount
            Bank.user_accounts[self.Ac_number]["balance"] = rem
            transaction = {"type": "Deposit", "amount": amount}
            Bank.user_accounts[self.Ac_number]["transaction_history"].append(
                transaction)
            print(f"\n{amount} Deposited Successfully.\n")
        else:
            print("\n Invalid Amount !!! \n")

    def withdraw(self, amount):
        if amount <= Bank.user_accounts[self.Ac_number]["balance"] and amount > 0 and amount <= Bank.balance:
            Bank.balance -= amount
            rem = Bank.user_accounts[self.Ac_number]["balance"]
            rem -= amount
            Bank.user_accounts[self.Ac_number]["balance"] = rem
            transaction = {"type": "Withdraw", "amount": amount}
            Bank.user_accounts[self.Ac_number]["transaction_history"].append(
                transaction)
            print(f"\n{amount} Withdrawn Successfull.\n")
        elif Bank.balance <= self.balance:
            print("\nThe bank is BANKRUPT !!!!!\n")
        else:
            print("\n Invalid Amount !!! \n")

    def show_trasaction(self):
        if len(Bank.user_accounts[self.Ac_number]["transaction_history"]) == 0:
            print("You have done no transaction yet !!! ")
        for transaction in Bank.user_accounts[self.Ac_number]["transaction_history"]:
            print(f"Transaction Type: {transaction['type']}, Amount: {
                  transaction['amount']}\n")
        print("\n")

    def take_loan(self, amount):
        if amount <= Bank.user_accounts[self.Ac_number]["balance"]*2 and amount > 0 and amount <= Bank.balance:
            self.loan += amount
            Bank.loan_amount += amount
            Bank.balance -= amount
            transaction = {"type": "Loan", "amount": amount}
            Bank.user_accounts[self.Ac_number]["transaction_history"].append(
                transaction)
        else:
            print("\n Invalid Amount !!! \n")

    def transfer_balance(self, Ac_number, amount):
        if amount <= Bank.user_accounts[self.Ac_number]["balance"] and amount > 0 and amount <= Bank.balance:
            self.balance -= amount
            Bank.user_accounts[self.Ac_number]["balance"] -= amount
            Bank.user_accounts[Ac_number]["balance"] += amount
            transaction = {"type": "Transfer", "amount": amount}
            Bank.user_accounts[self.Ac_number]["transaction_history"].append(
                transaction)
            transaction = transaction = {"type": "Received", "amount": amount}
            Bank.user_accounts[Ac_number]["transaction_history"].append(
                transaction)
            print(f"\n{amount} transferred to Ac No {Ac_number} successfully \n")
        else:
            print("\n Insufficient Balance !!! \n")


class Admin(user_details, Bank):
    def __init__(self, name, id, password) -> None:
        self.name = name
        self.password = password
        self.id = id
        if id not in Bank.admin_accounts:
            Bank.admin_accounts[id] = {"name": name, "password": password}
        super().__init__(name, password)


    def check_balance(self):
        print(f"\nTotal BALANCE of the Bank is: {Bank.balance}\n")

    def check_loan(self):
        print(f"\nTotal Loan AMOUNT of the Bank is: {Bank.loan_amount}\n")

    def loan_system(self, op):
        if op == 1:
            Bank.loan = True
            print("\nLoan System On successfully\n")
        elif op == 2:
            Bank.loan = False
            print("\nLoan System Close successfully\n")
        else:
            print("\nInvalid Selection\n")


while (True):
    print("--------------Welcome to Bank Management System -----------------")

    print("Who are YOU ?\n 1. User \n 2. Admin\n")
    print("Type 3 If you want to close the programme\n")
    choice = int(input("Your Choice : "))
    if choice == 1:
        print("What do you want to do : \n 1. Login \n 2. Create new account \n")
        # print("Press 1. for login and 2. for creating new account\n")
        choose = int(input("Your choice : "))

        if choose == 1 or choose == 2:
            if choose == 2:
                name = input("Your name : ")
            account_no = int(input("Account No : "))
            password = (input("Your password : "))
            ok = True
            if choose == 1 and account_no not in Bank.user_accounts:
                print(
                    "There is no account for this Account Number !!! Try again ")
                ok = False

            elif choose == 2 and account_no in Bank.user_accounts:
                while True:
                    print(
                        f"\nThis Account No is already used, Please give another one \n")
                    account_no = int(input("Account No : "))
                    if account_no not in Bank.user_accounts:
                        break

            elif choose == 1 and Bank.user_accounts[account_no]["password"] != password:
                while True:
                    print(
                        f"\n Your Password is not correct !!! .Please give the right one . \n")
                    password = (input("Your Password: "))
                    if Bank.user_accounts[account_no]["password"] == password:
                        break

            if ok == True:
                if choose == 1:
                    print("Login Successfull \n")
                else:
                    print("Account created Successfylly \n")
                user = User(name, account_no, password)
                print(f"---------------- Welcome {name} ----------------")
                while True:
                    print("1.Deposit")
                    print("2.Withdraw")
                    print("3.Transfer")
                    print("4.Transaction History")
                    print("5.Check Balance")
                    if Bank.loan == True:
                        print("6.Take Loan")
                        print("7.Logout")
                    else:
                        print("6.Logout")
                    opt = int(input("\nYour choice : "))
                    print("\n")
                    if opt == 1:
                        amount = int(input("Enter Amount : "))
                        user.deposit(amount)
                    elif opt == 2:
                        amount = int(input("Enter Amount : "))
                        user.withdraw(amount)
                    elif opt == 3:
                        accNo = int(input("Enter Account No : "))
                        if accNo not in Bank.user_accounts or (accNo == account_no) :
                            while True:
                                print(
                                    "\nThe Account Number is not correct.Please provide the correct Account No .\n")
                                accNo = int(input("Enter Account No : "))
                                if accNo in Bank.user_accounts and accNo != account_no:
                                    break
                        
                        amount = int(input("Enter Amount : "))
                        user.transfer_balance(accNo, amount)
                    elif opt == 4:
                        user.show_trasaction()
                    elif opt == 5:
                        user.check_balance()
                    elif opt == 6 and Bank.loan == True:
                        amount = int(input("Enter Amount : "))
                        user.take_loan(amount)
                    elif opt == 7 or (opt == 6 and Bank.loan == False):
                        break
                    else:
                        print("Invalid Selection\n")
        else:
            print("Invalid Selection\n")

    elif choice == 2:
        print("What do you want to do : \n 1. Login \n 2. Create new account \n")
        # print("Press 1. for login and 2. for creating new account\n")
        choose = int(input("Your choice : "))

        if choose == 1 or 2:
            if choose == 2:
                name = input("Your name : ")
            id = int(input("Your Id :"))
            password = (input("Your password : "))
            ok = True
            if choose == 1 and id not in Bank.admin_accounts:
                print(
                    "\nThere is no account for this ID !!! Please Try again .\n")
                ok = False

            elif choose == 1 and Bank.admin_accounts[id]["password"] != password:
                while True:
                    print(
                        f"\n Your Password is not correct !!! .Please give the right one . \n")
                    password = (input("Your Password: "))
                    if Bank.admin_accounts[account_no]["password"] == password:
                        break

            elif choose == 2 and id in Bank.admin_accounts:
                while True:
                    print(f"This ID is already used, Please give another one \n")
                    id = int(input("Id No : "))
                    if id not in Bank.admin_accounts:
                        print("\nAccount Created Successfully\n")
                        break
            if ok == True:
                if choose == 1:
                    print("\nLogin Successfull \n")
                else:
                    print("\nAccount created Successfylly \n")

                print(f"\n---------------- Welcome {name} ----------------\n")
                admin = Admin(name, id, password)

                while True:
                    print("1.Check Balance")
                    print("2.Check Loan Amount")
                    print("3.Turn on/off loan system")
                    print("4.Logout")
                    opt = int(input("Your choice : "))
                    if opt == 1:
                        admin.check_balance()
                    elif opt == 2:
                        admin.check_loan()
                    elif opt == 3:
                        print("1.Turn Loan option ON")
                        print("2.Turn Loan option CLOSE")
                        op = int(input("Your Choice :"))
                        admin.loan_system(op)
                    elif opt == 4:
                        break
        else:
           print("\nInvalid Selection\n")
    elif choice ==3 :
        print("\n----------------- The Programme Closed Successfully -----------------\n")
        break
    else:
        print("\nInvalid Selection\n")
