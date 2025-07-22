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
df
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
df.colums
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

