import mysql.connector as m
from datetime import datetime

# MySQL connection
conn = m.connect(
    host='localhost',
    user='root',     
    password='Ore.wa@Amol.Desu%1221', 
    database='bank_db'
)
cursor = conn.cursor()

def create_account():
    full_name = input("Enter your full name: ")
    aadhar_no = input("Enter your Aadhar No: ")
    pan_no = input("Enter your PAN No: ")
    DOB = input("Enter your DOB (YYYY-MM-DD): ")
    address = input("Enter your address: ")
    mobile_no = input("Enter your mobile no: ")
    email_id = input("Enter your email ID: ")
    balance = float(input("Add deposit (at least 500 Rs): "))

    if balance < 500:
        print("Minimum deposit should be 500 Rs.")
        return

    query = "INSERT INTO bank_accounts (full_name, aadhar_no, pan_no, DOB , address, mobile_no, email_id, balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (full_name, aadhar_no, pan_no, DOB, address, mobile_no, email_id, balance)
    
    cursor.execute(query, values)
    conn.commit()
    
    print(f"Account created successfully. Your account number is {cursor.lastrowid}")

def check_balance():
    account_no = input("Enter your account no: ")
    mobile_no = input("Enter your mobile no: ")
    
    query = "select balance from bank_accounts where account_no = %s AND mobile_no = %s"
    values = (account_no, mobile_no)
    
    cursor.execute(query, values)
    result = cursor.fetchone()
    
    if result:
        print(f"Your balance is: {result[0]}")
    else:
        print("Account not found or incorrect mobile number.")

def withdraw_money():
    account_no = input("Enter your account no: ")
    mobile_no = input("Enter your mobile no: ")
    amount = int(input("Enter amount to withdraw: "))
    
    query = "select balance from bank_accounts where account_no = %s AND mobile_no = %s"
    values = (account_no, mobile_no)
    
    cursor.execute(query, values)
    result = cursor.fetchone()
    
    if result:
        balance = result[0]
        if balance >= amount:
            new_balance = balance - amount
            update_query = "update bank_accounts set balance = %s where account_no = %s"
            cursor.execute(update_query, (new_balance, account_no))
            conn.commit()
            print(f"Withdrawal successful. Your new balance is: {new_balance}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found or incorrect mobile number.")

def deposit_money():
    account_no = input("Enter your account no: ")
    mobile_no = input("Enter your mobile no: ")
    amount = int(input("Enter amount to deposit: "))
    
    query = "select balance from bank_accounts where account_no = %s AND mobile_no = %s"
    values = (account_no, mobile_no)
    
    cursor.execute(query, values)
    result = cursor.fetchone()
    
    if result:
        new_balance = result[0] + amount
        update_query = "update bank_accounts set balance = %s where account_no = %s"
        cursor.execute(update_query, (new_balance, account_no))
        conn.commit()
        print(f"Deposit successful. Your new balance is: {new_balance}")
    else:
        print("Account not found or incorrect mobile number.")

def main():
    while True:
        print("\nBank Account Management System")
        print("1. Create bank account")
        print("2. Check balance")
        print("3. Withdraw money")
        print("4. Deposit money")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            create_account()
        elif choice == 2:
            check_balance()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            deposit_money()
        elif choice == 5:
            print("Exit")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()


cursor.close()
conn.close()
