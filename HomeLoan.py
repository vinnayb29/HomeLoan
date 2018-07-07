# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 22:55:38 2018

@author: Vinay
"""

import pandas as pd

fname = r'C:\Users\Vinay\Documents\Home_loan_kaggle\Datasets\application_train.csv'
df_train= pd.read_csv(fname)

fname = r'C:\Users\Vinay\Documents\Home_loan_kaggle\Datasets\bureau.csv'
df_bureau= pd.read_csv(fname)

fname = r'C:\Users\Vinay\Documents\Home_loan_kaggle\Datasets\bureau_balance.csv'
df_bureau_balance= pd.read_csv(fname)

fname = r'C:\Users\Vinay\Documents\Home_loan_kaggle\Datasets\credit_card_balance.csv'
df_credit_card_balance= pd.read_csv(fname)

fname = r'C:\Users\Vinay\Documents\Home_loan_kaggle\Datasets\installments_payments.csv'
df_installments_payments= pd.read_csv(fname)

fname = r'C:\Users\Vinay\Documents\Home_loan_kaggle\Datasets\POS_CASH_balance.csv'
df_POS_CASH_balance= pd.read_csv(fname)

fname = r'C:\Users\Vinay\Documents\Home_loan_kaggle\Datasets\previous_application.csv'
df_previous_application= pd.read_csv(fname)

