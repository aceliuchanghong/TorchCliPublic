import ChatTTS

chat = ChatTTS.Chat()
chat.load_models('/mnt/data/llch/chatTTS_model/asset/GPT.pt')
inputs_en = """
chat T T S is a text to speech model designed for dialogue applications. 
[uv_break]it supports mixed language input [uv_break]and offers multi speaker 
capabilities with precise control over prosodic elements [laugh]like like 
[uv_break]laughter[laugh], [uv_break]pauses, [uv_break]and intonation. 
[uv_break]it delivers natural and expressive speech,[uv_break]so please
[uv_break] use the project responsibly at your own risk.[uv_break]
""".replace('\n', '')  # English is still experimental.

inputs_cn = """
轻轻的我走了
[uv_break]正如我轻轻的来
我轻轻的招手
作别西天的云彩
那河畔的金柳
是夕阳中的新娘[laugh]
波光里的艳影
在我的心头荡漾
[uv_break]软泥上的青荇
油油的在水底招摇
在康河的柔波里
我甘心做一条水草
那榆荫下的一潭
不是清泉，是天上虹
揉碎在浮藻间
沉淀着彩虹似的梦[laugh]
""".replace('\n', '')  # English is still experimental.

params_refine_text = {
    'prompt': '[oral_2][laugh_0][break_4]'
}
audio_array_cn = chat.infer(inputs_cn, params_refine_text=params_refine_text)
audio_array_en = chat.infer(inputs_en, params_refine_text=params_refine_text)
