# Function to deposit money into an account
def deposit(account: dict, amount: float) -> None:

    for key in account.keys():
        account[key] += amount

    return account[key]

# accounts = {"John": {"balance": 1000}, "Jane": {"balance": 500}}
# print(deposit(accounts["John"], 200))

# Function to withdraw money from an account
def withdraw(account: dict, amount: float) -> None:

    for key, value in account.items():
        if amount > value:
            return "Insufficient funds"
        account[key] -= amount
    return value
# accounts = {"John": {"balance": 1000}, "Jane": {"balance": 500}}
# print(withdraw(accounts["John"], 500))
# print(withdraw(accounts["John"], 1000))


# Function to transfer money between two accounts
def transfer(from_account: dict, to_account: dict, amount: float) -> None:
    for key1, value1 in from_account.items():
        for key2, value2 in to_account.items():
            from_account[key1] -= amount
            to_account[key2] += amount
    return value1

# accounts = {"John": {"balance": 1000}, "Jane": {"balance": 500}}
# print(transfer(accounts['John'], accounts['Jane'], 300))


# Function to add a new account to the system
def add_account(accounts: dict, owner: str, initial_balance: float) -> None:
    pass

# Function to find an account by owner's name
def find_account(accounts: dict, owner: str) -> dict:
    pass

# Function to display all accounts in the system
def display_all_accounts(accounts: dict) -> str:
    return '\n'.join([f"{owner}: {account['balance']}" for owner, account in accounts.items()])
