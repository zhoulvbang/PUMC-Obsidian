1. `wget`:从网络下载文件
- `wget hllp//example.com/file.zip`:下载指定网址的 `file.zip` 文件到当前目录
- `wget -O newname.zip http://example.com/file.zip` :将下载的文件保存为 `newname.zip`
2. `Curl` ：传输数据的工具，常用于下载文件或与 API交互
- `curl -o file.zip hitp://example.com/file.zip`：将文件下载并保存为 file.zip
- `curl-X POST -d "param1=value1&param2=value2" http://example.com/api` ：向指定 API 发送 POST 请求并传递参数