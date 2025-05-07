from processor import process_loan_data

def main():
    results_df = process_loan_data("loan_data_assets_dict.csv")
    print(results_df)
    results_df.to_csv("loan_evaluation_results.csv", index=False)

if __name__ == "__main__":
    main()