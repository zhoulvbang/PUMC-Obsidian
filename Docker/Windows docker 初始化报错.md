![[docker desktop error.png]]
非常好！你遇到的是在 **Docker Desktop + WSL2 + Ubuntu-22.04** 环境下一个常见问题：

> **WSL integration with distro 'Ubuntu-22.04' unexpectedly stopped. Do you want to restart it?**  
> configuring docker in Ubuntu-22.04: docker cli config: failed to write file: exit status 2

意思是：

- Docker Desktop 和 Ubuntu-22.04 (WSL 分发版) 的集成挂掉了
- 尝试写 Docker CLI 配置文件失败（exit status 2 表示系统层面的错误，比如权限、文件系统只读、路径不存在等）

下面给你解决思路。

---

2025-07-17

进入 docker desktop 出现上述报错，目前排查原因应该是因为Windows下安装了次级Linux，这和 docker 中的Linux相冲突。

```bash
C:\Users\asus>wsl -l -v 
NAME STATE VERSION 
* Ubuntu-22.04 Stopped 1 
* docker-desktop Running 2

C:\Users\asus>wsl -d Ubuntu-22.04 
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 4.4.0-19041-Microsoft x86_64)

* Documentation: https://help.ubuntu.com 
* Management: https://landscape.canonical.com 
* Support: https://ubuntu.com/pro

System information as of Thu Jul 17 18:45:17 CST 2025
```

调整
```bash
C:\Users\asus>wsl --set-version Ubuntu-22.04 2
For information on key differences with WSL 2 please visit https://aka.ms/wsl2
Conversion in progress, this may take a few minutes.
The operation completed successfully.
```

```bash
C:\Users\asus>wsl -l -v
  NAME              STATE           VERSION
* Ubuntu-22.04      Running         2
  docker-desktop    Running         2
```

## fix integration

**Check Docker Desktop WSL Integration Settings**

- Open Docker Desktop, go to **Settings > Resources > WSL Integration**.
- Ensure the option "Enable integration with my default WSL distro" is checked.
- Under "Enable integration with additional distros," ensure Ubuntu-22.04 is toggled on.
- Click **Apply & Restart** to reapply the settings.商
---

# ✅ **检查步骤**

## 1. 重启 Docker Desktop

先尝试最简单的方式：

- 点击提示里的 **Restart**
- 或者手动关闭 Docker Desktop，然后重新打开

很多时候这就能恢复 WSL integration。

---

## 2. 检查 WSL 正常运行

在 PowerShell 或 CMD 输入：

```powershell
wsl -l -v
```

应看到类似：

```
  NAME            STATE           VERSION
* Ubuntu-22.04    Running         2
```

若不是 Running，请尝试启动：

```powershell
wsl -d Ubuntu-22.04
```

若仍报错，可以先重启 WSL：

```powershell
wsl --shutdown
```

再重新打开 Docker Desktop。

---

## 3. 检查磁盘空间

Docker Desktop 通过 WSL2 的虚拟磁盘存储镜像和容器，如果磁盘满了也会出现 exit status 2。

运行：

```powershell
wsl --list --verbose
```

再检查 WSL 磁盘使用情况：

```bash
df -h
```

若空间不足，清理一些容器、镜像，或者扩展 WSL vhdx 容量。

---

## 4. 检查权限

有时是配置文件无法写入。

在 Ubuntu-22.04 中运行：

```bash
ls -ld ~/.docker
```

若目录不存在，则新建：

```bash
mkdir -p ~/.docker
```

若权限不对，修复：

```bash
chmod 700 ~/.docker
```

再试：

```bash
docker info
```

或者在 Windows 下检查 `C:\Users\<你的用户名>\.docker` 是否存在权限限制。

---

## 5. 删除并重建 Docker CLI 配置

如果提示：

```
docker cli config: failed to write file
```

那是写入 `~/.docker/config.json` 失败。

在 Ubuntu-22.04：

```bash
rm -f ~/.docker/config.json
```

或者备份再删：

```bash
mv ~/.docker/config.json ~/.docker/config.json.bak
```

然后重新执行 Docker 命令，让系统自动生成新配置。

---

## 6. 升级 Docker Desktop

很多 bug 已在新版修复。

前往官网：  
→ [https://docs.docker.com/desktop/release-notes/](https://docs.docker.com/desktop/release-notes/)

下载最新版本覆盖安装。

---

## 7. 完全重置 Docker Desktop

若以上都不行，可尝试：

- **Docker Desktop → Settings → Troubleshoot → Reset to factory defaults**
⚠️ 会清空所有镜像、容器。

---

# 快速修复命令

如果你想快速试试修复流程，打开 Ubuntu-22.04 (WSL)，执行：

```bash
mkdir -p ~/.docker
chmod 700 ~/.docker
rm -f ~/.docker/config.json
docker info
```

若仍有报错，再去 Windows 的 Docker Desktop 重启或重置。

---

# ⚠️ 若仍失败

如果重启、重置都不行，可能有以下原因：  
✅ WSL2 kernel 太旧  
✅ 磁盘满  
✅ 文件系统损坏  
✅ Docker Desktop bug

告诉我：

- 你的 Windows 版本号
- Docker Desktop 版本号
- 完整错误信息

我可以帮你更精准排查！