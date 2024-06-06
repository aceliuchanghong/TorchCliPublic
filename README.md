## TorchCliPublic
大模型操作记录

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
│   ├── chatTTS.ipynb
│   ├── chatTTS_server_log.md
│   └── media2text_api.md
├── 04-Ollama/
│   ├── Modelfile.txt
│   ├── llm_api.md
│   └── ollama_readme.md
├── 05-Comfyui/
│   ├── comfyui_colab.ipynb
│   └── start.md
├── 06-MaxKB/
│   └── MaxKB_reademe.md
└── util/
    ├── remove_comments.py
    └── structure.py
```
