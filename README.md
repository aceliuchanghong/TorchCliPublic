# TorchCliPublic
执行的命令记录(数据文件别放在这儿)

### create a test env

```shell
pip freeze > requirements.txt
conda create -n TorchCliLog python=3.10
conda activate TorchCliLog
pip install -r requirements.txt
watch -n 1 nvidia-smi
```

### Structure
```
TorchCliPublic/
|
├── README.md
├── requirements.txt
├── 01-微调/
├── 02-推理/
└── util/
    ├── remove_comments.py
    └── structure.py
```