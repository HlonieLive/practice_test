# Function to deposit money into an account
def deposit(account: dict, amount: float) -> None:
    # names = []
    # holders = []

    for key, value in account.items():
        account[key] += amount
        # names.append(key)
        # holders.append(value)

    return account[key]

accounts = {
    'John': {'balance': 1000},
    'Jane': {'balance': 500}
    }

print(deposit(accounts["John"], 200))

# Function to withdraw money from an account
def withdraw(account: dict, amount: float) -> None:
    pass

# Function to transfer money between two accounts
def transfer(from_account: dict, to_account: dict, amount: float) -> None:
    pass

# Function to add a new account to the system
def add_account(accounts: dict, owner: str, initial_balance: float) -> None:
    pass

# Function to find an account by owner's name
def find_account(accounts: dict, owner: str) -> dict:
    pass

# Function to display all accounts in the system
def display_all_accounts(accounts: dict) -> str:
    return '\n'.join([f"{owner}: {account['balance']}" for owner, account in accounts.items()])
