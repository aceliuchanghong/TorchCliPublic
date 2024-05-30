# LLama_Factory 单机多卡微调模型

## 1. 数据集

数据集存放在` /mnt/data/LLaMA-Factory/LLaMA-Factory/data `目录下，具体文件为`torch.json`

增加新数据集时需要编辑`dataset_info.json`文件，新增以下内容

```json
"torch01_zh": {
"file_name": "torch.json",
"file_sha1": ""
},
```

## 2. 模型

模型可以下载到任意文件夹，目前路径`/mnt/data/`下有`chatglm3-6b  chatglm3-6b-base  Qwen1.5-14B-Chat  Qwen-7B-Chat`
,使用时带上绝对路径即可，如`/mnt/data/Qwen-7B-Chat`

## 3. 训练

首先进入` /mnt/data/LLaMA-Factory/LLaMA-Factory/ `目录下，激活conda环境

```
source activate llama_factory
```

服务器是单机多卡，训练命令如下（执行前删除注释）

```
CUDA_VISIBLE_DEVICES=0,1,2,3 accelerate launch     
    --config_file examples/accelerate/single_config.yaml src/train.py     
    --stage sft     
    --do_train     
    --model_name_or_path /mnt/data/Qwen-7B-Chat  #模型路径   
    --dataset torch01_zh     #数据集
    --dataset_dir data      #数据集路径
    --template default     
    --finetuning_type lora    #训练类型
    --lora_target all     
    --output_dir saves/Qwen-7B-Chat/lora/train_2024-05-22-17-00-00  #保存路径   
    --overwrite_cache     
    --overwrite_output_dir     
    --cutoff_len 1024     
    --preprocessing_num_workers 16     
    --per_device_train_batch_size 1    #每个设备训练的批处理大小 
    --per_device_eval_batch_size 1     
    --gradient_accumulation_steps 2     
    --lr_scheduler_type cosine     
    --logging_steps 10     #打印步数
    --warmup_steps 20     
    --save_steps 100     #保存步数
    --eval_steps 100     
    --evaluation_strategy steps     
    --load_best_model_at_end     
    --learning_rate 0.00001  #学习率   
    --num_train_epochs 3.0   #训练轮数
    --max_samples 10000     #最大样本数
    --val_size 0.1     
    --ddp_timeout 180000000     
    --plot_loss     
    --fp16  #计算类型
```

训练完毕后，可进入saves目录下查看训练结果，loss图等，如`saves/Qwen-7B-Chat/lora/train_2024-05-22-17-00-00`，或进入webui验证训练结果

## 4.webui

进入conda环境后，在` /mnt/data/LLaMA-Factory/LLaMA-Factory/ `目录下，使用以下命令开启webui（训练时需关闭webui）

```
CUDA_VISIBLE_DEVICES=0,1,2,3 nohup python src/webui.py > /mnt/data/Log/log.log &
```

启动后访问本机的7860端口即可访问，可用于模型加载，验证微调效果，生成训练命令等。