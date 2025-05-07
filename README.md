# Loan Evaluation Service

A Python-based service for processing loan applications from a CSV data file. It calculates key financial metrics for each user and evaluates loan approval scores along with risk classification.

## Features

* **Data Loading**: Reads loan requests and user data from a `CSV` file (e.g., `loan_data.csv`).
* **Financial Aggregation**: Computes:

  * Monthly income
  * Debt-to-income ratio
  * Income stability (based on standard deviation)
  * Employment seniority (months employed in the last year)
  * Total collateral asset value
* **Scoring & Risk Assessment**:

  * Configurable weighted scoring algorithm (see `loan_information.py`).
  * Risk classification into Low, Medium, or High risk.
* **Output**:

  * Displays results in a pandas DataFrame.
  * Exports detailed results to `loan_evaluation_results.csv`.

## Prerequisites

* Python 3.8 or higher
* `pip` package manager
* (Recommended) A virtual environment tool such as `venv` or `virtualenv`

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd loan-evaluation-service

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt
```

## Project Structure

```
loan-evaluation-service/
├── main.py                   # Entry point: orchestrates loading, processing, and output
├── processor.py              # Contains process_loan_data() for core logic
├── load_data.py              # Utility to read CSV data into pandas
├── user_information.py       # Gathers and computes individual user metrics
├── loan_information.py       # Scoring algorithm and risk assessment
├── loan_data.csv             # Sample input data file (CSV format)
├── loan_evaluation_results.csv # Example output file (after running main.py)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation (this file)
```

## Usage

1. Place your loan data in `loan_data.csv` with columns: `user_id`, `loan_amount_requested`, `incomes` (as list-like or separate columns), and `assets` (e.g., `car`, `house`, `savings`).
2. Run the processing script:

   ```bash
   python main.py
   ```
3. View printed output table in the console.
4. Check `loan_evaluation_results.csv` for a detailed report.

## Configuration

* **Input Path**: Modify the file path in `processor.py` if your data file is named differently.
* **Scoring Weights**: Adjust in `loan_information.py` under `calculate_loan_approval_score`.