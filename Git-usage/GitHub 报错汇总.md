# tables of contents


# unable to access GitHub

> fatal: unable to access 'https://github.com/zhoulvbang/PUMC-Obsidian.git/': Could not resolve host: github.com

在使用 Git 进行代码管理的过程中，经常会遇到各种各样的问题，其中之一就是在执行 git clone 或 git pull 等操作时出现 “fatal: unable to access ‘https://github.com/…/.git’: Recv failure Connection was reset” 的报错。这个问题通常是由网络连接问题或代理设置不正确导致的。在我的个人使用经验中，我亲自尝试了两种方法，它们都能够有效地解决这个报错。

## 方法一：取消代理设置

这是最常见的解决方法之一，通过在终端执行以下命令，可以取消 Git 的代理设置：

```bash
git config --global --unset http.proxy 
git config --global --unset https.proxy
```

这样就可以清除 Git 的代理设置，让其直接连接网络进行操作。
但是在2025-07-16的实操中，该办法不稳定。

## 方法二：设置系统代理

有时候取消代理设置仍然会出现报错，这时可以通过设置系统代理来解决。具体步骤如下：

1. 打开系统设置，搜索代理设置，并点击编辑按钮。
2. 在代理服务器中，将端口设置为7890或其他（这个端口不会影响正常上网，可以放心设置），然后点击保存。
3. 1. 在终端输入以下命令，设置 Git 使用本地代理：

```bash
git config --global http.proxy http://127.0.0.1:7890
```

设置完成后，可以通过以下命令检验是否设置成功：

```bash
git config --global -l
```

##  修复记录

```bash
E:\Obsidian\PUMC-Obsidian>git add .

E:\Obsidian\PUMC-Obsidian>git commit -m "update"
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

E:\Obsidian\PUMC-Obsidian>git push
fatal: unable to access 'https://github.com/zhoulvbang/PUMC-Obsidian.git/': Could not resolve host: github.com

E:\Obsidian\PUMC-Obsidian>git config --global --unset http.proxy

E:\Obsidian\PUMC-Obsidian>git config --global --unset https.proxy

E:\Obsidian\PUMC-Obsidian>git push
fatal: unable to access 'https://github.com/zhoulvbang/PUMC-Obsidian.git/': Could not resolve host: github.com

E:\Obsidian\PUMC-Obsidian>git config --global http.proxy http://127.0.0.1:7890

E:\Obsidian\PUMC-Obsidian>git config --global http.proxy http://127.0.0.1:7619

E:\Obsidian\PUMC-Obsidian>git config --global -l
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
filter.lfs.clean=git-lfs clean -- %f
user.name=zhoulvbang
user.email=simonzhou01@outlook.com
http.sslverify=false
http.postbuffer=524288000
http.proxy=http://127.0.0.1:7619
core.editor="E:\VSCode\Microsoft VS Code\bin\code" --wait

E:\Obsidian\PUMC-Obsidian>git push
Enumerating objects: 30, done.
Counting objects: 100% (30/30), done.
Delta compression using up to 8 threads
Compressing objects: 100% (19/19), done.
Writing objects: 100% (19/19), 25.93 KiB | 2.88 MiB/s, done.
Total 19 (delta 9), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (9/9), completed with 9 local objects.
To https://github.com/zhoulvbang/PUMC-Obsidian.git
   e634c6a..e476585  main -> main
```

2025-07-17，一般会挂VPN，需要注意把VPN的端口也调整为 `git config --global http.proxy http://127.0.0.1:7890` 中设置的端口。

2025-07-18，挂了VPN后，port 一致，但是push报错，解决办法：关闭VPN，退出clash，然后解除proxy，再重新push，成功。

---
2025-07-22

![[unable to access.png]]

将VPN和setting中的proxy页面都关闭后重启再上传。