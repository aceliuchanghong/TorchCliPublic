参数解释

```text
audio_path 文件地址

initial_prompt 初始提示词

mode 文本生成格式(normal:纯文本 timeline:带时间线文本 subtitle:字幕格式)
```

### faster-whisper模型

示例程序

```python
import requests


def test_media_endpoint():
    url = "http://112.48.199.63:9898/media"
    data = {
        "audio_path": "/mnt/data/llch/media_path/00.mp4.mp3",
        "initial_prompt": '支持小岛国迈向更具韧性的持久繁荣',
        "mode": 'timeline',
    }
    response = requests.post(url, params=data)
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error:", response, response.status_code)


if __name__ == "__main__":
    test_media_endpoint()
```

### funasr模型

示例程序

```python
import requests
import time


def test_media_endpoint():
    url = "http://112.48.199.197:8083/video"
    path1 = r'C:\Users\liuch\Videos\test1.mp4'
    path2 = r'C:\Users\liuch\Videos\meeting_01.mp4'
    try:
        files = [('files', ('test_video.mp4', open(path1, 'rb'), 'video/mp4'))]
        data = {
            'initial_prompt': '会议',
            'mode': 'timeline'
        }
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            for i in response.json()['information']:
                print(i)
        else:
            print("Error:", response.text, response.status_code)
    except FileNotFoundError:
        print(f"Error: The file {path1} does not exist.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    start = time.time()
    test_media_endpoint()
    end = time.time()
    print('\n识别时间:', end - start)
```
