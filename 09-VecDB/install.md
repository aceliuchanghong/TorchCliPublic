### release

- https://github.com/milvus-io/milvus/releases/

```shell
cd /mnt/data/llch
wget https://github.com/milvus-io/milvus/releases/download/v2.4.4/milvus-standalone-docker-compose.yml -O docker-compose.yml
sudo docker compose up -d

# Check Milvus
sudo docker compose ps
# Stop Milvus
sudo docker compose down
# Delete service data
sudo rm -rf volumes

然后安装 Milvus 可视化工具 Attu
```

如果是gpu版本,需要指定一下运行的节点

```text
wget https://github.com/milvus-io/milvus/releases/download/v2.4.4/milvus-standalone-docker-compose-gpu.yml -O docker-compose-gpu.yml
sudo docker compose -f docker-compose-gpu.yml up -d
sudo docker compose -f docker-compose-gpu.yml down
  deploy:
    resources:
      reservations:
        devices:
          - driver: nvidia
            capabilities: ["gpu"]
            device_ids: ['0', '1']
```
