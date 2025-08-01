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

---
## connection closed

![[connection closed.png]]

原因是使用了 clash 中的 TUN 模式

### **防火墙或网络限制**

`198.18.1.172` 是**一个私有测试网络的保留 IP 段**，**不是正常公网地址**，很可能是：

- 你正在用 VPN、内网代理、公司服务器；
- 或者 Git 设置被错误指向了错误的 IP；

解决办法：

- 修改 `.git/config` 中 `[remote "origin"]` 的 URL 为一个正确的地址；
- 如果你确实在公司服务器，联系管理员确认是否能连接 22 端口；
- 若用的是 GitHub/GitLab，IP 地址不该是 `198.18.*.*`

使用了 **TUN 模式来转发流量**，这说明你可能正在通过 **VPN（例如 Clash、Tailscale、WireGuard、OpenVPN 等）** 进行全局或分流代理。结合你之前的错误：

```
Connection closed by 198.18.1.172 port 22
fatal: Could not read from remote repository.
```

**`198.18.1.172` 是保留 IP 地址段**（专用于测试，见 RFC 2544），**正常情况下不会作为远程仓库地址使用**。这说明：

---

## 🔍 你的问题本质上是：

**VPN 的 TUN 分流/透明代理策略把 `github.com` 或其他 Git 服务器错误解析成了 `198.18.1.172`，导致 Git 无法连接远程仓库。**

---

## ✅ 解决方案一览

### ✅ 方法 1：手动指定 hosts 或使用 fake-ip 模式（推荐）

你很可能使用的是 Clash 或类似配置（`redir-host` + `TUN`），需要：

#### 🔧 修改 `clash.meta` 或 `openclash` 设置：

- **启用 fake-ip 模式**（避免 DNS 被污染或劫持）：

```yaml
dns:
enhanced-mode: fake-ip
```

- 或者添加 `github.com` 的真实 IP 到 hosts：

```yaml
hosts:
'github.com': 140.82.113.4
'ssh.github.com': 140.82.112.20
```

> 可用 ping 或 `dig github.com` 查询真实 IP。

### ✅ 方法 2：强制走代理 / 绕过分流策略

确认你的代理配置中，`github.com`、`gitlab.com` 等 Git 相关域名走了正确的代理节点，而不是被误拦或劫持进了 TUN 的假 IP 流量。

你可以手动将这些域名加入规则（Clash Rule 模式）：

```yaml
rules:
  - DOMAIN-SUFFIX,github.com,Proxy
  - DOMAIN-SUFFIX,gitlab.com,Proxy
  - DOMAIN,github.com,Proxy
```

或使用 `Rule Set` 加载 Git 规则集。

---

## 🧪 临时绕过法（适合验证）

### ✅ 用 `https` 替代 ssh 临时拉取：

```bash
git remote set-url origin https://github.com/yourname/yourrepo.git
git pull --tags origin main
```

这样可以避开 22 端口的 ssh 请求，验证是否是 ssh 被拦了。

---

## 🚧 如果你必须使用 SSH 且 TUN 转发错误：

### 🔄 修改 Git 使用 HTTPS：

```bash
git config --global url."https://github.com/".insteadOf "git@github.com:"
```

这样即便执行 `git clone git@github.com:user/repo.git`，也会变成 HTTPS。

---

## 🔚 总结

|问题本质|VPN 的 TUN 模式错误将 Git 请求引到 198.18.1.172|
|---|---|
|建议方法|启用 fake-ip、设置 hosts、确保 Git 域名走代理|
|临时解决|使用 HTTPS 替代 SSH 拉取、或设置 Git URL 映射|
|常见工具|Clash、Clash.Meta、OpenClash、PassWall、Tailscale|

