import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class DataLoader(object):
    def fit(self, dataset):
        self.dataset = dataset.copy()

    def load_data(self):

        self.dataset['company_type'] = self.dataset['company_type'].fillna(0)
        self.dataset['company_type'] = self.dataset['company_type'].replace(['ГТ(б50)', 'ДП'], [1, 2])

        self.dataset['company_status'][self.dataset['company_status'].isnull()] = 0
        self.dataset['company_status'][self.dataset['company_status'] != 0] = 1

        self.dataset['salary_debt_changes'] = self.dataset['salary_debt_changes'].fillna(66.89)

        self.dataset['salary_debt_mark'] = self.dataset['salary_debt_mark'].fillna(2.0)

        self.dataset['salary_average_changes'] = self.dataset['salary_average_changes'].fillna(115.19)

        self.dataset['salary_average_mark'] = self.dataset['salary_average_mark'].fillna(0)

        self.dataset['financial_outturn_sales_percent'] = self.dataset['financial_outturn_sales_percent'].fillna(87.96)

        self.dataset['financial_outturn_sales_percent'] = np.log(self.dataset['financial_outturn_sales_percent'] + 1)

        self.dataset['financial_outturn_sales_mark'] = self.dataset['financial_outturn_sales_mark'].fillna(1)

        self.dataset['financial_outturn_profit_percent'] = self.dataset['financial_outturn_profit_percent'].fillna(219.65)

        self.dataset['financial_outturn_profit_mark'] = self.dataset['financial_outturn_profit_mark'].fillna(1)

        self.dataset['financial_outturn_revenue_to_budget_percent'] = self.dataset[
            'financial_outturn_revenue_to_budget_percent'].fillna(92.37)

        self.dataset['financial_outturn_revenue_to_budget_mark'] = self.dataset[
            'financial_outturn_revenue_to_budget_mark'].fillna(1)

        self.dataset['financial_outturn_revenue_to_state_shareholder_percent'] = self.dataset[
            'financial_outturn_revenue_to_state_shareholder_percent'].fillna(0)

        self.dataset['financial_outturn_revenue_to_state_shareholder_mark'] = self.dataset[
            'financial_outturn_revenue_to_state_shareholder_mark'].fillna(0)

        self.dataset['financial_outturn_capital_investments_percent'] = self.dataset[
            'financial_outturn_capital_investments_percent'].fillna(120.26)

        self.dataset['financial_outturn_capital_investments_mark'] = self.dataset[
            'financial_outturn_capital_investments_mark'].fillna(0)

        self.dataset['profit_changes'] = np.log(self.dataset['profit_changes'] + 1)

        self.dataset['profit_changes'] = self.dataset['profit_changes'].fillna(0)

        self.dataset['profit_mark'] = self.dataset['profit_mark'].fillna(0)

        self.dataset['covering_coefficient_end'] = self.dataset['covering_coefficient_end'].fillna(15.99)

        self.dataset['covering_coefficient_mark'] = self.dataset['covering_coefficient_mark'].fillna(0)

        self.dataset['firmness_coefficient_end'] = np.log(self.dataset['firmness_coefficient_end'].fillna(6.96) + 1)

        self.dataset['firmness_coefficient_end'] = self.dataset['firmness_coefficient_end'].fillna(0.5)

        self.dataset['firmness_coefficient_mark'] = self.dataset['firmness_coefficient_mark'].fillna(0)

        ls1 = []
        for i in self.dataset['solvency_coefficient_end']:
            try:
                ls1.append(float(i))
            except:
                ls2, s = [], ''
                for j in i:
                    if j == ',':
                        ls2.append('.')
                    else:
                        ls2.append(j)
                for j in ls2:
                    s += j
                ls1.append(float(s))

        self.dataset['solvency_coefficient_end'] = np.array(ls1)

        self.dataset['solvency_coefficient_end'] = self.dataset['solvency_coefficient_end'].fillna(0)

        self.dataset['solvency_coefficient_mark'] = self.dataset['solvency_coefficient_mark'].fillna(0)

        self.dataset['amortization_end'] = self.dataset['amortization_end'].fillna(69.1)

        self.dataset['amortization_mark'] = self.dataset['amortization_mark'].fillna(0)

        self.dataset['audition_result'] = self.dataset['audition_result'].replace(
            ['задовільний', 'позитивний', 'негативний'], [1, 2, 0])

        self.dataset['audition_result'] = self.dataset['audition_result'].fillna(0)

        self.dataset['audition_mark'] = self.dataset['audition_mark'].fillna(0)

        self.dataset = self.dataset.drop(['company_name', 'company_code', 'company_status'], axis=1)

        scaler = MinMaxScaler()
        scaler.fit(self.dataset)
        self.dataset = scaler.transform(self.dataset)

        return self.dataset