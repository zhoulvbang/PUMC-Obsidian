## 文件操作

1. `ls` : 列出目录内容
- `ls` : 列出当前目录下的文件和文件夹
- `ls -l` : 以长格式列出文件和文件夹的详细信息，包括权限、所有者、大小等
- `ls -a` : 列出包括隐藏文件在内的所有文件和文件夹
2. `touch` : 创建空文件或修改文件时间戳
- `touch newfile.txt` : 创建一个名为 `newfile.txt` 的空文件
- `touch -t 202401011200 existingfile.txt` : 将 `existingfile.txt` 的时间戳修改为2024年1月1日12点0分
3. `CP` : 复制文件或目录
- `cp sourcefile txt destinationfile.txt` : 将 `sourcefile.txt` 复制为 `destinationfile.txt`
- `cp -r sourcedir/ destdir/` : 将 `sourcedir` 目录及其内容复制到 `destdir` 目录