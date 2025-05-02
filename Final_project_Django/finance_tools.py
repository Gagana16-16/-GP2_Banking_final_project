import math

# 1. EMI Calculator
def emi_calculator(principal, annual_interest_rate, tenure_months):
    monthly_rate = annual_interest_rate / (12 * 100)
    emi = (principal * monthly_rate * math.pow(1 + monthly_rate, tenure_months)) / \
          (math.pow(1 + monthly_rate, tenure_months) - 1)
    return round(emi, 2)

# 2. SIP Calculator
def sip_calculator(monthly_investment, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)
    maturity = monthly_investment * ((math.pow(1 + monthly_rate, tenure_months) - 1) / monthly_rate) * (1 + monthly_rate)
    return round(maturity, 2)

# 3. FD Calculator
def fd_calculator(principal, annual_rate, tenure_years):
    maturity = principal * math.pow(1 + annual_rate / 100, tenure_years)
    return round(maturity, 2)

# 4. RD Calculator
def rd_calculator(monthly_deposit, annual_rate, tenure_years):
    monthly_rate = annual_rate / (12 * 100)
    months = tenure_years * 12
    maturity = monthly_deposit * ((math.pow(1 + monthly_rate, months) - 1) / monthly_rate) * (1 + monthly_rate)
    return round(maturity, 2)

# 5. Retirement Savings Estimator
def retirement_savings_estimator(current_savings, monthly_addition, annual_rate, years):
    future_value = current_savings * math.pow(1 + annual_rate / 100, years)
    future_value += sip_calculator(monthly_addition, annual_rate, years * 12)
    return round(future_value, 2)

# 6. Home Loan Eligibility Estimator
def home_loan_eligibility_estimator(income, expenses, interest_rate, tenure_years):
    savings = income - expenses
    if savings <= 0:
        return 0
    emi_per_lakh = emi_calculator(100000, interest_rate, tenure_years * 12)
    return round((savings / emi_per_lakh) * 100000, 2)

# 7. Credit Card Interest Calculator
def credit_card_interest_calculator(balance, annual_rate, min_payment_percent, months):
    total = balance
    for _ in range(months):
        interest = total * (annual_rate / (12 * 100))
        payment = total * (min_payment_percent / 100)
        total = total + interest - payment
    return round(total, 2)

# 8. Taxable Income Calculator
def taxable_income_calculator(gross_income, deductions):
    return max(0, round(gross_income - deductions, 2))

# 9. Simple Budget Planner
def simple_budget_planner(income, expenses):
    savings = income - expenses
    if savings > 0:
        return {"status": "Surplus", "savings": savings}
    elif savings < 0:
        return {"status": "Deficit", "savings": savings}
    return {"status": "Break-even", "savings": 0}

# 10. Net Worth Calculator
def net_worth_calculator(assets, liabilities):
    return round(assets - liabilities, 2)
