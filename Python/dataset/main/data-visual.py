# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 21:17:15 2025

@author: simonzhou
"""

# install packages
# pip install pandas
# pip install matplotlib
# pip install seaborn

# load packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
loan=pd.read_csv(r'E:\Obsidian\PUMC-Obsidian\Python\dataset\loan_data.csv')
loan.head()

# check dataset
print(loan.dtypes)
print(loan.isnull().sum())