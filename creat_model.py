import pickle
import pandas as pd
from sklearn.svm import SVC
from utils.dataloader import DataLoader
from settings. constants import TRAIN_CSV


raw_train = pd.read_csv(TRAIN_CSV)
x_columns = ['year', 'period', 'company_name', 'company_code', 'company_type',
       'company_status', 'salary_debt_changes', 'salary_debt_mark',
       'salary_average_changes', 'salary_average_mark',
       'financial_outturn_sales_percent', 'financial_outturn_sales_mark',
       'financial_outturn_profit_percent', 'financial_outturn_profit_mark',
       'financial_outturn_revenue_to_budget_percent',
       'financial_outturn_revenue_to_budget_mark',
       'financial_outturn_revenue_to_state_shareholder_percent',
       'financial_outturn_revenue_to_state_shareholder_mark',
       'financial_outturn_capital_investments_percent',
       'financial_outturn_capital_investments_mark', 'profit_changes',
       'profit_mark', 'covering_coefficient_end', 'covering_coefficient_mark',
       'firmness_coefficient_end', 'firmness_coefficient_mark',
       'solvency_coefficient_end', 'solvency_coefficient_mark',
       'amortization_end', 'amortization_mark', 'audition_result',
       'audition_mark', 'total_mark']

y_column = ['final_assessment']
x_raw = raw_train[x_columns]
loader = DataLoader()
loader.fit(x_raw)
X = loader.load_data()
y = raw_train.final_assessment
y = y.replace(['ефективна', 'неефективна', 'задовільна'],[2, 0 ,1])

model = SVC(probability=True)
model.fit(X, y)
with open('models/SVC.pickle', 'wb')as f:
    pickle.dump(model, f)