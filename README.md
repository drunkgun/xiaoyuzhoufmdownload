# xiaoyuzhoufmdownload
下载小宇宙播客中的音频

## 安装依赖

1. 创建虚拟环境：
```bash
python3 -m venv venv
```

2. 激活虚拟环境：
```bash
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate  # Windows
```

3. 安装依赖包：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 在小宇宙播客音频界面中，点击分享按钮，然后复制链接地址

2. 修改 `xiaoyuzhoufmdownload.py` 文件中的 `url` 变量，将链接地址粘贴进去

3. 运行程序：
```bash
source venv/bin/activate  # 如果还没激活虚拟环境
python xiaoyuzhoufmdownload.py
```

4. 音频文件将下载到 `fmfiles` 目录中

## 注意事项

- 确保网络连接正常
- 程序会自动创建 `fmfiles` 目录
- 下载的音频文件将以播客标题命名

