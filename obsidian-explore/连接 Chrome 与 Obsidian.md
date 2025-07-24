在 google chrome store 搜索 obsidian web 添加其到插件中心，启用
# Obsidian Web

Obsidian Web 是第三方扩展，与 Obsidian 官方无任何关系，这个名字比较容易引起误解。
## 前提条件

使用 Obsidian Web 需要在 Obsidian 上先安装一个插件：[Local REST API](obsidian://show-plugin?id=obsidian-local-rest-api)（点击可直接打开 Obsidian 安装）。这是一个为 Obsidian 提供本地 API 的插件。

然后在 Chrome 系浏览器上安装扩展（[Chrome 商店](https://chrome.google.com/webstore/detail/obsidian-web/edoacekkjanmingkbkgjndndibhkegad/related)），输入由 Lcoal REST API 生成的 API 地址和 Key 就完成了链接。

将 API 输入如下页面的 vaults 中：

![[obsidian web setting.png]]

之后在浏览网页时，只需要按下 Obsidian Web 按钮，就能将当前网页发送至 Obsidian，支持选中文字后发送。另外还能创建自定义模板，支持追加笔记。以及显示当前网页是否有已记录笔记等功能。

# 具体用法

[# Introduction to Obsidian Web Clipper](https://help.obsidian.md/web-clipper)

# Local REST API for Obsidian

See our interactive docs: [https://coddingtonbear.github.io/obsidian-local-rest-api/](https://coddingtonbear.github.io/obsidian-local-rest-api/)

Have you ever needed to automate interacting with your notes? This plugin gives Obsidian a REST API you can interact with your notes from other tools so you can automate what you need to automate.

This plugin provides a secure HTTPS interface gated behind api key authentication that allows you to:

- Read, create, update or delete existing notes. There's even a `PATCH` HTTP method for inserting content into a particular section of a note.
- List notes stored in your vault.
- Create and fetch periodic notes.
- Execute commands and list what commands are available.

This is particularly useful if you need to interact with Obsidian from a browser extension like [Obsidian Web](https://chrome.google.com/webstore/detail/obsidian-web/edoacekkjanmingkbkgjndndibhkegad).