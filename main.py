import tkinter as tk
from tkinter import messagebox, ttk


# Calculate Loan Payment, Amortization Schedule and Extras
def calculate_loan():
    try:
        principal = float(principal_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100 / 12  # Monthly interest rate
        loan_term = float(loan_term_entry.get()) * 12  # Total number of payments (months)
        extra_payment = float(extra_payment_entry.get())
        
        # Monthly payment formula
        monthly_payment = (principal * interest_rate * (1 + interest_rate)**loan_term) / ((1 + interest_rate)**loan_term - 1)
        
        # Variables to track total paid and interest paid
        total_amount_paid = 0
        total_interest_paid = 0
        
        # Initialize amortization schedule
        amortization_schedule = []
        
        balance = principal
        for month in range(1, int(loan_term) + 1):
            interest = balance * interest_rate
            principal_payment = monthly_payment - interest + extra_payment
            balance -= principal_payment
            
            if balance < 0:
                balance = 0

            total_amount_paid += monthly_payment
            total_interest_paid += interest
            
            # Add entry to amortization schedule
            amortization_schedule.append((month, monthly_payment, principal_payment, interest, balance))
            
            if balance == 0:
                break
        
        # Display Results with INR format
        monthly_payment_label.config(text=f"Monthly Payment: ₹{monthly_payment:,.2f}")
        total_amount_paid_label.config(text=f"Total Amount Paid: ₹{total_amount_paid:,.2f}")
        total_interest_paid_label.config(text=f"Total Interest Paid: ₹{total_interest_paid:,.2f}")
        
        # Populate Amortization Schedule Table
        for row in tree.get_children():
            tree.delete(row)

        for month, payment, principal_payment, interest, balance in amortization_schedule:
            tree.insert("", "end", values=(month, f"₹{payment:,.2f}", f"₹{principal_payment:,.2f}", f"₹{interest:,.2f}", f"₹{balance:,.2f}"))
            
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Mutual Fund Calculator Function
def calculate_mutual_fund():
    try:
        sip = float(sip_entry.get())
        annual_rate = float(mutual_rate_entry.get())
        years = int(mutual_years_entry.get())

        # Monthly rate and total months
        monthly_rate = annual_rate / (12 * 100)
        months = years * 12

        # Future Value formula for SIP
        future_value = sip * ((1 + monthly_rate) ** months - 1) / monthly_rate * (1 + monthly_rate)

        # Display results
        sip_result_label.config(text=f"Future Value: ₹{future_value:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Switch to Loan Calculator Tab
def show_loan_calculator():
    tree.grid()
    notebook.select(loan_frame)  # Switch to Loan Calculator tab

# Switch to Mutual Fund Calculator Tab
def show_mutual_calculator():
    tree.grid_remove()
    notebook.select(mutual_frame)  # Switch to Mutual Fund Calculator tab


# Create the main window
root = tk.Tk()
root.title("Loan (INR) - RBI Standard And Mutual Funds (MF) Calculator")

# Notebook for tabs
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Loan Calculator Frame
loan_frame = ttk.Frame(notebook)
notebook.add(loan_frame, text="Loan Calculator")


# Mutual Fund Calculator Frame
mutual_frame = ttk.Frame(notebook)
notebook.add(mutual_frame, text="Mutual Fund Calculator")


# Create input fields and labels
# For the Label widget
principal_label = tk.Label(loan_frame, text="Principal Amount (₹):")
principal_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
principal_entry = tk.Entry(loan_frame)
principal_entry.grid(row=0, column=1, padx=10, pady=5)


interest_rate_label = tk.Label(loan_frame, text="Annual Interest Rate (%):")
interest_rate_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)
interest_rate_entry = tk.Entry(loan_frame)
interest_rate_entry.grid(row=1, column=1, padx=10, pady=5)

loan_term_label = tk.Label(loan_frame, text="Loan Term (years):")
loan_term_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)
loan_term_entry = tk.Entry(loan_frame)
loan_term_entry.grid(row=2, column=1, padx=10, pady=5)

extra_payment_label = tk.Label(loan_frame, text="Extra Monthly Payment (₹)(input '0' in none):")
extra_payment_label.grid(row=3, column=0, sticky='w', padx=10, pady=5)
extra_payment_entry = tk.Entry(loan_frame)
extra_payment_entry.grid(row=3, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(loan_frame, text="Calculate", command=calculate_loan)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)


# Input fields for Mutual Fund Calculator
sip_label = ttk.Label(mutual_frame, text="Monthly SIP Amount (₹):")
sip_label.grid(row=0, column=0, sticky='w', padx=10, pady=5)
sip_entry = ttk.Entry(mutual_frame)
sip_entry.grid(row=0, column=1, padx=10, pady=5)

mutual_rate_label = ttk.Label(mutual_frame, text="Annual Interest Rate (%):")
mutual_rate_label.grid(row=1, column=0, sticky='w', padx=10, pady=5)
mutual_rate_entry = ttk.Entry(mutual_frame)
mutual_rate_entry.grid(row=1, column=1, padx=10, pady=5)

mutual_years_label = ttk.Label(mutual_frame, text="Investment Period (Years):")
mutual_years_label.grid(row=2, column=0, sticky='w', padx=10, pady=5)
mutual_years_entry = ttk.Entry(mutual_frame)
mutual_years_entry.grid(row=2, column=1, padx=10, pady=5)

#Calculate Button
calculate_mutual_button = ttk.Button(mutual_frame, text="Calculate", command=calculate_mutual_fund)
calculate_mutual_button.grid(row=3, column=1, padx=10, pady=5)

# Output labels
monthly_payment_label = tk.Label(loan_frame, text="")
monthly_payment_label.grid(row=5, column=0, columnspan=2)

total_amount_paid_label = tk.Label(loan_frame, text="")
total_amount_paid_label.grid(row=6, column=0, columnspan=2)

total_interest_paid_label = tk.Label(loan_frame, text="")
total_interest_paid_label.grid(row=7, column=0, columnspan=2)

sip_result_label = ttk.Label(mutual_frame, text="Future Value:")
sip_result_label.grid(row=4, column=0, columnspan=2)


# Add Amortization Schedule table
tree = ttk.Treeview(loan_frame, columns=("Month", "Payment", "Principal", "Interest", "Balance"), show="headings")
tree.heading("Month", text="Month")
tree.heading("Payment", text="Payment (₹)")
tree.heading("Principal", text="Principal (₹)")
tree.heading("Interest", text="Interest (₹)")
tree.heading("Balance", text="Balance (₹)")
tree.grid(row=8, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
