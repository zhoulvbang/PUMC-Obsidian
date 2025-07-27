1. `cat`:连接文件并打印到标准输出，`zcat` :可以查看压缩包中的文件
- `cat file.txt` : 显示 `file.txt` 文件的内容
- `cat filel.txt file2.txt > combined.txt` 将 `file1.txt` 和 `file2.txt` 的内容合并后输出到 `combined.txt` 文件中
2. `head`:显示文件开头部分
- `head -n 5 file.tx`:显示 `file.txt` 文件的前5 行内容
3. `tail` 显示文件结尾部分
- `tail -n 5 file.txt` 显示 `file.txt` 文件的后5 行内容
- `tail -f logfile.txt` 实时显示 `logfile.txt` 文件的末尾新增内容，常用于查看日志文件的最新更新
4. `less` 分页显示文件内容
- `less largefile.txt` 分页显示 largefile.txt 文件的内容，可通过空格键翻页，b键返回上一页，q 键退出
5. `-S` 数据展示不折行
6. cut: 截取数据
- `cut -d ',' -f 1.3 file.csv` 以逗号为分隔符，提取 file.csv 文件中第1和第3列的数据
7. `paste`:将多个文件的行并排粘贴
- `paste file1.txt file2.txt > combined.txt` 将 file1.txt 和 file2.txt 的对应行并排输出到 combined.txt 文件中
8. `grep` : 搜索文本模式
- `grep "pattern" file.txt` 在 fie.txt 文件中搜索包含 "pattern" 的行
- `grep -i "pattern" fille.txt`  忽略大小写地搜索包含 "pattern" 的行
- `grep -r "pattern" directory/` 在 directory 目录及其子目录中递归搜索包含"pattern"的文件
9. `find` :查找文件
- `find /path/to/search -name "filename"` 在目录中查找特定文件
- `find /path/to/search -type f -name "*.txt"` 查找特定类型的文件
- `find /path/to/search -type f mtime -7` :查找最近修改过的文件
- `find /path/to/search -name "temp*.log" -type f-exec rm{}\`:查找并删除文件
10. `sed` : 流编辑器，用于文本替换、删除、插入等操作
- `sed 's/oldpattern/newpaltern/g’ file.txt`: 将 file.txt 文件中所有的 `oldpattern` 替换为 `newpattern`
- `sed -i '1d' file.txt`: 直接修改 `file.txt` 文件，`1d` 表示删除第一行
- `sed -n '1~2p'` : 跟在 `cat file.txt -n | ` 后只打印奇数行，`2p` 表示每隔一行打印一个
11. `awk` ： 强大的文本处理工具，用于格式化文本、进行计算、筛选等
- `awk '{print $1, $3}' file.txt` 打印 `file.txt` 文件中每行的第1和第3列 
- 选择 `$2=="chr1"` 和 `$3>30000000` 的数据：`cat 3.txt -n awk '$2=="chr1" && $3>30000000'`,如果需要打印，在后面加上: `{print $2,$3}`
