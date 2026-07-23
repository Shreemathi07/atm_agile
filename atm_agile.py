# 1. Store the user's initial balance
user_balance = 5000.0  # Example starting balance

print(f"Current Available Balance: ${user_balance:.2f}\n")

try:
    # 2. Take withdrawal amount as input
    withdrawal_amount = int(input("Enter the amount you want to withdraw: "))

    # 3. Check if the amount is a multiple of 100
    if withdrawal_amount % 100 != 0:
        print("Transaction Declined: Amount must be a multiple of 100.")
        
    # 4. Check if the balance is sufficient
    elif withdrawal_amount > user_balance:
        print("Transaction Declined: Insufficient balance available.")
        
    # 5. Deduct amount and display updated balance
    else:
        user_balance -= withdrawal_amount
        print("Transaction Successful! Please collect your cash.")
        print(f"Updated Balance: ${user_balance:.2f}")

except ValueError:
    print("Invalid Input: Please enter a valid whole number.")
