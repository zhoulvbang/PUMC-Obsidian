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

print(df.head())
```

