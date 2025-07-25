#python #data-analysis #guide 
# 导入函数

- Automatically have access tomany built-in Python functions
- Borrow other code using

```python
import
```
![[import modules.png]]

# pandas

![[pandas.png]]
## how to use pandas

![[data analysis.png]]

## 查看数据源

[2016-new-coder-survey](https://github.com/FreeCodeCamp/2016-new-coder-survey)

下载数据：> https://github.com/freeCodeCamp/2016-new-coder-survey/blob/master/clean-data/2016-FCC-New-Coders-Survey-Data.csv

可以将数据集与程序放置在同一个文件夹下，以方便程序调用数据集。

```python
print("Vault path:", @vault_path)
```

```python
import pandas as pd

df = pd.read_csv("E:/Obsidian/PUMC-Obsidian/Python/dataset/survey_data.csv", low_memory=False)

print(type(df))

# check out
print(df)
```

![[read csv.png]]

## explore dataset

```python
import pandas as pd

df = pd.read_csv("E:/Obsidian/PUMC-Obsidian/Python/dataset/survey_data.csv", low_memory=False)

# print the default row - 5
print(df.head())
```

可以在 `df.head(?)` 指定你需要查看的行数。

使用 `df.sample()` 查看 `df` 中的随机一行，如果给定数值，则出随机给出对应 ？ 行随机数据。

查看所有的列名：

```python
df.columns
```

查看每列数据的数据类型，主要类型有 string、float、object 等。

```python
df.dtypes
```

总结所有的数据类型信息：

```python
df.info()
```

![[object type.png]]

## 属性和方法

![[attributes and methods.png]]

### analogy

![[analogy-attributes-methods.png]]
## 列选择

![[selection.png]]

查看制定的一列：

```python
languages = df["LanguageAtHome"]

# check type
type(languages)

print(languages.head())

# check length
print(len(languages))

# unique
unique_languages = pd.unique(language)
print(unique_languages)

# how much languages
pringt(len(unique_languages))
```

![[selecting coloums.png]]
## 计数、求和与直方图

```python
age = df["Age"]
age.hist()
```

![[count-sum-hist.png]]
## 数据排序

```python
# default
df_sorted_by_age = df.sort_values(by="Age")

type(df_sorted_by_age)

len(df_sorted_by_age)

df_sorted_by_age.head()

# ascending
df_sorted_by_age = df.sort_values(by="Age",ascending = False)
df_sorted_by_age.head()
```

![[sort-rank.png]]
## 多列排序

```python
# sort by age descending, then hours spent studying descending
# find highest studiers by age
columns =["Age","HoursLearning"]
order =[False,False]

sorted_by_age_and_hours = df.sort_values(by=columns, ascending=order)
type(sorted_by_age_and_hours)
len(sorted_by_age_and_hours)
sorted_by_age_and_hours.head()
```

![[multi-columns-sort.png]]

## 筛选数据

```python
unique_genders = pd.unique(df["Gender"])
print(unique_genders)

female_respondents = df[df["Gender"] == "female"]
type(female_respondents)
female_respondents.head()

len(female_respondents)
len(female_respondents) / len(df)

female_respondents["Age"].hist()
```

![[select data.png]]
## 多条件筛选

```python
female_and_above_30 = df[(df["Gender"] == "female") & (df["Age"] >= 30 )]

len(female_and_above_30)

female_and_above_30.sample(10)
```

![[多条件筛选.png]]

## 行选择

![[行选择-1.png]]

```python
df['RowID'] = range(len(df))
index_df = df.set_index("RowID")
index_df.head()

# loc
index_df.loc[14354]

response_1001 = index_df.iloc[1000]
type(response_1001)
# output：pandas.core.series.Series

response_1001.index

# 从8888开始的5行，一个切片数据框
range_of_rows = index_df.iloc[8888:8893]

type(range_of_rows)
# output：pandas.core.frame.DataFrame

# 显示切片
range_of_rows
```

因为从 csv 导入的数据中没有定义 ID，这里定义一个 ID，用排序做 ID。

![[行选择-2.png]]

![[行选择-3-切片.png]]

## 集中趋势、离散趋势与偏态

```python
# 集中趋势、离散趋势与偏态
hours = df["HoursLearning"]
hours.hist()

# 计算均数
hours.mean()

# 查看中位数
hours.median()

# 计算标准差
hours.std()

# 获得四分位数
hours_25th = hours.quantile(0.25)
hours_50th = hours.quantile(0.5)
hours_75th = hours.quantile(0.75)

print(hours_25th)

# 一起获得百分数
percentiles = hours.quantile([0.25,0.5,0.75])
print(percentiles)

type(percentiles)

# describe
hours.describe()

# 偏态程度
hours.skew()

# 所有的特征describe
df.describe()
```

![[集中-离散趋势-偏态.png]]