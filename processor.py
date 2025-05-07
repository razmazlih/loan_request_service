import pandas as pd
from user_information import gather_user_info
from loan_information import evaluate_loan_application
from load_data import load_data

def sort_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.sort_values(by=['risk_level'], ascending=[True])

def process_loan_data(file_path: str) -> pd.DataFrame:
    df = load_data(file_path)

    results = []

    for _, row in df.iterrows():
        user_id = row["user_id"]
        loan_amount = row["loan_amount_requested"]
        incomes = row["incomes"]
        assets = row["assets"]
        employment = [bool(i) for i in incomes]

        user_info = gather_user_info(
            loan_amount=loan_amount,
            last_year_incomes=incomes,
            employment_history=employment,
            assets=assets
        )

        evaluation = evaluate_loan_application(user_info)

        data_to_append = {
            "user_id": user_id,
            "loan_amount": loan_amount,
            "credit_score": user_info["credit_score"],
            "monthly_income": round(user_info["monthly_income"], 2),
            "debt_to_income_ratio": round(user_info["debt_to_income_ratio"], 2),
            "income_stability": user_info["monthly_income_stability"],
            "employment_seniority": user_info["employment_seniority"],
            "collateral_assets": user_info["collateral_assets"],
            "approval_score": evaluation["approval_score"],
            "risk_level": evaluation["risk_level"]
        }

        results.append(data_to_append)

    df = pd.DataFrame(results)

    return sort_df(df)