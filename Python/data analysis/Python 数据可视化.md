#python #可视化 

# 数据可视化简介

![[数据可视化简介.png]]

# matplotlib

![[matplotlib-function.png]]![[matplotlib原理.png]]

# 案例目标

- Goal: Develop a state-of-the-art risk management strategy for providing loans to different communities across the United States
- Dataset: Loans from Lending Tree, a peer-to-peer lending platform
- Task: Conducting exploratory data analysis to better understand the characteristics of loans with different levels of risk 
	- Develop a report of findings to share with the bank
	- Develop insightful visualizations to help client understand different risk profiles

# 数据集

**[Loan-Approval-Classification-Dataset](https://github.com/CR7-800/Loan-Approval-Classification-Dataset)**

数据集来自 kaggle 中的 [# Loan Approval Classification Dataset](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data)

## About Dataset

## 1. **Data Source**

This dataset is a synthetic version inspired by the original [Credit Risk dataset on Kaggle](https://www.kaggle.com/datasets/laotse/credit-risk-dataset) and enriched with additional variables based on [Financial Risk for Loan Approval data](https://www.kaggle.com/datasets/lorenzozoppelletto/financial-risk-for-loan-approval). SMOTENC was used to simulate new data points to enlarge the instances. The dataset is structured for both categorical and continuous features.

## 2. **Metadata**

The dataset contains 45,000 records and 14 variables, each described below:

|Column|Description|Type|
|---|---|---|
|`person_age`|Age of the person|Float|
|`person_gender`|Gender of the person|Categorical|
|`person_education`|Highest education level|Categorical|
|`person_income`|Annual income|Float|
|`person_emp_exp`|Years of employment experience|Integer|
|`person_home_ownership`|Home ownership status (e.g., rent, own, mortgage)|Categorical|
|`loan_amnt`|Loan amount requested|Float|
|`loan_intent`|Purpose of the loan|Categorical|
|`loan_int_rate`|Loan interest rate|Float|
|`loan_percent_income`|Loan amount as a percentage of annual income|Float|
|`cb_person_cred_hist_length`|Length of credit history in years|Float|
|`credit_score`|Credit score of the person|Integer|
|`previous_loan_defaults_on_file`|Indicator of previous loan defaults|Categorical|
|`loan_status` (target variable)|Loan approval status: 1 = approved; 0 = rejected|Integer|