import finance_tools

# EMI
def calculate_emi(principal, annual_rate, tenure_months):
    if principal <= 0 or annual_rate <= 0 or tenure_months <= 0:
        raise ValueError("Principal, rate, and tenure must be positive.")
    return finance_tools.emi_calculator(principal, annual_rate, tenure_months)

# SIP
def calculate_sip(monthly_investment, annual_rate, tenure_months):
    if monthly_investment <= 0 or annual_rate <= 0 or tenure_months <= 0:
        raise ValueError("Investment, rate, and tenure must be positive.")
    return finance_tools.sip_calculator(monthly_investment, annual_rate, tenure_months)

# FD
def calculate_fd(principal, annual_rate, tenure_years):
    if principal <= 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("All inputs must be positive.")
    return finance_tools.fd_calculator(principal, annual_rate, tenure_years)

# RD
def calculate_rd(monthly_deposit, annual_rate, tenure_years):
    if monthly_deposit <= 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("All inputs must be positive.")
    return finance_tools.rd_calculator(monthly_deposit, annual_rate, tenure_years)

# Retirement
def estimate_retirement_savings(current_savings, monthly_addition, annual_rate, years):
    if current_savings < 0 or monthly_addition < 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("Invalid inputs.")
    return finance_tools.retirement_savings_estimator(current_savings, monthly_addition, annual_rate, years)

# Home Loan Eligibility
def estimate_home_loan_eligibility(income, expenses, interest_rate, tenure_years):
    if income <= 0 or expenses < 0 or expenses >= income:
        raise ValueError("Income must be greater than expenses and positive.")
    return finance_tools.home_loan_eligibility_estimator(income, expenses, interest_rate, tenure_years)

# Credit Card Interest
def calculate_credit_card_balance(balance, annual_rate, min_payment_percent, months):
    if balance <= 0 or annual_rate <= 0 or months <= 0 or min_payment_percent <= 0:
        raise ValueError("Invalid inputs.")
    return finance_tools.credit_card_interest_calculator(balance, annual_rate, min_payment_percent, months)

# Taxable Income
def calculate_taxable_income(income, deductions):
    if income <= 0 or deductions < 0:
        raise ValueError("Invalid income or deductions.")
    return finance_tools.taxable_income_calculator(income, deductions)

# Budget
def create_budget_plan(income, expenses):
    if income <= 0 or expenses < 0:
        raise ValueError("Income must be positive, expenses non-negative.")
    return finance_tools.simple_budget_planner(income, expenses)

# Net Worth
def calculate_net_worth(assets, liabilities):
    if assets < 0 or liabilities < 0:
        raise ValueError("Assets and liabilities must be non-negative.")
    return finance_tools.net_worth_calculator(assets, liabilities)
