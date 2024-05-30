###################################
# Sample a speaker from Gaussian.
import torch

std, mean = torch.load('/mnt/data/llch/chatTTS_model/asset/spk_stat.pt').chunk(2)
rand_spk = torch.randn(768) * std + mean

params_infer_code = {
    'spk_emb': rand_spk,  # add sampled speaker
    'temperature': .3,  # using custom temperature
    'top_P': 0.7,  # top P decode
    'top_K': 20,  # top K decode
}

###################################
# For sentence level manual control.

# use oral_(0-9), laugh_(0-2), break_(0-7)
# to generate special token in text to synthesize.
params_refine_text = {
    'prompt': '[oral_2][laugh_0][break_6]'
}

wav = chat.infer(
    "我们过了江，进了车站。我买票，他忙着照看行李。行李太多了，得向脚夫行些小费才可过去。他便又忙着和他们讲价钱。我那时真是聪明过分，总觉他说话不大漂亮，非自己插嘴不可，但他终于讲定了价钱；就送我上车。他给我拣定了靠车门的一张椅子；我将他给我做的紫毛大衣铺好座位。他嘱我路上小心，夜里要警醒些，不要受凉。又嘱托茶房好好照应我。我心里暗笑他的迂；他们只认得钱，托他们只是白托！而且我这样大年纪的人，难道还不能料理自己么？我现在想想，我那时真是太聪明了。",
    params_refine_text=params_refine_text, params_infer_code=params_infer_code)

###################################
# For word level manual control.
text = 'What is [uv_break]your favorite english food?[laugh][lbreak]'
wav = chat.infer(text, skip_refine_text=True, params_infer_code=params_infer_code)
