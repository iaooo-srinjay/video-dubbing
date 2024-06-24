
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

