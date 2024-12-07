print("Welcome to the ATM!\n")

balance = 100

while True:
    print(f"""Current balance: ${balance}
    1. Check Balance
    2. Deposit Money
    3. Withdraw Money
    4. Exit""")

    option = input("Choose an option: ")

    match option:
        case '1':
            print(f"Your balance is currently: {balance}\n")
        case '2':
            deposit = float(input("Enter amount to deposit: "))
            balance += deposit
            print(f"Deposit successful! Your new balance is ${float(balance)}\n")
        case '3':
            withdrawal = float(input("Enter amount to withdraw: "))
            balance -= withdrawal
            print(f"Withdrawal successful! Your new balance is ${float(balance)}\n")
        case '4':
            exit(0)
        case _:
            print("Please enter one of the above options")
