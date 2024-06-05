### 开始

```shell
cd /mnt/data/llch
git clone https://github.com/aceliuchanghong/ChatTTS
```

### env

```shell
conda create -n chattts python=3.9
source activate chattts
cd ChatTTS
# 服务器换源(pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple)
pip install -r requirements.txt
# pip install -r requirements.txt --proxy=127.0.0.1:10809
watch -n 1 nvidia-smi
```

### 模型下载

```shell
cd ..
git clone https://www.modelscope.cn/pzc163/chatTTS.git
```

### webui

```shell
python webui.py --server_port=8082 --local_path /mnt/data/llch/chatTTS
nohup python webui.py --server_port=8082 --local_path /mnt/data/llch/chatTTS > unicore.log &
```
