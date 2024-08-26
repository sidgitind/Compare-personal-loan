def calculate_interest(principal, interest_rate, tenure, prepayments, prepayment_charges, min_part_payment, max_part_payment, max_prepayments, max_annual_prepayments):
  """Calculates total interest paid based on given parameters.

  Args:
    principal: Initial loan amount.
    interest_rate: Annual interest rate.
    tenure: Loan tenure in years.
    prepayments: A list of prepayment amounts for each year.
    prepayment_charges: A dictionary mapping loan durations to prepayment charges.
    min_part_payment: Minimum part payment allowed.
    max_part_payment: Maximum part payment allowed.
    max_prepayments: Maximum number of prepayments allowed.
    max_annual_prepayments: Maximum number of prepayments allowed per year.

  Returns:
    Total interest paid.
  """

  balance = principal
  total_interest = 0
  prepayments_made = 0
  annual_prepayments_made = 0
  for year, prepayment in enumerate(prepayments):
    if year * 12 < 12 or prepayments_made >= max_prepayments or prepayment == 0:
      continue

    interest = balance * interest_rate
    total_interest += interest
    balance += interest

    if annual_prepayments_made < max_annual_prepayments:
      adjusted_prepayment = max(min(prepayment, max_part_payment), min_part_payment)
      prepayment_charge = prepayment_charges.get(year, 0)
      total_interest += adjusted_prepayment * prepayment_charge / 100
      balance -= adjusted_prepayment
      prepayments_made += 1
      annual_prepayments_made += 1

    # Reset annual prepayments at the start of each year
    if year % 12 == 0:
      annual_prepayments_made = 0

  # Calculate interest for remaining years after prepayments are exhausted
  for remaining_year in range(year + 1, tenure):
    interest = balance * interest_rate
    total_interest += interest
    balance += interest

  return total_interest

def compare_loan_options(principal, interest_rate1, interest_rate2, tenure, prepayments1, prepayments2, prepayment_charges1, prepayment_charges2, min_part_payment1, max_part_payment1, max_prepayments1, min_part_payment2, max_part_payment2, max_prepayments2, max_annual_prepayments1, max_annual_prepayments2):
  """Compares two loan options based on given parameters.

  Args:
    principal: Initial loan amount.
    interest_rate1: Interest rate for option 1.
    interest_rate2: Interest rate for option 2.
    tenure: Loan tenure in years.
    prepayments1: Prepayments for option 1.
    prepayments2: Prepayments for option 2.
    prepayment_charges1: Prepayment charges for option 1.
    prepayment_charges2: Prepayment charges for option 2.
    min_part_payment1: Minimum part payment for option 1.
    max_part_payment1: Maximum part payment for option 1.
    max_prepayments1: Maximum number of prepayments for option 1.
    min_part_payment2: Minimum part payment for option 2.
    max_part_payment2: Maximum part payment for option 2.
    max_prepayments2: Maximum number of prepayments for option 2.
    max_annual_prepayments1: Maximum number of prepayments allowed per year for option 1.
    max_annual_prepayments2: Maximum number of prepayments allowed per year for option 2.

  Returns:
    A tuple containing total interest for option 1 and option 2.
  """

  interest1 = calculate_interest(principal, interest_rate1 / 100, tenure, prepayments1, prepayment_charges1, min_part_payment1, max_part_payment1, max_prepayments1, max_annual_prepayments1)
  interest2 = calculate_interest(principal, interest_rate2 / 100, tenure, prepayments2, prepayment_charges2, min_part_payment2, max_part_payment2, max_prepayments2, max_annual_prepayments2)
  return interest1, interest2

# Example usage
principal = 1500000
interest_rate1 = 11 #hdfc
interest_rate2 = 11.20 # icici
tenure = 6
prepayments1 = [250000, 250000, 25000]  # Option 1 prepayments
prepayments2 = [250000, 250000, 250000, 250000]  # Option 2 prepayments
prepayment_charges1 = {13: 4, 25: 3, 37: 2}  # Prepayment charges for option 1
prepayment_charges2 = {13: 3, 25: 0, 37: 0}  # Prepayment charges for option 2
min_part_payment1 = 90000
max_part_payment1 = 500000
max_prepayments1 = 2
min_part_payment2 = 90000
max_part_payment2 = 300000
max_prepayments2 = 3
max_annual_prepayments1 = 2  # Option 1: Maximum 2 prepayments per year
max_annual_prepayments2 = 3  # Option 2: Maximum 3 prepayments per year

interest1, interest2 = compare_loan_options(principal, interest_rate1, interest_rate2, tenure, prepayments1, prepayments2, prepayment_charges1, prepayment_charges2, min_part_payment1, max_part_payment1, max_prepayments1, min_part_payment2, max_part_payment2, max_prepayments2, max_annual_prepayments1, max_annual_prepayments2)

print("Total interest for option 1:", interest1)
print("Total interest for option 2:", interest2)