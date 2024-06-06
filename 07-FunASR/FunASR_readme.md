# FunASR部署文档
## 一、环境安装
### 1、安装miniconda3
略
### 2、安装虚拟环境
```
conda create -p /mnt/data/asr python=3.8
```
### 3、启动虚拟环境
```
conda activate /mnt/data/asr
```
或
```
source activate /mnt/data/asr
```
## 二、代码示例
```
from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
import os
from funasr import AutoModel

app = FastAPI()

# 提前加载模型
model = AutoModel(model='/mnt/data/speech_paraformer-large-vad-punc-spk_asr_nat-zh-cn',
                  vad_model='/mnt/data/speech_fsmn_vad_zh-cn-16k-common-pytorch',
                  punc_model='/mnt/data/punc_ct-transformer_cn-en-common-vocab471067-large',
                  spk_model="/mnt/data/speech_campplus_sv_zh-cn_16k-common")

@app.post("/video/")
async def process_video(files: List[UploadFile] = File(...)):
    for file in files:
        # 保存音视频文件
        file_path = os.path.join('/mnt/data/video', file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # 进行识别操作
        res = model.generate(input=file_path, batch_size_s=1000)
        
        # 将结果保存到文件
        result_file_path = os.path.join('/mnt/data/result', f"{os.path.splitext(file.filename)[0]}.txt")
        with open(result_file_path, 'w') as f:
            for item in res:
                # 如果结果是字典对象，则转换为字符串
                if isinstance(item, dict):
                    item = str(item)
                f.write(str(item) + '\n')

        # 删除音视频文件
        os.remove(file_path)

    return {"message": "Processing complete"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8083)
```
## 三、模型下载
共有四个模型,下载任意位置，代码中使用绝对路径

### 1、model(Paraformer分角色语音识别-中文-通用)：
```
git clone https://www.modelscope.cn/iic/speech_paraformer-large-vad-punc-spk_asr_nat-zh-cn.git
```
### 2、vad_model(FSMN语音端点检测-中文-通用-16k):
```
git clone https://www.modelscope.cn/iic/speech_fsmn_vad_zh-cn-16k-common-pytorch.git
```
### 3、punc_model(CT-Transformer标点-中英文-通用-large):
```
git clone https://www.modelscope.cn/iic/punc_ct-transformer_cn-en-common-vocab471067-large.git
```
### 4、spk_model(CAM++说话人确认-中文-通用-200k-Spkrs):
```
git clone https://www.modelscope.cn/iic/speech_campplus_sv_zh-cn_16k-common.git
```
## 四、依赖安装
首先进行代码运行，如
```
python test.py
```
启动后，依据报错信息进行依赖安装，如
```
pip install funasr
```
等
## 五、开放端口号
### 1、进入服务器后台管理平台进行开放端口号
### 2、打开linux内部端口号
如开放端口 9880：
```
iptables -A INPUT -p tcp --dport 9880 -j ACCEPT
```