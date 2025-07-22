#  [Execute Code](https://github.com/twibiral/obsidian-execute-code?tab=readme-ov-file) 插件

**步骤1：安装插件**  
导航至"设置"，然后选择"第三方插件"。在搜索框中输入并选择 `Execute Code` 进行安装。

**步骤2：配置插件**  
安装完成后，返回"设置"，在"插件选项"中找到并选择 `Execute Code`。在"Python 设置"下，将"Python 路径"设为 Python 解释器路径。例如：`c:/Users/DW/AppData/Local/Programs/Python/Python311/python.exe`。

**步骤3：创建并运行代码块**  
在笔记中，创建一个 Python 代码块，如下所示。**运行代码前，需要切换到"阅读视图"以显示运行按钮。** 点击「run」 按钮，Python 代码将会执行，结果会在 Obsidian 中显示。

```python
import sys

def test():
    for i in sys.argv:
        print(i)
    print('Hello, Obsidian!')   
    return "hello"

if __name__ == '__main__':
    test()
```

## 关键问题

### **Obsidian's Code Runner Doesn't Display All Output**

Some Obsidian plugins that run code might only display errors or the very last line of output. If your script produces a lot of output, or if the output you're looking for isn't the final result, it might be getting suppressed or redirected elsewhere.

**Solution:** Explicitly print the results you want to see. Even if a variable holds a value, it won't be displayed unless you `print()` it.

For example, if you have a DataFrame `df`, simply typing `df` as the last line might not show anything in some runners. You should use `print(df)`:

Python

```python
import pandas as pd

df = pd.read_csv("E:/Obsidian/PUMC-Obsidian/Python/dataset/survey_data.csv", low_memory=False)

# To see the type of df
print(type(df))

# To display the DataFrame content
print(df)
```

---
### **2. Output is Being Redirected to a Log File or Console**

Depending on how your Obsidian code runner plugin is configured, it might be sending the output to:

- **Obsidian's Developer Console:** You can often open this with `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Option+I` (Mac) and look for the "Console" tab. Any `print()` statements from your Python code might appear there.
- **A specific log file:** Some plugins allow you to configure an output log file. Check the settings of the Python execution plugin you're using in Obsidian.

