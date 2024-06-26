### stop it

systemctl stop ollama.service

### disable it if you want

systemctl disable ollama.service

### confirm its status

systemctl status ollama.service
systemctl start ollama.service

### modelfile

ollama create Qwen2-72B-Instruct -f Modelfile
ollama run Qwen2-72B-Instruct 

### env

vi /etc/systemd/system/ollama.service

Environment="OLLAMA_MODELS=/mnt/data/ollama/models"
Environment="OLLAMA_HOST=0.0.0.0"

```text
~# cat /etc/systemd/system/ollama.service
[Unit]
Description=Ollama Service
After=network-online.target

[Service]
ExecStart=/usr/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="OLLAMA_HOST=0.0.0.0:11434"

[Install]
WantedBy=default.target
```
