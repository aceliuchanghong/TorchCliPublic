### reference

```
https://github.com/ollama/ollama/blob/main/docs/api.md
```

### usage

流式生成

```shell
curl http://112.48.199.70:11434/api/generate -d '{
  "model": "qwen:14b-gguf",
  "prompt": "Why is the sky blue?"
}'
```

普通生成

```shell
curl http://112.48.199.70:11434/api/generate -d '{
  "model": "qwen:14b-gguf",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
```

python1

```python
from langchain_openai import ChatOpenAI

baseURL = 'http://112.48.199.70:11434/v1/'
apiKey = 'qwen:14b-gguf'
llm = ChatOpenAI(
    base_url=baseURL,
    api_key=apiKey,
    model="qwen:14b-gguf"
)
print(llm.invoke("你好").content)
```

python2

```python
from langchain_community.llms import Ollama

ollama = Ollama(
    base_url='http://112.48.199.70:11434',
    model="qwen:14b-gguf"
)
print(ollama.invoke("why is the sky blue"))
```
