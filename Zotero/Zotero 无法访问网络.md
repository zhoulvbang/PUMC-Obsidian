#网络 #问题 
#  "Error connecting to server. Check your Internet connection."

当 Zotero 无法访问网络时，通常是由于计算机上的代理设置或安全软件造成的。

默认情况下，Zotero 会使用系统代理设置中手动输入的代理服务器或代理自动配置 (PAC) URL。即使在系统设置中启用了 Web 代理自动发现 (WPAD) 或 macOS 上的“自动代理发现”，它也不会自动使用。

如果您不使用代理连接互联网，则应在系统代理设置中禁用所有代理。如果您确实需要通过代理连接，则应验证系统设置是否正确。请注意，您计算机上的其他软件可能未使用系统代理设置，因此当 Zotero 无法连接互联网时，其他程序可能仍能连接。

如果您需要将 Zotero 代理设置配置得与系统设置不同，您可以从 Zotero 首选项的高级窗格访问配置编辑器，应用[与 Firefox](http://kb.mozillazine.org/Network.proxy.type "http://kb.mozillazine.org/Network.proxy.type")（Zotero 基于 Firefox）中相同的设置，然后重新启动 Zotero，但建议使用默认设置（network.proxy.type = 5，使用系统代理设置）。

如果使用 PAC 文件（自动或 network.proxy.type = 2），并且您的代理需要 HTTP 身份验证，请确保 PAC 文件处理了其中的大部分或所有主机`extensions.zotero.proxyAuthenticationURLs`。Zotero 会在每次启动时测试随机子集，以便在必要时触发代理身份验证提示。

要使用 WPAD，您必须将 network.proxy.type 设置为 4。

如果更改代理设置没有帮助，请尝试暂时禁用系统上的任何安全/防火墙软件。

某些连接错误也可能是由网络上的 [证书问题引起的。](https://www.zotero.org/support/kb/ssl_certificate_error "kb：ssl_certificate_error")

另请参阅[Zotero 和防火墙](https://www.zotero.org/support/kb/zotero_and_firewalls "kb:zotero_and_firewalls")。