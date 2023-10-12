# StyleHEAT

## StyleHEAT

Propose a unified framework based on a pre-trained Style-GAN for one-shot talking face generation,which use audio or video driving a source image.

**what’s new:** 

Fei Yin from Tsinghua University and researchers from Tencent AI Lab have released a new generation pipeline named StyleHEAT to synthesis diverse and stylized talking-face videos

**key insights:** 

Previous work was unable to generate high-resolution speaking videos due to dataset, efficiency, and other limitations. To overcome the low quality of video resolution,the author verified the spatial characteristics of sytleGAN and added it to the generation framework to achieve high-resolution face speaking video generation, and can edit it by attributes.

**How it works:** 

The authors designed Video-Driven , Autdio-driven Motion Generator and Feature Calibration to achieve the unified framework.

- First it obtain the style codes and feature maps of the source image by the encoder of GAN inversion.
- Second the video or audio along with the source image are used to predict motion fields by the corresponding **motion generator**. The motion generator output the desired flow fields for feature warping
    - Driving-Video Motion Generator use 3DMM parameters as  the motion representation,and the network is based on U-Net
    - Driving-Audio Motion Generator use the Mel-Spectrogram,use an MLP to squeeze the temporal dimension. The network is the via AdaIN
- Then,the selected feature map is warped by the motion fields, followed by the **calibration network** for rectifying feature distortions.
- The refined feature map is then fed into the StyleGAN for the final face generation.

![Untitled](Untitled.png)

**Results:** 

Authors train the two motion generators on the VoxCeleb dataset,while joint training the whole framework on the HDTF dataset.This model output is a 1024×1024 image generated by the pre-trained styleGAN . Authors evaluated the generation picture with the other work,containing reappearance of the same character and different characters.Compared with other methods qualitatively and quantitatively, this method generates images that are more natural and have higher resolution. In terms of lip sync, more details and higher resolution than wav2lip.

**Why it matters:** 

This work proposes a unified framework based on a pre-trained Style-GAN for one-shot high-quality talking face generation.Such insights provide us with a new method and idea to improve the generation resolution.

**We’re thinking:** 

We can achieve the last step of generating video through GAN inversion-styleGAN inference, replacing the last step FaceRender in sadtalker