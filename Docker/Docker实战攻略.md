
1. [1. Docker 简介](# 1. Docker 简介)
2. [[2. Docker 安装]]
3. [[3. 下载镜像]]
4. [[4. 运行容器]]
5. [[5. 常用命令示例]]

---

# 1. Docker 简介

**Docker** 是一个开源容器化平台，主要用来“打包”应用及其依赖环境，使应用在不同环境中都能一致运行。

- 容器 ≈ 一个轻量、隔离的系统进程
- 镜像（Image） ≈ 应用及运行环境的快照
- 容器（Container） ≈ 镜像运行时的实例
- Docker Hub ≈ 镜像的公共仓库

优势：  
✅ 快速部署  
✅ 环境一致  
✅ 高效利用资源  
✅ 易于打包和分享

---

## 简易工作流示例

在Windows下的 Linux 中使用 docker

```bash
C:\Users\asus>wsl -d Ubuntu-22.04
zhou@simonzhou:/mnt/c/Users/asus$
```

例如，你想快速部署一个 nginx 服务器：

```bash
docker pull nginx
docker run -d -p 8080:80 --name web nginx
```

访问：

```
http://localhost:8080
```

```bash
zhou@simonzhou:/mnt/c/Users/asus$ sudo docker pull nginx
[sudo] password for zhou:
Using default tag: latest
latest: Pulling from library/nginx
3da95a905ed5: Already exists
037111f539a0: Pull complete
1e537b66692c: Pull complete
d3618cedc15e: Pull complete
63b1ad245775: Pull complete
40c013bb3d47: Pull complete
ec5daaed1d0a: Pull complete
Digest: sha256:f5c017fb33c6db484545793ffb67db51cdd7daebee472104612f73a85063f889
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
zhou@simonzhou:/mnt/c/Users/asus$ sudo docker run -d -p 8080:80 --name mynginx nginx
fe2c3e6be9f5f4e98eda8752cdfc481437fd2c4491edb91b7db0a607dbd47045
```

## 暂停docker

```bash
docker pause mynginx
```

## 恢复docker

```bash
docker unpause <容器名或ID>
```

## 如果你是想“临时停止”容器（而不是暂停进程），请使用：

```bash
docker stop <容器名或ID>`
```

## ❓“pause” 和 “stop” 的区别

|命令|是否中断进程|是否释放资源|可恢复状态|
|---|---|---|---|
|`pause`|❌ 只是挂起|❌ 保留资源|✅ `unpause` 恢复|
|`stop`|✅ 终止进程|✅ 释放资源|❌ 需 `start` 重新运行|
## 查看容器状态

```bash
docker ps -a
```

状态列可能出现：
- `Up`：运行中
- `Paused`：已暂停
- `Exited`：已停止