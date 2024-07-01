
## Environment
```
git clone https://github.com/vinthony/video-retalking.git
cd video-retalking
conda create -n video_retalking python=3.8
conda activate video_retalking

conda install ffmpeg

# Please follow the instructions from https://pytorch.org/get-started/previous-versions/
# This installation command only works on CUDA 11.1
pip install torch==2.0.1+cu117 torchvision==0.15.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html

pip install -r requirements.txt
```

## Quick Inference

#### Pretrained Models
Please download the [pre-trained models](https://drive.google.com/drive/folders/18rhjMpxK8LVVxf7PI6XwOidt8Vouv_H0?usp=share_link) and put them in `./checkpoints`.

<!-- We also provide some [example videos and audio](https://drive.google.com/drive/folders/14OwbNGDCAMPPdY-l_xO1axpUjkPxI9Dv?usp=share_link). Please put them in `./examples`. -->

#### Inference

```
python3 final_inference.py \
  --face ./examples/face/5.mp4 \
  --audio_save ./examples/saved.wav \
  --audio_translate_save ./examples/translated_saved.wav \
  --outfile ./results/subbed_translated.mp4
```

### Limitations
- Fails with multiple faces and multiple voices in the audio .
- Translation model is unreliable, sometimes the translation is wrong and sometimes the translation does not occur .
- Unable to handle pauses in long sentences .
- Translation fails for videos > 15s .   


## Citation

If you find this work useful in your research, please consider citing:

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

