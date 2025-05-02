import finance_tools
import storage

def main():
    while True:
        print("\nFinancial Tools Menu:")
        print("1. EMI Calculator")
        print("2. SIP Calculator")
        print("3. FD Calculator")
        print("4. RD Calculator")
        print("5. Retirement Savings Estimator")
        print("6. Home Loan Eligibility Estimator")
        print("7. Credit Card Interest Calculator")
        print("8. Taxable Income Calculator")
        print("9. Simple Budget Planner")
        print("10. Net Worth Calculator")
        print("11. All Financial Data")
        print("0. Exit")

        choice = input("Enter your choice (0-11): ")

        if choice == "1":
            p = float(input("Enter principal: "))
            r = float(input("Annual interest rate (%): "))
            t = int(input("Tenure (months): "))
            result = finance_tools.emi_calculator(p, r, t)
            print(f"EMI: {result}")
            storage.save_data("EMI Calculation", {"Inputs": {"Principal": p, "Rate": r, "Months": t}, "Result": result})

        elif choice == "2":
            m = float(input("Monthly investment: "))
            r = float(input("Annual rate (%): "))
            t = int(input("Tenure (months): "))
            result = finance_tools.sip_calculator(m, r, t)
            print(f"Maturity Amount: {result}")
            storage.save_data("SIP Calculation", {"Inputs": {"Monthly": m, "Rate": r, "Months": t}, "Result": result})

        elif choice == "3":
            p = float(input("FD Amount: "))
            r = float(input("Annual Rate (%): "))
            t = float(input("Tenure (years): "))
            result = finance_tools.fd_calculator(p, r, t)
            print(f"Maturity: {result}")
            storage.save_data("FD Calculation", {"Inputs": {"Amount": p, "Rate": r, "Years": t}, "Result": result})

        elif choice == "4":
            d = float(input("Monthly Deposit: "))
            r = float(input("Annual Rate (%): "))
            t = float(input("Tenure (years): "))
            result = finance_tools.rd_calculator(d, r, t)
            print(f"Maturity: {result}")
            storage.save_data("RD Calculation", {"Inputs": {"Deposit": d, "Rate": r, "Years": t}, "Result": result})

        elif choice == "5":
            cs = float(input("Current Savings: "))
            ma = float(input("Monthly Addition: "))
            r = float(input("Annual Rate (%): "))
            y = int(input("Years: "))
            result = finance_tools.retirement_savings_estimator(cs, ma, r, y)
            print(f"Future Corpus: {result}")
            storage.save_data("Retirement Estimate", {"Inputs": {"Savings": cs, "Monthly": ma, "Rate": r, "Years": y}, "Result": result})

        elif choice == "6":
            i = float(input("Monthly Income: "))
            e = float(input("Monthly Expenses: "))
            r = float(input("Rate (%): "))
            t = int(input("Tenure (years): "))
            result = finance_tools.home_loan_eligibility_estimator(i, e, r, t)
            print(f"Loan Eligibility: {result}")
            storage.save_data("Loan Eligibility", {"Inputs": {"Income": i, "Expenses": e, "Rate": r, "Years": t}, "Result": result})

        elif choice == "7":
            b = float(input("Balance: "))
            r = float(input("Rate (%): "))
            mp = float(input("Minimum Payment (%): "))
            m = int(input("Months: "))
            result = finance_tools.credit_card_interest_calculator(b, r, mp, m)
            print(f"Final Balance: {result}")
            storage.save_data("Credit Card Interest", {"Inputs": {"Balance": b, "Rate": r, "MinPay %": mp, "Months": m}, "Result": result})

        elif choice == "8":
            gi = float(input("Gross Income: "))
            d = float(input("Deductions: "))
            result = finance_tools.taxable_income_calculator(gi, d)
            print(f"Taxable Income: {result}")
            storage.save_data("Taxable Income", {"Inputs": {"Gross": gi, "Deductions": d}, "Result": result})

        elif choice == "9":
            i = float(input("Income: "))
            e = float(input("Expenses: "))
            result = finance_tools.simple_budget_planner(i, e)
            print(f"Status: {result['status']} | Savings: {result['savings']}")
            storage.save_data("Budget Planner", {"Inputs": {"Income": i, "Expenses": e}, "Result": result})

        elif choice == "10":
            a = float(input("Assets: "))
            l = float(input("Liabilities: "))
            result = finance_tools.net_worth_calculator(a, l)
            print(f"Net Worth: {result}")
            storage.save_data("Net Worth",)
