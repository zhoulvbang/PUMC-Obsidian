# [设置 WSL 开发环境](https://learn.microsoft.com/zh-cn/windows/wsl/setup/environment)

设置 WSL 开发环境的最佳做法分步指南。 了解如何运行命令以安装默认的 Bash Shell，它使用 Ubuntu，或者可以设置为安装其他 Linux 发行版、使用基本 WSL 命令、设置 Visual Studio Code 或 Visual Studio、Git、Windows 凭据管理器、MongoDB、Postgres 或 MySQL 等数据库、设置 GPU 加速、运行 GUI 应用等。
## 入门

适用于 Linux 的 Windows 子系统随 Windows 操作系统一起提供，但必须先启用它并安装 Linux 发行版，然后才能开始使用它。

若要使用简化的 --install 命令，必须运行最新版本的 Windows（内部版本 20262+）。 要检查您的 Windows 版本和内部版本号，请按 Windows 徽标键 + R，输入“winver”，然后选择“确定”。 可以使用[“设置”菜单](ms-settings:windowsupdate)或 [Windows 更新助手](https://www.microsoft.com/software-download/)进行更新。

如果希望安装除 Ubuntu 以外的 Linux 发行版，或者希望手动完成这些步骤，请参阅 [WSL 安装页](https://learn.microsoft.com/zh-cn/windows/wsl/install)了解更多详细信息。

打开 PowerShell（或 Windows 命令提示符）并输入：

```
wsl --install
```

--install 命令执行以下操作：

- 启用可选的 WSL 和虚拟机平台组件
- 下载并安装最新 Linux 内核
- 将 WSL 2 设置为默认值
- 下载并安装 Ubuntu Linux 发行版（可能需要重新启动）

在此安装过程中，你将需要重启计算机。

![PowerShell command line running wsl --install](https://learn.microsoft.com/zh-cn/windows/wsl/media/wsl-install.png)运行 wsl --install 的 PowerShell 命令行

如果遇到任何问题，请查看[排查安装问题](https://learn.microsoft.com/zh-cn/windows/wsl/troubleshooting)一文。

## 设置 Linux 用户名和密码

使用 WSL 安装 Linux 发行版的过程完成后，使用“开始”菜单打开该发行版（默认情况下为 Ubuntu）。 系统将要求你为 Linux 发行版创建“用户名”和“密码”。

- 此**用户名**和**密码**特定于安装的每个单独的 Linux 分发版，与 Windows 用户名无关。
- 请注意，输入**密码**时，屏幕上不会显示任何内容。 这称为盲人键入。 你不会看到你正在键入的内容，这是完全正常的。
- 创建**用户名**和**密码**后，该帐户将是分发版的默认用户，并将在启动时自动登录。
- 此帐户将被视为 Linux 管理员，能够运行 `sudo` (Super User Do) 管理命令。
- 在 WSL 上运行的每个 Linux 发行版都有其自己的 Linux 用户帐户和密码。 每当添加分发版、重新安装或重置时，都必须配置一个 Linux 用户帐户。
![[Linux username.png]]

```bash
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: zhou
New password:
Retype new password:
passwd: password updated successfully
Installation successful!
Windows Subsystem for Linux is now available in the Microsoft Store!
You can upgrade by running 'wsl.exe --update' or by visiting https://aka.ms/wslstorepage
Installing WSL from the Microsoft Store will give you the latest WSL updates, faster.
For more information please visit https://aka.ms/wslstoreinfo

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 4.4.0-19041-Microsoft x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Thu Jul 10 22:51:39 CST 2025

  System load:    0.52      Processes:              8
  Usage of /home: unknown   Users logged in:        0
  Memory usage:   59%       IPv4 address for wifi0: 192.168.50.176
  Swap usage:     0%


This message is shown once a day. To disable it please create the
/home/zhou/.hushlogin file.
```
### 备注

随 WSL 一起安装的 Linux 发行版是按用户安装，不可与其他 Windows 用户帐户共享。 遇到用户名错误？ [StackExchange：在 Linux 上的用户名中，应使用或不使用哪些字符？](https://serverfault.com/questions/73084/what-characters-should-i-use-or-not-use-in-usernames-on-linux)

![Ubuntu command line enter UNIX username](https://learn.microsoft.com/zh-cn/windows/wsl/media/ubuntuinstall.png)在 Ubuntu 命令行中输入 UNIX 用户名

若要更改或重置密码，请打开 Linux 发行版并输入命令：`passwd`。 系统会要求你输入当前密码，然后要求输入新密码，之后再确认新密码。

如果忘记了 Linux 分发版的密码：

1. 请打开 PowerShell，并使用以下命令进入默认 WSL 分发版的根目录：`wsl -u root`
    
    > 如果需要在非默认的分发版中更新忘记的密码，请使用命令：`wsl -d Debian -u root`，并将 `Debian` 替换为目标分发版的名称。
    
2. 在 PowerShell 内的根级别打开 WSL 发行版后，可使用此命令更新密码：`passwd <username>`，其中 `<username>` 是发行版中帐户的用户名，而你忘记了它的密码。
    
3. 系统将提示你输入新的 UNIX 密码，然后确认该密码。 在您被告知密码已正确更新后，请在 PowerShell 内使用以下命令关闭 WSL：`exit`。
## 更新和升级软件包

建议使用发行版的首选包管理器定期更新和升级包。 对于 Ubuntu 或 Debian，请使用以下命令：

```
sudo apt update && sudo apt upgrade
```

Windows 不会自动更新或升级 Linux 分发版。 大多数 Linux 用户往往倾向于自行控制此任务。
## 添加其他发行版

若要添加其他 Linux 发行版，可以通过 [Microsoft Store](https://aka.ms/wslstore)、通过 [--import 命令](https://learn.microsoft.com/zh-cn/windows/wsl/use-custom-distro)或通过[旁加载你自己的自定义发行版](https://learn.microsoft.com/zh-cn/windows/wsl/build-custom-distro)进行安装。 你可能还希望设置自定义 WSL 映像，以便在企业公司中分发。
## 设置 Windows Terminal

Windows Terminal 可以运行任何具有命令行界面的应用程序。 它的主要功能包括多个选项卡、窗格、Unicode 和 UTF-8 字符支持、GPU 加速文本呈现引擎，你还可用它来创建你自己的主题并自定义文本、颜色、背景和快捷方式。

每当安装新的 WSL Linux 发行版时，都会在 Windows Terminal 中为其创建一个新实例，该实例可根据你的偏好进行自定义。

我们建议将 WSL 与 Windows Terminal 配合使用，特别是在计划同时使用多个命令行界面时。 请参阅 Windows Terminal 文档，了解如何对其进行设置以及如何自定义首选项，包括：

- 从 Microsoft Store [安装 Windows Terminal 或 Windows Terminal（预览版）](https://learn.microsoft.com/zh-cn/windows/terminal/get-started)
- [使用命令面板](https://learn.microsoft.com/zh-cn/windows/terminal/get-started#invoke-the-command-palette)
- 设置键盘快捷方式等[自定义操作](https://learn.microsoft.com/zh-cn/windows/terminal/#custom-actions)，使终端适应你的首选项
- 设置[默认启动配置文件](https://learn.microsoft.com/zh-cn/windows/terminal/customize-settings/startup)
- 自定义外观：[主题](https://learn.microsoft.com/zh-cn/windows/terminal/customize-settings/appearance#theme)、[配色方案](https://learn.microsoft.com/zh-cn/windows/terminal/customize-settings/color-schemes)、[名称和起始目录](https://learn.microsoft.com/zh-cn/windows/terminal/customize-settings/profile-general)、[背景图像](https://learn.microsoft.com/zh-cn/windows/terminal/customize-settings/profile-appearance#background-image)等
- 了解如何使用[命令行参数](https://learn.microsoft.com/zh-cn/windows/terminal/command-line-arguments?tabs=windows)，例如使用拆分为窗口窗格或选项卡的多个命令行打开终端
- 了解[搜索功能](https://learn.microsoft.com/zh-cn/windows/terminal/search)
- 查找[提示和技巧](https://learn.microsoft.com/zh-cn/windows/terminal/tips-and-tricks)，例如如何重命名选项卡或为其着色、使用鼠标交互或启用“Quake 模式”
- 查找有关如何设置[自定义命令提示符](https://learn.microsoft.com/zh-cn/windows/terminal/tutorials/custom-prompt-setup)、[SSH 配置文件](https://learn.microsoft.com/zh-cn/windows/terminal/tutorials/ssh)或[选项卡标题](https://learn.microsoft.com/zh-cn/windows/terminal/tutorials/tab-title)的教程
- 查找[自定义终端库](https://learn.microsoft.com/zh-cn/windows/terminal/custom-terminal-gallery/custom-schemes)和[故障排除指南](https://learn.microsoft.com/zh-cn/windows/terminal/troubleshooting)

![Windows Terminal screenshot](https://learn.microsoft.com/zh-cn/windows/wsl/media/terminal.png)Windows Terminal 屏幕截图

## 文件存储

- 若要在 Windows 文件资源管理器中打开 WSL 项目，请输入：`explorer.exe .`  
    请确保在命令的末尾添加句点以打开当前目录。
    
- [将项目文件与计划使用的工具存储在相同的操作系统上](https://learn.microsoft.com/zh-cn/windows/wsl/filesystems#file-storage-and-performance-across-file-systems)。  
    若想获得最快的性能速度，请将文件存储在 WSL 文件系统中，前提是使用 Linux 工具在 Linux 命令行（Ubuntu、OpenSUSE 等）中处理这些文件。 如果是使用 Windows 工具在 Windows 命令行（PowerShell、命令提示符）中工作，请将文件存储在 Windows 文件系统中。 可以跨操作系统访问文件，但这可能会显著降低性能。
    

例如，在存储 WSL 项目文件时：

- 使用 Linux 文件系统根目录：`\\wsl$\<DistroName>\home\<UserName>\Project`
- 不是 Windows 文件系统的根目录：`C:\Users\<UserName>\Project` 或 `/mnt/c/Users/<UserName>/Project$`

![Windows 文件资源管理器显示 Linux 存储](https://learn.microsoft.com/zh-cn/windows/wsl/media/windows-file-explorer.png)

## 设置你最喜欢的代码编辑器

建议使用 Visual Studio Code 或 Visual Studio，因为它们直接支持使用 WSL 进行远程开发和调试。 Visual Studio Code 使你能够将 WSL 用作功能完备的开发环境。 Visual Studio 提供了对 C++ 跨平台开发的原生 WSL 支持。
### 使用 Visual Studio Code

按照此分步指南开始在 WSL 中使用 Visual Studio Code，其中包括安装远程开发扩展包。 使用此扩展，能够运行 WSL、SSH 或开发容器，以使用整套 Visual Studio Code 功能进行编辑和调试。 在不同的独立开发环境之间快速切换并进行更新，而无需担心会影响本地计算机。

安装并设置 VS Code 后，可以通过输入以下内容使用 VS Code 远程服务器打开 WSL 项目：`code .`

请确保在命令的末尾添加句点以打开当前目录。

![VS Code with WSL extensions displayed](https://learn.microsoft.com/zh-cn/windows/wsl/media/vscode-remote-wsl-extensions.png)VS Code 显示的 WSL 扩展
### 使用 Visual Studio

按照此分步指南[开始将 Visual Studio 与 WSL 一起用于 C++ 跨平台开发](https://learn.microsoft.com/zh-cn/cpp/build/walkthrough-build-debug-wsl2)。 Visual Studio 2022 使你能够从 Visual Studio 的同一实例在 Windows、WSL 发行版和 SSH 连接上生成和调试 CMake 项目。

![Select a target system in Visual Studio 2022](https://learn.microsoft.com/zh-cn/windows/wsl/media/vs-target-system.png)在 Visual Studio 2022 中选择目标系统

## 使用 Git 设置版本管理

按照此分步指南[开始在 WSL 上使用 Git](https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/wsl-git)，并将项目连接到 Git 版本控制系统，同时使用凭据管理器进行身份验证，使用 Git Ignore 文件，了解 Git 行尾，以及使用内置到 VS Code 的 Git 命令。

在命令行中显示 git 版本
## 使用 Docker 设置远程开发容器

开始按照此分步指南来使用 WSL 2 上的 Docker 远程容器，并通过 Windows 的 Docker Desktop 将您的项目连接到远程开发容器。

![Docker Desktop 屏幕截图](https://learn.microsoft.com/zh-cn/windows/wsl/media/docker-running.png)Docker Desktop 屏幕截图
## 设置数据库

按照这份分步指南开始使用 WSL 上的数据库，并将您的项目连接到 WSL 环境中的数据库。 开始使用 MySQL、PostgreSQL、MongoDB、Redis、Microsoft SQL Server 或 SQLite。

![Running MongoDB in Ubuntu via WSL](https://learn.microsoft.com/zh-cn/windows/wsl/media/mongodb.png)在 Ubuntu 中通过 WSL 运行 MongoDB
## 设置 GPU 加速以提高性能

按照这份分步指南，在 WSL 中设置 GPU 加速的机器学习训练，并利用计算机的 GPU（图形处理单元）来加速繁重的性能工作负载。

使用 WSL 进行 GPU 加速运行

## 基本 WSL 命令

通过 WSL 安装的 Linux 发行版最好使用 PowerShell 或 Windows 命令提示符 (CMD) 进行管理。 有关使用 WSL 时需要熟悉的基本命令的列表，请参阅 [WSL 命令参考指南](https://learn.microsoft.com/zh-cn/windows/wsl/basic-commands)。

此外，许多命令在 Windows 和 Linux 之间都具有互操作性。 下面是几个示例：

- [从 Windows 命令行运行 Linux 工具](https://learn.microsoft.com/zh-cn/windows/wsl/filesystems#run-linux-tools-from-a-windows-command-line)：打开 PowerShell，通过输入以下内容使用 Linux `C:\temp>` 命令显示 `ls -la` 的目录内容：`wsl ls -la`
    
- [混合 Linux 和 Windows 命令](https://learn.microsoft.com/zh-cn/windows/wsl/filesystems#mixing-linux-and-windows-commands)：在此示例中，使用 Linux 命令 `ls -la` 列出目录中的文件，然后使用 PowerShell 命令 `findstr` 筛选包含“git”的单词的结果：`wsl ls -la | findstr "git"`。 这还可以通过混合使用 Windows `dir` 命令和 Linux `grep` 命令来实现：`dir | wsl grep git`。
    
- [直接从 WSL 命令行运行 Windows 工具](https://learn.microsoft.com/zh-cn/windows/wsl/filesystems#run-windows-tools-from-linux)：`<tool-name>.exe`。例如，若要打开 .bashrc 文件（启动 Linux 命令行时运行的 shell 脚本），请输入：`notepad.exe .bashrc`
    
- [使用 Linux Grep 工具运行 Windows ipconfig.exe 工具](https://learn.microsoft.com/zh-cn/windows/wsl/filesystems#run-windows-tools-from-linux)：从 Bash 输入命令 `ipconfig.exe | grep IPv4 | cut -d: -f2` 或从 PowerShell 输入 `ipconfig.exe | wsl grep IPv4 | wsl cut -d: -f2`。此示例演示了 Windows 文件系统上的 ipconfig 工具，该工具先是用于显示当前 TCP/IP 网络配置值，然后通过 Linux 工具 grep 被筛选为仅显示 IPv4 结果。

## 装载外部驱动器或 USB 设备

按照此分步指南[开始在 WSL 2 中装载 Linux 磁盘](https://learn.microsoft.com/zh-cn/windows/wsl/wsl2-mount-disk)。

![wsl mount command screenshot](https://learn.microsoft.com/zh-cn/windows/wsl/media/wslmountsimple.png)wsl 装载命令屏幕截图
## 运行 Linux GUI 应用

按照本教程了解如何在 WSL 上设置和运行 Linux GUI 应用。
## 其他资源

- [设置开发环境](https://learn.microsoft.com/zh-cn/windows/dev-environment/)：了解有关为您首选的语言或框架（如 React、Python、NodeJS、Vue 等）设置开发环境的详细信息。
- [疑难解答](https://learn.microsoft.com/zh-cn/windows/wsl/troubleshooting)：查找常见问题、在何处报告错误、在何处请求新功能以及如何参与文档编撰工作。
- [常见问题解答](https://learn.microsoft.com/zh-cn/windows/wsl/faq)：查找常见问题列表。
- [发行说明](https://learn.microsoft.com/zh-cn/windows/wsl/release-notes)：查看 WSL 发行说明，了解过去版本更新的历史记录。 还可以查找 [WSL Linux 内核的发行说明](https://learn.microsoft.com/zh-cn/windows/wsl/kernel-release-notes)。