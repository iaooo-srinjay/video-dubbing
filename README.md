
## Environment
```
git clone https://github.com/vinthony/video-retalking.git
cd video-retalking
conda create -n video_retalking python=3.8
conda activate video_retalking

conda install ffmpeg

# Please follow the instructions from https://pytorch.org/get-started/previous-versions/
# This installation command only works on CUDA 11.1
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 -f https://download.pytorch.org/whl/torch_stable.html

pip install -r requirements.txt
```

## Quick Inference

#### Pretrained Models
Please download our [pre-trained models](https://drive.google.com/drive/folders/18rhjMpxK8LVVxf7PI6XwOidt8Vouv_H0?usp=share_link) and put them in `./checkpoints`.

<!-- We also provide some [example videos and audio](https://drive.google.com/drive/folders/14OwbNGDCAMPPdY-l_xO1axpUjkPxI9Dv?usp=share_link). Please put them in `./examples`. -->

#### Inference

```
python3 inference.py \
  --face examples/face/1.mp4 \
  --audio examples/audio/1.wav \
  --outfile results/1_1.mp4
```
This script includes data preprocessing steps. You can test any talking face videos without manual alignment. But it is worth noting that DNet cannot handle extreme poses.

You can also control the expression by adding the following parameters:

```--exp_img```: Pre-defined expression template. The default is "neutral". You can choose "smile" or an image path.

```--up_face```: You can choose "surprise" or "angry" to modify the expression of upper face with [GANimation](https://github.com/donydchen/ganimation_replicate).



## Citation

If you find our work useful in your research, please consider citing:

```
@misc{cheng2022videoretalking,
        title={VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild}, 
        author={Kun Cheng and Xiaodong Cun and Yong Zhang and Menghan Xia and Fei Yin and Mingrui Zhu and Xuan Wang and Jue Wang and Nannan Wang},
        year={2022},
        eprint={2211.14758},
        archivePrefix={arXiv},
        primaryClass={cs.CV}
  }
```

## Acknowledgement
Thanks to
[Wav2Lip](https://github.com/Rudrabha/Wav2Lip),
[PIRenderer](https://github.com/RenYurui/PIRender), 
[GFP-GAN](https://github.com/TencentARC/GFPGAN), 
[GPEN](https://github.com/yangxy/GPEN),
[ganimation_replicate](https://github.com/donydchen/ganimation_replicate),
[STIT](https://github.com/rotemtzaban/STIT)
for sharing their code.


## Related Work
- [StyleHEAT: One-Shot High-Resolution Editable Talking Face Generation via Pre-trained StyleGAN (ECCV 2022)](https://github.com/FeiiYin/StyleHEAT)
- [CodeTalker: Speech-Driven 3D Facial Animation with Discrete Motion Prior (CVPR 2023)](https://github.com/Doubiiu/CodeTalker)
- [SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation (CVPR 2023)](https://github.com/Winfredy/SadTalker)
- [DPE: Disentanglement of Pose and Expression for General Video Portrait Editing (CVPR 2023)](https://github.com/Carlyx/DPE)
- [3D GAN Inversion with Facial Symmetry Prior (CVPR 2023)](https://github.com/FeiiYin/SPI/)
- [T2M-GPT: Generating Human Motion from Textual Descriptions with Discrete Representations (CVPR 2023)](https://github.com/Mael-zys/T2M-GPT)

##  Disclaimer

This is not an official product of Tencent. 

```
1. Please carefully read and comply with the open-source license applicable to this code before using it. 
2. Please carefully read and comply with the intellectual property declaration applicable to this code before using it.
3. This open-source code runs completely offline and does not collect any personal information or other data. If you use this code to provide services to end-users and collect related data, please take necessary compliance measures according to applicable laws and regulations (such as publishing privacy policies, adopting necessary data security strategies, etc.). If the collected data involves personal information, user consent must be obtained (if applicable). Any legal liabilities arising from this are unrelated to Tencent.
4. Without Tencent's written permission, you are not authorized to use the names or logos legally owned by Tencent, such as "Tencent." Otherwise, you may be liable for your legal responsibilities.
5. This open-source code does not have the ability to directly provide services to end-users. If you need to use this code for further model training or demos, as part of your product to provide services to end-users, or for similar use, please comply with applicable laws and regulations for your product or service. Any legal liabilities arising from this are unrelated to Tencent.
6. It is prohibited to use this open-source code for activities that harm the legitimate rights and interests of others (including but not limited to fraud, deception, infringement of others' portrait rights, reputation rights, etc.), or other behaviors that violate applicable laws and regulations or go against social ethics and good customs (including providing incorrect or false information, spreading pornographic, terrorist, and violent information, etc.). Otherwise, you may be liable for your legal responsibilities.

```
## All Thanks To Our Contributors 

<a href="https://github.com/OpenTalker/video-retalking/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=OpenTalker/video-retalking" />
</a>
