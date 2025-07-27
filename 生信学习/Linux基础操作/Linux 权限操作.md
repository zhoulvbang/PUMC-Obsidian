1. `chmod`:更改文件或目录的权限
- `chmod u+x script.sh`:给 `script.sh` 文件的用户(所有者)添加可执行权限
- `chmod 755 file.txt` :将 `file.txt` 文件的权限设置为所有者可读写执行，组用户和他人可读可执行
2. `chovn` ：更改文件或目录的所有者
- `chown newuser file.txt` : 将 `file.txt` 文件的所有者更改为 `newuser`
- `chown -R newuser:newgroup directory/`: 递归地将 `directory` 目录及其内容的所有者更改为 `newuser`，所属组更改为 newgroup
3. `chgrp`:更改文件或目录的所属组
- `chgrp newgroup file.txt` : 将 `file.txt` 文件的所属组更改为 `newgroup`