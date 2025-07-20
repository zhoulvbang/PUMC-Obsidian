 # **一、仓库基础操作**

## 初始化本地仓库：`git init`

```bash
# 进入你的项目文件夹
cd my-project
# 初始化本地仓库
git init
```

## 克隆远程仓库到本地：`git clone`

```bash
# 克隆远程仓库到本地
git clone https://github.com/user/repo.git
# 克隆指定分支
git clone -b develop https://github.com/user/repo.git
```

# **二、提交与修改**

## 查看当前状态：`git status`

```bash
# 查看当前状态（未跟踪的文件会显示为红色）
git status
# 简短版状态（-s参数）
git status -s
```

## 输出结果

```bash
?? new-file.txt   # 未跟踪
M  modified-file.js # 已修改未暂存
A  added-file.css  # 已暂存
```
## 添加文件：`git add .`

```bash
# 添加单个文件
git add index.html
# 添加所有修改（包括新文件和修改的文件）
git add .
# 添加所有.js文件
git add *.js
```

## 提交到本地：`git commit`

```bash
# 提交并写提交信息
git commit -m "修复用户登录页面布局错位问题"
# 添加遗漏文件到上次提交（比如忘记add某个文件）
git add missing-file.txt
git commit --amend --no-edit  # 不修改提交信息
```

# **三、分支管理**

## 查看分支：`git branch`

```bash
# 查看本地分支列表
git branch
# 查看远程分支
git branch -r
# 查看所有分支（本地+远程）
git branch -a
```

## 创建新分支：`git branch <分支名>`

```bash
# 创建新功能分支
git branch feat/user-profile
# 创建并切换到新分支（推荐）
git checkout -b fix/login-bug
```

## 切换分支：`git checkout`

```bash
# 切换分支
git checkout develop
# 快速创建并切换分支（等价于 git branch + git checkout）
git checkout -b hotfix/urgent
```

## 合并分支：`git merge`

```bash
# 合并分支（假设当前在main分支）
git merge feature/new-api
# 遇到冲突时：
# 1. 手动解决冲突文件中的<<<<<<<标记
# 2. 重新add并commit
```

# **四、远程协作**

## 拉取远程分支：`git pull`

```bash
# 拉取远程分支更新（相当于git fetch + git merge）
git pull origin main
# 推荐使用 rebase 方式拉取（保持提交历史线性）
git pull --rebase origin main
```

## 推送到本地分支或远程分支：`git push`

```bash
# 首次推送本地分支到远程
git push -u origin feat/search
# 后续推送可简写
git push
# 强制推送（谨慎使用！会覆盖远程历史）
git push -f origin main
```

## 远程仓库：`git remote`

```bash
# 查看已配置的远程仓库
git remote -v
# 添加新的远程仓库
git remote add upstream https://github.com/original/repo.git
```

# **五、撤销与急救**

## 撤销：`git checkout -- <文件>`

```bash
# 撤销单个文件的修改（危险！不可恢复）
git checkout -- src/components/Button.js
# 撤销所有未暂存的修改（慎用！）
git checkout -- .
```

## 回退：`git reset`

```bash
# 将暂存区的文件移出（保留工作区修改）
git reset HEAD package.json
# 回退到指定提交（保留工作区文件）
git reset a1b2c3d
# 彻底回退到某个提交（丢弃所有后续修改）
git reset --hard a1b2c3d
```

## 提交：`git commit --amend`

```bash
# 修改最后一次提交信息
git commit --amend -m "新的提交信息"
# 添加漏掉的文件到上次提交
git add forgotten-file.js
git commit --amend --no-edit
```

# **六、查询与调试**

## 日志：`git log`

```bash
# 简洁版提交历史（单行显示）
git log --oneline
# 带分支图的日志（推荐）
git log --graph --abbrev-commit --decorate
# 查看某个文件的修改历史
git log -p src/utils/helper.js
```

## 比较：`git diff`

```bash
# 比较工作区和暂存区的差异
git diff
# 比较暂存区和最新提交的差异
git diff --staged
# 比较两个分支的差异
git diff main..develop
```

## 查看：`git show`

```bash
# 查看某次提交的详细信息
git show a1b2c3d
# 查看某次提交中某个文件的变化
git show a1b2c3d:src/app.js
```

# **七、临时存储**

## 临时保存：`git stash`

```bash
# 临时保存所有未提交的修改
git stash
# 保存时添加注释
git stash save "正在调试登录功能，临时保存"
# 查看存储列表
git stash list
```

## 恢复最近一次的暂存内容：`git stash pop`

```bash
# 恢复最近一次的暂存内容（并删除stash记录）
git stash pop
# 应用某个stash但不删除记录
git stash apply stash@{1}
```

# **实战场景示例**

## 场景1：误删文件

```bash
# 删除文件后突然发现需要恢复
rm important.js
git checkout HEAD -- important.js
```

## 场景2：提交到错误分支

```bash
# 1. 切换到正确分支
git checkout correct-branch
# 2. 移植提交
git cherry-pick a1b2c3d
# 3. 删除错误分支上的提交
git checkout wrong-branch
git reset --hard HEAD~1
```

## 场景3：合并后想取消

```bash
# 查看合并前的提交记录
git reflog
# 回退到合并前的状态
git reset --hard HEAD@{1}
```

# 学习建议

1. **优先掌握这些命令的常规用法**，遇到特殊需求再查文档。
2. **用`-h`参数快速查看帮助**：`git push -h`。
3. **常用别名配置**（在`~/.gitconfig`中添加）：

```kconfig
[alias]
    co = checkout
    br = branch
    ci = commit
    st = status
    lg = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

记住：**不要试图背诵所有命令**，就像你不会记住所有手机App的功能一样。实际开发中遇到问题时，只需要：

1. 明确你要达到什么目的（例如"撤销上次提交"）。
2. 搜索"git 如何撤销上次提交" 。
3. 找到对应命令（比如`git reset HEAD~1`） 。
4. 查看文档确认用法。

附一张常用命令的**思维导图**供参考：

```bash
Git核心命令
├─ 本地操作
│  ├─ 提交三部曲：add → commit → (amend)
│  └─ 撤销三剑客：checkout → reset → reflog
├─ 分支管理
│  ├─ 日常：branch → checkout → merge
│  └─ 高级：rebase → cherry-pick
└─ 远程协作
   ├─ 拉取：fetch → pull
   └─ 推送：push → (force push)
```