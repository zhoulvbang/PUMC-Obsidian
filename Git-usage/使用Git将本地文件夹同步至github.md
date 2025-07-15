# 一、操作过程

## Step 1 创建新仓库

在Github上创建一个New repository作为目标仓库。
## Step 2 初始化仓库

打开 git bash, 进入需要上传的本地文件夹所在的目录（我的目标文件夹为Autp_Loan_Default）。做仓库初始化。

```bash
git init
```

初始化后将在对应的本地文件夹中生成一个新的文件夹 `.git`
## Step 3 添加文件（将文件放入暂存区）

```bash
git add .
```

## Step 4 设定注释信息

```bash
git commit -m "注释信息"
```

在这一步可能会提醒设定git邮箱和用户名

```bash
git config --global "youremail@example.com"
git config --global "username"
```

## Step 5 设定公钥

1、生成ssh key

```bash
ssh-keygen -t rsa -C "youremail@example.com"
```

这一步执行后会生成了相应的公钥，并储存至Users/XXX/.ssh/id_rsa.pub文件中。

2、打开Users/XXX/.ssh/id_rsa.pub，复制出文件中的内容，然后粘贴至github中的SSH keys设定中。详细操作：  
(1) 进入github，打开settings >> 右侧目录选定 “SSH and GPG keys” >> New SSH key；  
(2) 将复制的id_rsa.pub中的内容粘贴至"key"中，点击Add SSH key。

## Step 6 绑定远程仓库

(1) 在github仓库中获取ssh地址，复制。
(2) 绑定本地文件夹与远程仓库

```bash
git remote add origin [SSH]
```
## Step 7 push

```bash
git push -u origin master
```