
# 1. Store the user's initial balance
user_balance = 5000.0  

# 2. Hardcoded withdrawal amount (Change this value to test different scenarios)
withdrawal_amount = 0  

print(f"Current Available Balance: ${user_balance:.2f}")
print(f"Attempting to withdraw: ${withdrawal_amount:.2f}\n")

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
