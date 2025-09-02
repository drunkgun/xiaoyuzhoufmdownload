import requests
from bs4 import BeautifulSoup
import os

# 1. 设置要下载的网址
url = "https://www.xiaoyuzhoufm.com/episode/68923a1a638b0158792063c4"

# 2. 获取网页源代码并解析
try:
    response = requests.get(url)
    response.raise_for_status()  # 检查请求是否成功
    soup = BeautifulSoup(response.content, 'html.parser')
except requests.RequestException as e:
    print(f"获取网页失败: {e}")
    exit(1)

# 3. 获取音频文件的标题和下载地址
title_tag = soup.find('meta', {'property': 'og:title'})
audio_tag = soup.find('meta', {'property': 'og:audio'})

if not title_tag or not audio_tag:
    print("无法找到音频文件的标题或下载地址")
    exit(1)

title = title_tag['content']
audio_url = audio_tag['content']

# 4. 创建保存目录
save_dir = "fmfiles"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 5. 下载音频文件并保存到本地
try:
    response = requests.get(audio_url)
    response.raise_for_status()
    
    # 修复文件路径，使用正斜杠
    file_path = os.path.join(save_dir, f"{title}.mp3")
    
    with open(file_path, "wb") as f:
        f.write(response.content)
    
    print(f"音频文件 {title}.mp3 下载完成！")
    print(f"保存位置: {file_path}")
    
except requests.RequestException as e:
    print(f"下载音频文件失败: {e}")
except IOError as e:
    print(f"保存文件失败: {e}")
