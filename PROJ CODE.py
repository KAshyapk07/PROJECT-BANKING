import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from tkinter import Toplevel, StringVar, Label, Entry, Button, N, W, S, E

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.credit_card = None

class CreditCard:
    def __init__(self, card_number, card_holder, expiration_date, pin):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.pin = pin
        self.balance = 1000  # Initial balance
        self.spending_limit = float('inf')
        self.transactions = []

    def make_transaction(self, amount, merchant):
        if amount > self.spending_limit:
            messagebox.showinfo("Error", "Transaction exceeds spending limit!")
        else:
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction = {"date": date, "amount": amount, "merchant": merchant}
            self.transactions.append(transaction)
            self.balance -= amount
            messagebox.showinfo("Success", f"Transaction successful!\nAmount: {amount}\nMerchant: {merchant}")

    def change_pin(self, new_pin):
        self.pin = new_pin
        messagebox.showinfo("Success", "PIN changed successfully!")

    def set_spending_limit(self, limit):
        self.spending_limit = limit
        messagebox.showinfo("Success", "Spending limit set successfully!")

    def close_account(self):
        messagebox.showinfo("Account Closed", "Account closed successfully!")


class CreditCardManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Credit Card Management System")

        self.current_user = None

        self.login_frame = ttk.Frame(self.master)
        self.login_frame.pack(pady=20)

        self.register_label = ttk.Label(self.login_frame, text="Login or Register", font=("Helvetica", 16))
        self.register_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.username_label = ttk.Label(self.login_frame, text="Username:")
        self.username_label.grid(row=1, column=0, pady=5, padx=10, sticky="E")

        self.password_label = ttk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=2, column=0, pady=5, padx=10, sticky="E")

        self.username_entry = ttk.Entry(self.login_frame)
        self.username_entry.grid(row=1, column=1, pady=5, padx=10, sticky="W")

        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=2, column=1, pady=5, padx=10, sticky="W")

        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.register_button = ttk.Button(self.login_frame, text="Register", command=self.register)
        self.register_button.grid(row=4, column=0, columnspan=2, pady=10)
    def register(self):
        global registered_users = []
        registered_users = []
        
        global temp_name
        global temp_age
        global temp_email
        global temp_pass

        temp_name = StringVar()
        temp_age = StringVar()
        temp_email = StringVar()
        temp_pass = StringVar()

        # registering screen
        register_screen = Toplevel(self.master)
        register_screen.title('REGISTER TO BANK MANAGER')
        register_screen.geometry('500x500')

        Label(register_screen, text="FILL THE DETAILS TO REGISTER", font=('calibri', 12)).grid(row=0, sticky=N, pady=10)
        Label(register_screen, text="Name", font=('calibri', 12)).grid(row=1, sticky=W)
        Label(register_screen, text="Age", font=('calibri', 12)).grid(row=2, sticky=W)
        Label(register_screen, text="Email", font=('calibri', 12)).grid(row=3, sticky=W)
        Label(register_screen, text="Password", font=('calibri', 12)).grid(row=4, sticky=W)

        notif = Label(register_screen, font=('calibri', 12))
        notif.grid(row=10, sticky=N, pady=10)

        Entry(register_screen, textvariable=temp_name).grid(row=1, sticky=E, column=2)
        Entry(register_screen, textvariable=temp_age).grid(row=2, sticky=E, column=2)
        Entry(register_screen, textvariable=temp_email).grid(row=3, sticky=E, column=2)
        Entry(register_screen, textvariable=temp_pass, show="*").grid(row=4, sticky=E, column=2)

        def finish_reg():
            name = temp_name.get()
            age = temp_age.get()
            email = temp_email.get()
            password = temp_pass.get()

            if name == "" or age == "" or email == "" or password == "":
                notif.config(fg='red', text="ALL FIELDS ARE REQUIRED!!")
                return

            user_exists = self.check_user_exists(name)

            if user_exists:
                notif.config(fg='red', text="USER ALREADY EXIST!!")
            else:
                # Store user information
                self.store_user_info(name, password)

                # Create a user instance and add it to the list
                registered_users.append(User(name, password))
                notif.config(fg='green', text="CONGRATULATIONS!! ACCOUNT SUCCESFULLY CREATED")

        Button(register_screen, text='REGISTER', font=('calibri', 12), width=20, command=finish_reg).grid(row=6,
                                                                                                          sticky=S)

    def check_user_exists(self, username):
        # Check if the user is already registered by checking the stored data
        return any(user.username == username for user in registered_users)

    def store_user_info(self, username, password):
        # Store user information in a file (you may use a database for a more robust solution)
        with open("registered_users.txt", "a") as file:
            file.write(f"{username},{password}\n")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = self.authenticate_user(username, password)

        if user:
            # If the user is registered, show the main credit card management app
            self.login_frame.destroy()
            self.current_user = user
            self.create_credit_card_management_app()
        else:
            messagebox.showinfo("Error", "Invalid username or password. Please register if you are a new user.")

    def authenticate_user(self, username, password):
        for user in registered_users:
            if user.username == username and user.password == password:
                return user
        return None


    def create_credit_card_management_app(self):
        # Create a credit card instance for the logged-in user
        self.current_user.credit_card = CreditCard("1234567812345678", "John Doe", "12/25", "1234")

        # Create GUI components
        self.label = ttk.Label(self.master, text="Credit Card Management System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.balance_label = ttk.Label(self.master,
                                       text=f"Balance: ${self.current_user.credit_card.balance}")
        self.balance_label.pack()

        self.tabs = ttk.Notebook(self.master)
        self.tabs.pack(pady=10)

        self.transaction_tab = ttk.Frame(self.tabs)
        self.settings_tab = ttk.Frame(self.tabs)

        self.tabs.add(self.transaction_tab, text="Transactions")
        self.tabs.add(self.settings_tab, text="Settings")

        self.create_transaction_tab()
        self.create_settings_tab()

    def create_transaction_tab(self):
        transaction_label = ttk.Label(self.transaction_tab, text="Make Transaction", font=("Helvetica", 12))
        transaction_label.grid(row=0, column=0, columnspan=2, pady=10)

        amount_label = ttk.Label(self.transaction_tab, text="Amount:")
        amount_label.grid(row=1, column=0, pady=5, padx=10, sticky="E")

        self.amount_entry = ttk.Entry(self.transaction_tab)
        self.amount_entry.grid(row=1, column=1, pady=5, padx=10, sticky="W")

        merchant_label = ttk.Label(self.transaction_tab, text="Merchant:")
        merchant_label.grid(row=2, column=0, pady=5, padx=10, sticky="E")

        self.merchant_entry = ttk.Entry(self.transaction_tab)
        self.merchant_entry.grid(row=2, column=1, pady=5, padx=10, sticky="W")

        transaction_button = ttk.Button(self.transaction_tab, text="Make Transaction", command=self.make_transaction)
        transaction_button.grid(row=3, column=0, columnspan=2, pady=10)

        history_label = ttk.Label(self.transaction_tab, text="Transaction History", font=("Helvetica", 12))
        history_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.transaction_listbox = tk.Listbox(self.transaction_tab, width=40, height=10)
        self.transaction_listbox.grid(row=5, column=0, columnspan=2, pady=5)

        for transaction in self.current_user.credit_card.transactions:
            self.transaction_listbox.insert(tk.END,
                                            f"{transaction['date']} - ${transaction['amount']} - {transaction['merchant']}")

    def create_settings_tab(self):
        pin_label = ttk.Label(self.settings_tab, text="Change PIN", font=("Helvetica", 12))
        pin_label.grid(row=0, column=0, columnspan=2, pady=10)

        new_pin_label = ttk.Label(self.settings_tab, text="New PIN:")
        new_pin_label.grid(row=1, column=0, pady=5, padx=10, sticky="E")

        self.new_pin_entry = ttk.Entry(self.settings_tab, show="*")
        self.new_pin_entry.grid(row=1, column=1, pady=5, padx=10, sticky="W")

        pin_button = ttk.Button(self.settings_tab, text="Change PIN", command=self.change_pin)
        pin_button.grid(row=2, column=0, columnspan=2, pady=10)

        limit_label = ttk.Label(self.settings_tab, text="Set Spending Limit", font=("Helvetica", 12))
        limit_label.grid(row=3, column=0, columnspan=2, pady=10)

        limit_amount_label = ttk.Label(self.settings_tab, text="Limit Amount:")
        limit_amount_label.grid(row=4, column=0, pady=5, padx=10, sticky="E")

        self.limit_amount_entry = ttk.Entry(self.settings_tab)
        self.limit_amount_entry.grid(row=4, column=1, pady=5, padx=10, sticky="W")

        limit_button = ttk.Button(self.settings_tab, text="Set Limit", command=self.set_spending_limit)
        limit_button.grid(row=5, column=0, columnspan=2, pady=10)

        close_label = ttk.Label(self.settings_tab, text="Close Account", font=("Helvetica", 12))
        close_label.grid(row=6, column=0, columnspan=2, pady=10)

        close_button = ttk.Button(self.settings_tab, text="Close Account", command=self.close_account)
        close_button.grid(row=7, column=0, columnspan=2, pady=10)

        due_label = ttk.Label(self.settings_tab, text="Payment Due", font=("Helvetica", 12))
        due_label.grid(row=8, column=0, columnspan=2, pady=10)

        self.due_notification_label = ttk.Label(self.settings_tab, text="")
        self.due_notification_label.grid(row=9, column=0, columnspan=2, pady=5)

        check_due_button = ttk.Button(self.settings_tab, text="Check Due", command=self.check_due)
        check_due_button.grid(row=10, column=0, columnspan=2, pady=10)

    def check_due(self):
        current_date = datetime.datetime.now()
        due_date = datetime.datetime.strptime(self.current_user.credit_card.expiration_date, "%m/%y")
        remaining_days = (due_date - current_date).days

        if self.current_user.credit_card.balance < 0:
            due_amount = abs(self.current_user.credit_card.balance)
            notification = f"Payment due in {remaining_days} days. Due Amount: ${due_amount}. Please make the payment on time!"
        else:
            notification = "No payment due at the moment."

        self.due_notification_label.config(text=notification)

    def make_transaction(self):
        try:
            amount = float(self.amount_entry.get())
            merchant = self.merchant_entry.get()
            self.current_user.credit_card.make_transaction(amount, merchant)
            self.update_balance_label()
            self.update_transaction_listbox()
        except ValueError:
            messagebox.showinfo("Error", "Invalid amount!")

    def change_pin(self):
        new_pin = self.new_pin_entry.get()
        self.current_user.credit_card.change_pin(new_pin)

    def set_spending_limit(self):
        try:
            limit = float(self.limit_amount_entry.get())
            self.current_user.credit_card.set_spending_limit(limit)
        except ValueError:
            messagebox.showinfo("Error", "Invalid limit!")

    def close_account(self):
        result = messagebox.askyesno("Close Account", "Are you sure you want to close your account?")
        if result:
            self.current_user.credit_card.close_account()
            self.master.destroy()

    def update_balance_label(self):
        self.balance_label.config(text=f"Balance: ${self.current_user.credit_card.balance}")

    def update_transaction_listbox(self):
        self.transaction_listbox.delete(0, tk.END)
        for transaction in self.current_user.credit_card.transactions:
            self.transaction_listbox.insert(tk.END,
                                            f"{transaction['date']} - ${transaction['amount']} - {transaction['merchant']}")

# List to store registered users


if __name__ == "__main__":
    root = tk.Tk()
    app = CreditCardManagementApp(root)
    root.mainloop()
