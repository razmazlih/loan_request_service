# loan_information.py

def calculate_loan_approval_score(
    credit_score: int,
    debt_to_income_ratio: float,
    monthly_income_stability: float,
    employment_seniority: int,
    collateral_assets: int,
    banking_history_quality: float,
) -> float:
    weights = {
        'credit_score': 0.25,
        'debt_to_income_ratio': 0.25,
        'monthly_income_stability': 0.15,
        'employment_seniority': 0.10,
        'collateral_assets': 0.15,
        'banking_history_quality': 0.10,
    }

    score = 0
    score += weights['credit_score'] * min(credit_score / 850, 1)
    score += weights['debt_to_income_ratio'] * (1 - min(debt_to_income_ratio, 1))
    score += weights['monthly_income_stability'] * monthly_income_stability
    score += weights['employment_seniority'] * min(employment_seniority / 10, 1)
    score += weights['collateral_assets'] * min(collateral_assets / 500_000, 1)
    score += weights['banking_history_quality'] * banking_history_quality

    return round(score, 3)


def assess_risk_level(score: float) -> str:
    if score >= 0.8:
        return "Low Risk"
    elif score >= 0.6:
        return "Medium Risk"
    else:
        return "High Risk"
    


def evaluate_loan_application(user_info: dict[str, any]) -> dict[str, any]:
    """
    Takes a dictionary of parameters produced by `gather_user_info`
    and returns:
      - approval_score: float between 0.0 and 1.0 based on weighted factors
      - risk_level: one of "Low Risk", "Medium Risk", or "High Risk"
    """
    score = calculate_loan_approval_score(
        user_info["credit_score"],
        user_info["debt_to_income_ratio"],
        user_info["monthly_income_stability"],
        user_info["employment_seniority"],
        user_info["collateral_assets"],
        user_info["banking_history_quality"],
    )
    risk = assess_risk_level(score)

    return {
        "approval_score": score,
        "risk_level": risk,
    }