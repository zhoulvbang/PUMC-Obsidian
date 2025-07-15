# 如何使用 WSL 在 Windows 上安装 Linux

- 2025/06/11

开发人员可以在 Windows 计算机上同时访问 Windows 和 Linux 的强大功能。 借助适用于 Linux 的 Windows 子系统（WSL），开发人员可以安装 Linux 分发版（如 Ubuntu、OpenSUSE、Kali、Debian、Arch Linux 等），并在 Windows 上直接使用 Linux 应用程序、实用工具和 Bash 命令行工具（未经修改），无需传统虚拟机或双包设置的开销。
## 先决条件

必须运行 Windows 10 版本 2004 及更高版本（内部版本 19041 及更高版本）或 Windows 11 才能使用以下命令。 如果使用的是早期版本，请参阅 [手动安装页](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual)。
## 安装 WSL 命令

现在，可以使用单个命令安装运行 WSL 所需的所有内容。 右键单击并选择“以管理员身份运行”，在 **管理员** 模式下打开 PowerShell 或 Windows 命令提示符，输入 wsl --install 命令，然后重新启动计算机。

```
wsl --install
```

此命令将启用运行 WSL 并安装 Linux 的 Ubuntu 分发所需的功能。 （[可以更改此默认分布](https://learn.microsoft.com/zh-cn/windows/wsl/basic-commands#install)）。

如果运行的是较旧的版本，或者只是不想使用安装命令，并且想要分步说明，请参阅 **[适用于旧版本的 WSL 手动安装步骤](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual)**。

首次启动新安装的 Linux 分发版时，控制台窗口将打开，系统会要求你等待文件取消压缩并存储在计算机上。 所有未来的发射应该需要不到一秒钟的时间。

 备注

仅当 WSL 根本不安装时，上述命令才有效。 如果运行 `wsl --install` 并查看 WSL 帮助文本，请尝试运行 `wsl --list --online` 以查看可用发行版列表并运行 `wsl --install -d <DistroName>` 以安装发行版。 若要卸载 [WSL，请参阅卸载旧版 WSL](https://learn.microsoft.com/zh-cn/windows/wsl/troubleshooting#uninstall-legacy-version-of-wsl) 或 [注销或卸载 Linux 分发版](https://learn.microsoft.com/zh-cn/windows/wsl/basic-commands#unregister-or-uninstall-a-linux-distribution)。

## 如果安装进程停滞

我在安装过程时，发现进程停滞，询问AI后，进行一些修复尝试，如下是记录：
![[WSL-install.png]]

更新 `wsl --update --web-download`

```bash
PS C:\WINDOWS\system32> wsl --update --web-download

Copyright (c) Microsoft Corporation. All rights reserved.

Usage: wsl.exe [Argument]

Arguments:

    --install <Options>
        Install Windows Subsystem for Linux features. If no options are specified,
        the recommended features will be installed along with the default distribution.

        To view the default distribution as well as a list of other valid distributions,
        use 'wsl --list --online'.

        Options:
            --distribution, -d [Argument]
                Specifies the distribution to be downloaded and installed by name.

                Arguments:
                    A valid distribution name (not case sensitive).

                Examples:
                    wsl --install -d Ubuntu
                    wsl --install --distribution Debian

            --inbox
                Install the optional Windows feature instead of the version available via the Microsoft Store.

            --no-distribution
                Do not install a distribution (cannot be used with --distribution).

            --no-launch, -n
                Do not launch the distribution after install.

            --web-download
                Download the most recent version of WSL from the internet instead of the Microsoft Store.

    --list, -l [Options]
        Lists distributions.

        Options:
            --online, -o
                Displays a list of available distributions for install with 'wsl --install'.

    --status
        Show the status of Windows Subsystem for Linux.

    --help
        Display usage information.
```
## 更改安装的默认 Linux 分发版

默认情况下，已安装的 Linux 分发版将为 Ubuntu。 可以通过使用`-d`标志来更改这一点。

- 若要更改安装的分发版，请输入： `wsl --install -d <Distribution Name>` 将 `<Distribution Name>` 替换为您想要安装的分发版名称。
- 若要查看可通过在线商店下载的可用 Linux 分发版的列表，请输入： `wsl --list --online` 或 `wsl -l -o`。
- 若要在初始安装后安装其他 Linux 分发版，也可以使用以下命令： `wsl --install -d <Distribution Name>`

```bash
PS C:\WINDOWS\system32> wsl --list --online
The following is a list of valid distributions that can be installed.
The default distribution is denoted by '*'.
Install using 'wsl --install -d <Distro>'.

  NAME                            FRIENDLY NAME
* Ubuntu                          Ubuntu
  Debian                          Debian GNU/Linux
  kali-linux                      Kali Linux Rolling
  Ubuntu-18.04                    Ubuntu 18.04 LTS
  Ubuntu-20.04                    Ubuntu 20.04 LTS
  Ubuntu-22.04                    Ubuntu 22.04 LTS
  Ubuntu-24.04                    Ubuntu 24.04 LTS
  OracleLinux_7_9                 Oracle Linux 7.9
  OracleLinux_8_10                Oracle Linux 8.10
  OracleLinux_9_5                 Oracle Linux 9.5
  openSUSE-Leap-15.6              openSUSE Leap 15.6
  SUSE-Linux-Enterprise-15-SP6    SUSE Linux Enterprise 15 SP6
  openSUSE-Tumbleweed             openSUSE Tumbleweed
```

建议使用 ubuntu 22.04：[大模型开发ubuntu 20.04还是22.04好？]( https://zhuanlan.zhihu.com/p/1888945653234791235)

`wsl --install -d Ubuntu-22.04`

![[install-Ubuntu-22.04.png]]

![[install-ubuntu.png]]
### 提示

如果要从 Linux/Bash 命令行（而不是 PowerShell 或命令提示符）安装其他分发版，则必须在命令中使用 .exe：或列出可用分发版： `wsl.exe --install -d <Distribution Name>``wsl.exe -l -o`

如果在安装过程中遇到问题，请查看故障排除指南 [](https://learn.microsoft.com/zh-cn/windows/wsl/troubleshooting#installation-issues)安装部分。

若要安装未列为可用的 Linux 分发版，可以使用 TAR 文件 [导入任何 Linux 分发](https://learn.microsoft.com/zh-cn/windows/wsl/use-custom-distro) 版。 或者在某些情况下，与 [Arch Linux 一样](https://wsldl-pg.github.io/ArchW-docs/How-to-Setup/)，可以使用文件进行安装 `.appx` 。 还可以创建自己的 [自定义 Linux 分发版](https://learn.microsoft.com/zh-cn/windows/wsl/build-custom-distro) ，以便与 WSL 一起使用。

## 设置 Linux 用户信息

安装 WSL 后，需要为新安装的 Linux 分发版创建用户帐户和密码。 请参阅 [[设置 WSL 开发环境]](https://learn.microsoft.com/zh-cn/windows/wsl/setup/environment#set-up-your-linux-username-and-password) ，了解详细信息。

![[Linux username.png]]
## 配置和最佳实践

建议遵循我们的 [设置 WSL 开发环境的最佳实践](https://learn.microsoft.com/zh-cn/windows/wsl/setup/environment) 指南，通过逐步演示来了解如何为已安装的 Linux 发行版设置用户名和密码，使用基本 WSL 命令，安装和自定义 Windows 终端，为 Git 版本控制、代码编辑和调试使用 VS Code 远程服务器，好的文件存储实践，设置数据库，装载外部驱动器，设置 GPU 加速等。

## 检查你正在运行的 WSL 的版本

可以通过在 PowerShell 或 Windows 命令提示符中输入命令 `wsl -l -v` 来列出已安装的 Linux 发行版，并检查每个发行版设置的 WSL 版本。

若要在安装新的 Linux 分发版时将默认版本设置为 WSL 1 或 WSL 2，请使用以下命令 `wsl --set-default-version <Version#>`，替换为 `<Version#>` 1 或 2。

要设置默认的 Linux 发行版以用于 `wsl` 命令，请输入：在 `wsl -s <DistributionName>` 或 `wsl --set-default <DistributionName>` 中将 `<DistributionName>` 替换为你想使用的 Linux 发行版名称。 例如，在 PowerShell/CMD 中，输入： `wsl -s Debian` 将默认分发设置为 Debian。 现在，从 Powershell 运行 `wsl npm init` 将在 Debian 中运行 `npm init` 命令。

若要在不更改默认分发的情况下从 PowerShell 或 Windows 命令提示符内运行特定的 wsl 分发版，请使用以下命令： `wsl -d <DistributionName>`，替换为 `<DistributionName>` 要使用的分发的名称。

在 [WSL 基本命令](https://learn.microsoft.com/zh-cn/windows/wsl/basic-commands)指南中了解详细信息。

## 将版本从 WSL 1 升级到 WSL 2

默认情况下，使用 `wsl --install` 命令安装的新 Linux 安装将设置为 WSL 2。

该 `wsl --set-version` 命令可用于从 WSL 2 降级到 WSL 1，或将以前安装的 Linux 分发版从 WSL 1 降级到 WSL 2。

若要查看 Linux 分发版是否设置为 WSL 1 或 WSL 2，请使用以下命令： `wsl -l -v`

若要更改版本，请使用命令： `wsl --set-version <distro name> 2` 替换为 `<distro name>` 要更新的 Linux 分发版的名称。 例如， `wsl --set-version Ubuntu-20.04 2` 将 Ubuntu 20.04 分发版设置为使用 WSL 2。

如果在命令可用之前 `wsl --install` 手动安装了 WSL，则还可能需要启用 WSL 2 使用的 [虚拟机可选组件](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual#step-3---enable-virtual-machine-feature) ，并 [安装内核包](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package) （如果尚未这样做）。

若要了解更多信息，请参阅 [WSL 的命令参考](https://learn.microsoft.com/zh-cn/windows/wsl/basic-commands)以获取 WSL 命令列表，查看 [WSL 1 和 WSL 2 的比较](https://learn.microsoft.com/zh-cn/windows/wsl/compare-versions)以获得关于您工作场景适用版本的指导，或参考 [设置 WSL 开发环境的最佳实践](https://learn.microsoft.com/zh-cn/windows/wsl/setup/environment)以获取关于设置高效开发工作流程的一般指导。

## 使用 WSL 运行多个 Linux 分发版的方法

WSL 支持运行您想安装的许多不同的 Linux 发行版。 这包括从 [Microsoft 应用商店](https://aka.ms/wslstore)中选择分发版、 [导入自定义分发版](https://learn.microsoft.com/zh-cn/windows/wsl/use-custom-distro)或 [生成自己的自定义分发版](https://learn.microsoft.com/zh-cn/windows/wsl/build-custom-distro)。

安装 Linux 分发版后，可通过多种方式运行：

- [安装 Windows 终端](https://learn.microsoft.com/zh-cn/windows/terminal/get-started)_**（推荐）**_。使用 Windows 终端可以支持多个命令行，并允许您在多个选项卡或窗口窗格中打开它们，并能在多个 Linux 发行版或其他命令行（如 PowerShell、命令提示符、Azure CLI 等）之间快速切换。 可以使用独特的配色方案、字体样式、大小、背景图像和自定义键盘快捷方式完全自定义终端。 [了解详细信息](https://learn.microsoft.com/zh-cn/windows/terminal)。
- 可以通过访问 Windows 开始菜单并键入已安装的分发版的名称来直接打开 Linux 分发版。 例如：“Ubuntu”。 这将在一个独立的控制台窗口中打开 Ubuntu。
- 在 Windows 命令提示符或 PowerShell 中，可以输入已安装的分发版的名称。 例如：`ubuntu`
- 在 Windows 命令提示符或 PowerShell 中，可以通过输入： `wsl.exe`在当前命令行中打开默认 Linux 分发版。
- 在 Windows 命令提示符或 PowerShell 中，可以通过输入：`wsl [command]`，在当前命令行中使用默认 Linux 分发版，而无需输入新发行版。 你可以用 `[command]` 替换为 WSL 命令，例如：`wsl -l -v` 列出已安装的发行版，或 `wsl pwd` 查看当前目录路径在 WSL 中装载的位置。 在 PowerShell 中，该命令 `get-date` 将提供 Windows 文件系统中的日期，并提供 `wsl date` Linux 文件系统中的日期。

选择的方法应取决于你正在做的事情。 如果已在 Windows 提示符或 PowerShell 窗口中打开 WSL 命令行并想要退出，请输入以下命令： `exit`
## 想要试用最新的 WSL 预览功能？

通过加入 [Windows 预览体验计划](https://insider.windows.com/getting-started)来试用 WSL 的最新功能或更新。 加入 Windows 预览体验成员后，可以选择希望从 Windows 设置菜单中接收预览版的频道，以自动接收与该版本关联的任何 WSL 更新或预览功能。 可以选择：

- 开发通道：最新的更新，但稳定性较低。
- Beta 通道：非常适合早期采用者，比开发通道更可靠。
- 发布预览频道：在 Windows 下一个版本正式提供给公众之前，预览修补程序和主要功能。

如果不想将 Windows 安装切换到预览频道，仍可以通过发出命令来测试 WSL 的最新预览。 `wsl --update --pre-release` 有关详细信息，请查看 [GitHub 上的 WSL 发布页](https://github.com/Microsoft/WSL/releases)。