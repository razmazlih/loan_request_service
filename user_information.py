import statistics

def get_credit_score():
    return 600

def get_monthly_income(last_incomes: list[int]) -> int:
    last_year_income = last_incomes[0:12]
    return sum(last_year_income) / len(last_year_income)

def get_debt_to_income_ratio(loan_amount: int, monthly_income: int) -> float:
    return loan_amount / monthly_income

def get_monthly_income_stability(last_incomes: list[int]) -> float:
    last_year_incomes = last_incomes[0:12]
    if not last_year_incomes:
        return 0.0

    avg = sum(last_year_incomes) / len(last_year_incomes)

    std = statistics.stdev(last_year_incomes)
    stability = 1 - (std / avg)
    return max(0.0, min(round(stability, 3), 1.0))

def get_employment_seniority(employment_history: list[bool]) -> int:
    return sum(employment_history[0:12])


def get_collateral_assets(assets: dict[str, int]) -> int:
    return sum(assets.values())

def get_banking_history_quality():
    return 0.9

def gather_user_info(
    loan_amount: int,
    last_year_incomes: list[int],
    employment_history: list[bool],
    assets: dict[str, int]
) -> dict[str, any]:
    """
    Aggregates all of the borrower’s personal and financial data:
    - Calculates monthly income from `last_year_incomes`
    - Computes the debt-to-income ratio
    - Determines monthly income stability
    - Calculates employment seniority
    - Sums up collateral asset values
    - Retrieves banking history quality
    """
    credit = get_credit_score()
    monthly = get_monthly_income(last_year_incomes)
    dti = get_debt_to_income_ratio(loan_amount, monthly)
    stability = get_monthly_income_stability(last_year_incomes)
    seniority = get_employment_seniority(employment_history)
    collateral = get_collateral_assets(assets)
    history_quality = get_banking_history_quality()

    return {
        "credit_score": credit,
        "debt_to_income_ratio": dti,
        "monthly_income": monthly,
        "monthly_income_stability": stability,
        "employment_seniority": seniority,
        "collateral_assets": collateral,
        "banking_history_quality": history_quality,
    }