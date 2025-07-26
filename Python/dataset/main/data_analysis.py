'''
一个 Python 数据分析的代码
author: simonzhou
date: 2025-07-23
'''

import pandas as pd

df = pd.read_csv("E:/Obsidian/PUMC-Obsidian/Python/dataset/survey_data.csv",low_memory=False)

# print the default row - 5
print(df.head())

# 查看所有列名
print(df.columns) # 添加 print()

# 查看数据类型
print(df.dtypes) # 添加 print()

# 查看数据类型信息
df.info()


languages = df["LanguageAtHome"]

# check type
print(type(languages)) # 添加 print()

print(languages.head()) # 添加 print()

# check length
print(len(languages)) # 添加 print()

# unique
unique_languages = pd.unique(languages)
print(unique_languages) # 添加 print()

# how much languages
print(len(unique_languages))

# 计数、求和和直方图
age = df["Age"]
age.hist()

# fix color
age.hist(bins=20,color = "skyblue",edgecolor="black",alpha=0.7)

# check the count
age.count()

df.count()

hours = df["HoursLearning"]
hours.hist(bins=20,color = "skyblue",edgecolor="black",grid = False,alpha=0.7)

hours.sum()

# sort and rank
df_sorted_by_age = df.sort_values(by="Age")

type(df_sorted_by_age)

len(df_sorted_by_age)

df_sorted_by_age.head()

# ascending
df_sorted_by_age = df.sort_values(by="Age",ascending = False)
df_sorted_by_age.head()

# 数据筛选

