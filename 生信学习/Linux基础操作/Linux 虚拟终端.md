1. 将命令放到后台执行
- `command &`或运行过程中按下 `Ctrl+Z`
- `fg` 将命令转入前台执行
- `bg` 将命令转入后台执行
- `jobs` 查看后台正在执行的命令
2. `screen`: 终端复用工具，可创建多个终端会话并在其中切换
- `screen` 创建一个新的 screen 会话
- `screen -ls` 列出当前存在的 screen 会话
- `screen -r 会话名`:恢复连接到指定的 screen 会话
3. `tmux`:另一种终端复用工具，功能强大且易于配置
- `tmux` 启动一个新的 `tmux` 会话
- `tmux attach-session -t 会话名` 连接到指定的 tmux 会话
- `tmux list-sessions` 列出所有 tmux 会话