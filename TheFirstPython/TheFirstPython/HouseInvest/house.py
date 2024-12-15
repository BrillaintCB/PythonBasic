import matplotlib.pyplot as plt
import numpy as np

# Constants for all cases
start_year = 2025
end_year = 2055
sp500_annual_return = 0.07
rent_increase_rate = 0.05
house_appreciation_rate = 0.03
mortgage_interest_rate_case2 = 0.05
mortgage_interest_rate_case3 = 0.05

# Shared initial conditions
initial_assets = 45000  # Starting assets for all cases
monthly_income = 3300

# Case 1: Renting and Investing
case1_monthly_rent = 1300
case1_monthly_investment = 2000
case1_assets = initial_assets

# Case 2: Buying a 1-Bedroom House
case2_house_value = 250000
case2_deposit = initial_assets  # Initial deposit
case2_mortgage_principal = case2_house_value - case2_deposit  # Mortgage loan amount
case2_loan_term_years = 15
case2_monthly_mortgage = 1779
mortgage_balance_case2 = case2_mortgage_principal  # Initial mortgage balance
investment_value_case2 = 0  # Start with no investments after deposit
assets_over_time_case2 = []
months_paid = 0

case4_mortgage_principal = case2_mortgage_principal  # Same house and deposit as Case 2
case4_monthly_mortgage = 1335
mortgage_balance_case4 = case4_mortgage_principal  # Initial mortgage balance
investment_value_case4 = 0  # Start with no investments
assets_over_time_case4 = []
months_paid_case4 = 0

# Case 3: Buying a 2-Bedroom House and Letting One Room
case3_house_value = 450000
case3_stamp_duty = 1250
case3_loan_term_years = 30
case3_monthly_mortgage = 2367
case3_tenant_rent = 800
tenant_rent_increase_rate = 0.03
case3_assets = initial_assets - case3_stamp_duty

# Function to calculate compound growth of investments
def calculate_investment_growth(initial, monthly, annual_rate, months):
    monthly_rate = (1 + annual_rate) ** (1/12) - 1
    future_value = initial * (1 + monthly_rate) ** months
    for month in range(int(months)):
        future_value += monthly * (1 + monthly_rate) ** (months - month - 1)
    return future_value

# Function to calculate remaining mortgage balance
def calculate_mortgage_balance(principal, annual_rate, term_years, months_paid):
    monthly_rate = (1 + annual_rate) ** (1/12) - 1
    total_months = term_years * 12
    balance = principal * ((1 + monthly_rate) ** total_months - (1 + monthly_rate) ** months_paid) / ((1 + monthly_rate) ** total_months - 1)
    return balance

# Case 1: Renting and Investing
current_rent = case1_monthly_rent
investment_value_case1 = case1_assets
assets_over_time_case1 = []

years = list(range(start_year, end_year + 1))
for year in years:
    for month in range(12):
        disposable_income = monthly_income - current_rent
        investment_value_case1 = calculate_investment_growth(investment_value_case1, disposable_income, sp500_annual_return, 1)
    current_rent *= (1 + rent_increase_rate)
    assets_over_time_case1.append(investment_value_case1)

for year in years:
    for month in range(12):
        if mortgage_balance_case2 > 0:
            # Pay mortgage with monthly income and calculate remaining balance
            disposable_income = monthly_income - case2_monthly_mortgage
            investable_income = disposable_income  # All disposable income goes to investments
            mortgage_balance_case2 -= case2_monthly_mortgage
            months_paid += 1
            mortgage_balance_case2 = max(0, mortgage_balance_case2)  # Ensure no negative balance
            
            # Invest any remaining disposable income
            investment_value_case2 = calculate_investment_growth(investment_value_case2, investable_income, sp500_annual_return, 1)
        else:
            # Once mortgage is paid off, invest the entire monthly income
            investment_value_case2 = calculate_investment_growth(investment_value_case2, monthly_income, sp500_annual_return, 1)

    # Calculate total assets at the end of the year
    house_value = case2_house_value * (1 + house_appreciation_rate) ** (year - start_year)
    total_assets_case2 = round(investment_value_case2 + house_value, 2) if mortgage_balance_case2 == 0 else round(investment_value_case2 + house_value - mortgage_balance_case2, 2)
    assets_over_time_case2.append(total_assets_case2)
    print(f"Year: {year}, Mortgage Balance: {round(mortgage_balance_case2, 2)}, Investment Value: {round(investment_value_case2, 2)}, Total Assets: {total_assets_case2}")


# Case 3: Buying a 2-Bedroom House and Letting One Room
mortgage_balance_case3 = case3_house_value - (case3_assets + case3_stamp_duty)
investment_value_case3 = case3_assets
assets_over_time_case3 = []

tenant_rent = case3_tenant_rent

for year in years:
    for month in range(12):
        disposable_income = monthly_income + tenant_rent - case3_monthly_mortgage
        investment_value_case3 = calculate_investment_growth(investment_value_case3, disposable_income, sp500_annual_return, 1)
    tenant_rent *= (1 + tenant_rent_increase_rate)
    months_paid = (year - start_year + 1) * 12
    mortgage_balance_case3 = calculate_mortgage_balance(case3_house_value - (case3_assets + case3_stamp_duty), mortgage_interest_rate_case3, case3_loan_term_years, months_paid)
    total_assets_case3 = investment_value_case3 + (case3_house_value - mortgage_balance_case3)
    assets_over_time_case3.append(total_assets_case3)

for year in years:
    for month in range(12):
        if mortgage_balance_case4 > 0:
            # Pay mortgage with monthly income
            disposable_income = max(0, monthly_income - case4_monthly_mortgage)
            # Use all disposable income to pay down mortgage
            mortgage_balance_case4 -= disposable_income
            months_paid_case4 += 1
            mortgage_balance_case4 = max(0, mortgage_balance_case4)  # Ensure no negative balance
        else:
            # Once the mortgage is paid off, invest the full income
            investment_value_case4 = calculate_investment_growth(investment_value_case4, monthly_income, sp500_annual_return, 1)

    # Calculate total assets at the end of the year
    house_value = case2_house_value * (1 + house_appreciation_rate) ** (year - start_year)
    total_assets_case4 = round(investment_value_case4 + house_value, 2) if mortgage_balance_case4 == 0 else round(investment_value_case4 + house_value - mortgage_balance_case4, 2)
    assets_over_time_case4.append(total_assets_case4)
    print(f"Year: {year}, Investment Value: {round(investment_value_case4, 2)}, Mortgage Balance: {round(mortgage_balance_case4, 2)}, Total Assets: {total_assets_case4}")

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(years, assets_over_time_case1, label="Case 1: Renting and Investing", linestyle='-', marker='o')
plt.plot(years, assets_over_time_case2, label="Case 2: Buying 1-Bedroom focus on morgage", linestyle='--', marker='s')
plt.plot(years, assets_over_time_case3, label="Case 3: Buying 2-Bedroom with Tenant", linestyle='-.', marker='x')
plt.plot(years, assets_over_time_case4, label="Case 4: Buying 1-Bedroom focus on s&p", linestyle=':', marker='d')

plt.title("Total Assets Comparison Over 30 Years (2025-2055)", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Total Assets (£)", fontsize=12)
plt.grid(True)
plt.legend()
plt.show()
