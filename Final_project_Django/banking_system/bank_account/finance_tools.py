def test_func():
    return "Hello from finance_tools"
#  --------------------------------------------------1 --------------------------------
def calculate_emi(principal, annual_rate, tenure_years):
    """
    Calculate the Equated Monthly Installment (EMI) for a loan.

    Parameters:
    ----------
    principal : float
        The total loan amount (must be greater than 0).
    
    annual_rate : float
        The annual interest rate in percentage (e.g., 7.5 for 7.5% per annum).
        Can be 0 if it's a zero-interest loan.
    
    tenure_years : int
        The loan tenure or duration in years (must be greater than 0).

    Returns:
    -------
    float
        The monthly EMI amount. Returns 0 if any input leads to invalid or negative EMI.
    """
    if principal <= 0 or annual_rate < 0 or tenure_years <= 0:
        raise ValueError("Principal, annual rate, and tenure must be positive and greater than zero.")
    monthly_rate = annual_rate / (12 * 100)
    tenure_months = tenure_years * 12

    if monthly_rate == 0:
        emi = principal / tenure_months
    else:
        emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / \
              ((1 + monthly_rate) ** tenure_months - 1)

    return max(emi, 0)

#  --------------------------------------------------2 --------------------------------
def calculate_sip(monthly_investment, annual_rate, years):
    """
    Calculate the future value of a Systematic Investment Plan (SIP).

    A SIP is a method of investing a fixed amount every month into mutual funds or similar instruments.
    This function computes the future value using the compound interest formula for monthly contributions.

    Parameters:
    ----------
    monthly_investment : float
        The fixed amount invested every month.

    annual_rate : float
        The expected annual return rate (in percentage), e.g., 12 for 12% annual return.

    years : int
        The total investment period in years.

    Returns:
    -------
    float
        The future value (FV) of the investment rounded to 2 decimal places.
    """
    if monthly_investment <= 0 or annual_rate < 0 or years <= 0:
        raise ValueError("Inputs must be positive and annual rate non-negative.")
    r = annual_rate / (12 * 100)
    n = years * 12
    fv = monthly_investment * (((1 + r) ** n - 1) / r) * (1 + r)
    return round(fv, 2)

# --------------------------------------------------3 --------------------------------
def calculate_fd(principal, annual_rate, years, compounding_frequency=4):
    """
    Calculate the maturity amount and interest earned for a Fixed Deposit (FD).

    This function uses compound interest to compute the future value of a fixed deposit,
    considering compounding frequency (e.g., quarterly, monthly, etc.).

    Parameters:
    ----------
    principal : float
        The initial amount deposited.

    annual_rate : float
        The annual interest rate (in percentage), e.g., 6.5 for 6.5% per annum.

    years : float
        The duration of the deposit in years.

    compounding_frequency : int, optional
        The number of times the interest is compounded per year (default is 4, i.e., quarterly).
        Common values: 1 (annually), 2 (semi-annually), 4 (quarterly), 12 (monthly).

    Returns:
    -------
    tuple
        A tuple containing:
        - maturity_amount (float): The total amount at maturity, rounded to 2 decimal places.
        - interest_earned (float): The interest earned over the period, rounded to 2 decimal places.
    """
    if principal <= 0 or annual_rate < 0 or years <= 0 or compounding_frequency <= 0:
        raise ValueError("Inputs must be positive, and interest rate must be non-negative.")
    r = annual_rate / 100
    n = compounding_frequency
    t = years
    maturity_amount = principal * (1 + r / n) ** (n * t)
    interest_earned = maturity_amount - principal
    return round(maturity_amount, 2), round(interest_earned, 2)

# --------------------------------------------------4 --------------------------------
def calculate_rd(monthly_deposit, annual_rate, years):
    """
    Calculate the maturity amount of a Recurring Deposit (RD).

    A recurring deposit involves investing a fixed amount every month for a fixed period.
    This function assumes quarterly compounding, which is standard in many banks.

    Parameters:
    ----------
    monthly_deposit : float
        The fixed amount deposited every month.

    annual_rate : float
        The annual interest rate (in percentage), e.g., 7.0 for 7% per annum.

    years : int
        The total deposit period in years.

    Returns:
    -------
    float
        The maturity value of the recurring deposit, rounded to 2 decimal places.
    """
    if monthly_deposit <= 0 or annual_rate < 0 or years <= 0:
        raise ValueError("All inputs must be positive, and interest rate must be non-negative.")

    n = years * 12
    r = annual_rate / 400
    maturity_value = monthly_deposit * (((1 + r) ** n - 1) / (1 - (1 + r) ** -1))
    return round(maturity_value, 2)

#--------------------------------------------------5--------------------------------

def estimate_retirement(current_savings, monthly_contribution, annual_return, years):
    """ Estimate the total retirement corpus based on current savings, monthly investments, and expected return.

    This function calculates the future value of a lump-sum investment (current savings)
    and the future value of regular monthly contributions (similar to SIP),
    both compounded monthly at the given annual return rate.

    Parameters:
    ----------
    current_savings : float
        The current lump-sum savings amount.

    monthly_contribution : float
        The fixed monthly contribution toward retirement.

    annual_return : float
        The expected annual return rate (in percentage), e.g., 8.0 for 8% per annum.

    years : int
        The number of years until retirement.

    Returns:
    -------
    tuple
        A tuple containing:
        - total_corpus (float): The estimated future value (retirement corpus) at the end of the investment period.
        - total_invested (float): The total principal amount invested (current savings + all monthly contributions).
        - total_interest (float): The interest earned over the investment period.
    """
    if current_savings < 0 or monthly_contribution < 0 or annual_return < 0 or years <= 0:
        raise ValueError("All inputs must be non-negative, and years must be positive.")
    r = annual_return / 12 / 100
    n = years * 12
    fv_sip = monthly_contribution * (((1 + r) ** n - 1) / r) * (1 + r)
    fv_lump = current_savings * ((1 + r) ** n)
    total_corpus = round(fv_sip + fv_lump, 2)
    total_invested = current_savings + (monthly_contribution * n)
    total_interest = round(total_corpus - total_invested, 2)

    return float(total_corpus), float(total_invested), float(total_interest)

# #  --------------------------------------------------6--------------------------------
def calculate_home_loan_eligibility(monthly_income, monthly_expenses, loan_term_years, interest_rate):
    """
    Calculate the maximum home loan eligibility based on monthly income, expenses, loan term, and interest rate.

    The function calculates the maximum loan amount the borrower is eligible for by first determining
    the eligible EMI, which is capped at 50% of the monthly income after expenses. The loan amount is
    then calculated using the EMI formula rearranged to find the principal (loan amount).

    Parameters:
    ----------
    monthly_income : float
        The borrower’s total monthly income.

    monthly_expenses : float
        The borrower’s monthly expenses.

    loan_term_years : int
        The loan term in years.

    interest_rate : float
        The annual interest rate (in percentage) on the loan.

    Returns:
    -------
    float
        The maximum loan amount the borrower is eligible for, rounded to 2 decimal places.
    """
    if monthly_income < 0 or monthly_expenses < 0 or loan_term_years <= 0 or interest_rate < 0:
        raise ValueError("Inputs must be non-negative, and loan term must be greater than zero.")

    disposable_income = monthly_income - monthly_expenses
    if disposable_income <= 0:
        return 0.0  # No eligibility
    eligible_emi = monthly_income * 0.50 - monthly_expenses
    loan_term_months = loan_term_years * 12
    r = interest_rate / 12 / 100
    emi = eligible_emi
    if r == 0:
        loan_amount = emi * loan_term_months
    else:
        loan_amount = emi * ((1 + r) ** loan_term_months - 1) / (r * (1 + r) ** loan_term_months)
    
    loan_amount = round(loan_amount, 2)  # Round to 2 decimal places
    return loan_amount
# #  --------------------------------------------------7 --------------------------------

def calculate_credit_card_balance(initial_balance, interest_rate, min_payment, months):
    """
    Calculates the outstanding balance of the credit card after making minimum payments
    every month with interest applied.
    
    Parameters:
    - initial_balance: The initial amount owed on the credit card
    - interest_rate: The annual interest rate (in percentage)
    - min_payment: The minimum monthly payment (in percentage or amount)
    - months: The number of months to calculate for

    Returns:
    - The outstanding balance after the given number of months
    """
    if not all(isinstance(val, (int, float)) for val in [initial_balance, interest_rate, min_payment, months]):
        raise TypeError("All inputs must be numbers (int or float).")
    if initial_balance <= 0 or interest_rate <= 0 or min_payment <= 0 or months <= 0:
        raise ValueError("All inputs must be positive numbers.")

    balance = initial_balance
    monthly_interest_rate = interest_rate / 12 / 100  # Convert annual rate to monthly

    for month in range(months):

        balance += balance * monthly_interest_rate
        balance -= min_payment
        if balance < 0:
            balance = 0
            break
    
    return round(balance, 2)

# #  --------------------------------------------------8 --------------------------------
def calculate_taxable_income(gross_income, deductions):
    """
    Calculates taxable income based on gross income and deductions.

    Basic assumptions:
    - Standard deduction of ₹50,000
    - Taxable income = gross income - deductions - standard deduction
    - Taxable income can't be negative
    """

    STANDARD_DEDUCTION = 50000
    taxable_income = gross_income - deductions - STANDARD_DEDUCTION
    return max(0, round(taxable_income, 2))
#
# #  --------------------------------------------------9 --------------------------------


def budget_planner(monthly_income, monthly_expenses):
    """
    Suggests saving and investing plans based on income and expenses.

    Assumptions:
    - Save 20% of surplus
    - Invest 30% of surplus
    - Remaining 50% is free to use or reallocate
    """
    surplus = monthly_income - monthly_expenses

    if surplus <= 0:
        return {
            'surplus': surplus,
            'message': "You are overspending! Consider reducing expenses.",
            'savings': 0,
            'investments': 0,
            'free_to_use': 0
        }

    savings = round(surplus * 0.2, 2)
    investments = round(surplus * 0.3, 2)
    free_to_use = round(surplus * 0.5, 2)

    return {
        'surplus': round(surplus, 2),
        'message': "Good job! Here's how you can allocate your surplus.",
        'savings': savings,
        'investments': investments,
        'free_to_use': free_to_use
    }

# #  --------------------------------------------------10 --------------------------------


def calculate_net_worth(total_assets, total_liabilities):
    """
    Calculate net worth by subtracting total liabilities from total assets.

    Parameters:
    ----------
    total_assets : float
        The total value of assets owned.

    total_liabilities : float
        The total value of liabilities or debts.

    Returns:
    -------
    float
        The calculated net worth, rounded to 2 decimal places.
    """
    net_worth = total_assets - total_liabilities
    return round(net_worth, 2)
