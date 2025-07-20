# Nginx容器的运行位置 

若你是借助WSL（Windows Subsystem for Linux）安装的Linux子系统，并且Docker是安装在WSL环境里，那么运行的Nginx容器就会在WSL的Linux子系统中运行。

这是因为Docker守护进程（Docker daemon）是在Linux子系统内部运转的。

# 进入WSL Linux子系统的方法 

要进入WSL Linux子系统，可直接在Windows的CMD或PowerShell里执行如下命令： 

```bash
wsl
```

要是你安装了多个Linux发行版，想指定进入某一个，可以使用： 

```bash
bash wsl -d <发行版名称>
```

这里的 `<发行版名称>` 可以是Ubuntu、Debian之类的。

# 命令的运行位置 

你给出的命令

```sudo
sudo docker run -d -p 8080:80 -v /website/html:/usr/share/nginx/html nginx
```

应当在WSL的Linux环境中运行。
