# TorchCliPublic
执行的命令记录(数据文件别放在这儿)

### create a test env

```shell
pip freeze > requirements.txt
conda create -n TorchCliLog python=3.10
conda activate TorchCliLog
pip install -r requirements.txt
pip install -r requirements.txt --proxy=127.0.0.1:10809
watch -n 1 nvidia-smi
```

### Structure
```
TorchCliPublic/
|
├── README.md
├── requirements.txt
├── 01-LLM_FineTune/
│   └── 01-llama_factory_readme.md
├── 02-LLM_Inference/
├── 03-Voice_Stuff/
│   ├── download_file.md
│   ├── test_tts01.py
│   └── test_tts02.py
└── util/
    ├── remove_comments.py
    └── structure.py
```