import torch
import torchaudio
from seamless_communication.inference import Translator

#init translator
# translator = Translator("seamlessM4T_v2_large", "vocoder_v2", torch.device("cuda:0"), torch.float16)
translator = Translator("seamlessM4T_v2_large", "vocoder_v2", device=torch.device("cuda:0"), dtype=torch.float16,)
assert translator is not None
print(translator)
text_output, speech_output = translator.predict( input = "/mnt/facedet-vol/srinjay/video-retalking/examples/face/kim_7s_raw.mp4", task_str="S2ST",tgt_lang = "hin")
torchaudio.save("/mnt/facedet-vol/srinjay/translate/output1.wav",speech_output.audio_wavs[0][0].to(torch.float32).cpu(),sample_rate=speech_output.sample_rate)