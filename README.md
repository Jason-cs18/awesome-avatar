# awesome-avatar
This is a repository for organizing papers, codes and other resources related to the topic of Avatar (talking-face and talking-body). 

#### 🔆 This project is still on-going, pull requests are welcomed!!
If you have any suggestions (missing papers, new papers, key researchers or typos), please feel free to edit and pull a request.

#### TO DO LIST

- [x] Main paper list
- [x] Researchers list
- [x] Toolbox for avatar
- [x] Add paper link
- [ ] Add [paper notes](https://github.com/Jason-cs18/awesome-avatar/tree/main/notes)
- [x] Add codes if have
- [x] Add project page if have
- [x] Datasets and metrics
- [x] Related links

## Researchers and labs
1. [NVIDIA Research](https://www.nvidia.com/en-us/research/)
   - Neural rendering models for human generation: [vid2vid NeurIPS'18](https://tcwang0509.github.io/vid2vid/), [fs-vid2vid NeurIPS'19](https://nvlabs.github.io/few-shot-vid2vid/), [EG3D CVPR'22](https://github.com/NVlabs/eg3d);
   - Talking-face synthesis: [face-vid2vid CVPR'21](https://nvlabs.github.io/face-vid2vid/), [Implicit NeurIPS'22](https://research.nvidia.com/labs/dir/implicit_warping/), [SPACE ICCV'23](https://research.nvidia.com/labs/dir/space/), [One-shot
Neural Head Avatar arXiv'23](https://research.nvidia.com/labs/lpr/one-shot-avatar/);
   - Talking-body synthesis: [DreamPose ICCV'23](https://grail.cs.washington.edu/projects/dreampose/);
   - Face enhancement (relighting, restoration, etc): [Lumos SIGGRAPH Asia 2022](https://research.nvidia.com/labs/dir/lumos/), [RANA ICCV'23](https://nvlabs.github.io/RANA/);
   - Authorized use of synthetic videos: [Avatar Fingerprinting arXiv'23](https://research.nvidia.com/labs/nxp/avatar-fingerprinting/);
2. [Aliaksandr Siarohin @ Snap Research](https://research.snap.com/team/team-member.html#aliaksandr-siarohin)
   - Neural rendering models for human generation (focus on flow-based generative models): [Unsupervised-Volumetric-Animation CVPR'23](https://github.com/snap-research/unsupervised-volumetric-animation), [3DAvatarGAN CVPR'23](https://arxiv.org/abs/2301.02700), [3D-SGAN ECCV'22](https://arxiv.org/abs/2112.01422), [Articulated-Animation CVPR'21](https://arxiv.org/abs/2104.11280), [Monkey-Net CVPR'19](https://arxiv.org/abs/1812.08861), [FOMM NeurIPS'19](http://papers.nips.cc/paper/8935-first-order-motion-model-for-image-animation);
3. [Ziwei Liu @ Nanyang Technological University](https://liuziwei7.github.io/index.html)
   - Talking-face synthesis: [StyleSync CVPR'23](https://hangz-nju-cuhk.github.io/projects/StyleSync), [AV-CAT SIGGRAPH Asia 2022](https://hangz-nju-cuhk.github.io/projects/AV-CAT), [StyleGANX ICCV'23](https://www.mmlab-ntu.com/project/styleganex/), [StyleSwap ECCV'22](https://hangz-nju-cuhk.github.io/projects/StyleSwap), [PC-AVS CVPR'21](https://hangz-nju-cuhk.github.io/projects/PC-AVS), [Speech2Talking-Face IJCAI'21](https://www.ijcai.org/proceedings/2021/0141.pdf), [VToonify SIGGRAPH Asia 2022](https://www.youtube.com/watch?v=0_OmVhDgYuY);
   - Talking-body synthesis: [MotionDiffuse arXiv'22](https://mingyuan-zhang.github.io/projects/MotionDiffuse.html);
   - Face enhancement (relighting, restoration, etc): [Relighting4D ECCV'22](https://www.youtube.com/watch?v=NayAw89qtsY);
4. [Xiaodong Cun @ Tencent AI Lab](https://vinthony.github.io/academic/): 
   - Talking-face synthesis: [StyleHEAT ECCV'22](https://arxiv.org/abs/2203.04036), [VideoReTalking SIGGRAPH Asia'22](https://arxiv.org/abs/2211.14758), [ToolTalking ICCV'23](https://arxiv.org/abs/2308.12866), [DPE CVPR'23](https://arxiv.org/abs/2301.06281), [CodeTalker CVPR'23](https://arxiv.org/abs/2301.06281), [SadTalker CVPR'23](https://arxiv.org/abs/2211.12194);
   - Talking-body synthesis: [LivelySpeaker ICCV'23](https://arxiv.org/abs/2306.00926);
<!-- 5. [Gordon Wetzstein @ Stanford University](https://stanford.edu/~gordonwz/):
   - 3D face models (*e.g.,* 3DMM): [SSIF SIGGRAPH'23](https://research.nvidia.com/labs/toronto-ai/ssif/)  -->
5. Max Planck Institute for Informatics:
    - 3D face models (*e.g.,* 3DMM): [FLAME SIGGRAPH Asia 2017](https://flame.is.tue.mpg.de/);

## Papers
Example: [Conference'year] [Title](https://github.com/Jason-cs18/awesome-avatar), First-author Affiliation, [ProjectPage](https://github.com/Jason-cs18/awesome-avatar), [Code](https://github.com/Jason-cs18/awesome-avatar)
### 2D talking-face synthesis
- [MM 2020] [Wav2Lip: Accurately Lip-sync Videos to Any Speech](https://arxiv.org/abs/2008.10010), The International Institute of Islamic Thought (IIIT), India, [ProjectPage](https://bhaasha.iiit.ac.in/lipsync/), [Code](https://github.com/Rudrabha/Wav2Lip) ![Github stars](https://img.shields.io/github/stars/Rudrabha/Wav2Lip.svg) ![Github forks](https://img.shields.io/github/forks/Rudrabha/Wav2Lip.svg)
- [MM 2021] [Imitating Arbitrary Talking Style for Realistic Audio-Driven Talking Face Synthesis](https://hcsi.cs.tsinghua.edu.cn/Paper/Paper21/MM21-WUHAOZHE.pdf), Tsinghua University, [Code](https://github.com/wuhaozhe/style_avatar), ![Github stars](https://img.shields.io/github/stars/wuhaozhe/style_avatar.svg) ![Github forks](https://img.shields.io/github/forks/wuhaozhe/style_avatar.svg)
- [CVPR 2021] [Pose-Controllable Talking Face Generation by Implicitly Modularized Audio-Visual Representation](https://arxiv.org/abs/2104.11116), The Chinese University of Hong Kong, [ProjectPage](https://hangz-nju-cuhk.github.io/projects/PC-AVS), [Code](https://github.com/Hangz-nju-cuhk/Talking-Face_PC-AVS) ![Github stars](https://img.shields.io/github/stars/Hangz-nju-cuhk/Talking-Face_PC-AVS.svg) ![Github forks](https://img.shields.io/github/forks/Hangz-nju-cuhk/Talking-Face_PC-AVS.svg)
- [ICCV 2021] [PIRenderer: Controllable Portrait Image Generation via Semantic Neural Rendering](https://arxiv.org/abs/2109.08379), Peking University, [ProjectPage](https://renyurui.github.io/PIRender_web/), [Code](https://github.com/RenYurui/PIRender) ![Github stars](https://img.shields.io/github/stars/RenYurui/PIRender.svg) ![Github forks](https://img.shields.io/github/forks/RenYurui/PIRender.svg)
- [ECCV 2022] [StyleHEAT: One-Shot High-Resolution Editable Talking Face Generation via Pre-trained StyleGAN](https://arxiv.org/pdf/2203.04036.pdf), Tsinghua University, [ProjectPage](https://feiiyin.github.io/StyleHEAT/), [Code](https://github.com/OpenTalker/StyleHEAT) ![Github stars](https://img.shields.io/github/stars/OpenTalker/StyleHEAT.svg) ![Github forks](https://img.shields.io/github/forks/OpenTalker/StyleHEAT.svg)
- [SIGGRAPH Asia 2022] [VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild](https://github.com/OpenTalker/video-retalking), Xidian University, [ProjectPage](https://opentalker.github.io/video-retalking/), [Code](https://github.com/OpenTalker/video-retalking) ![Github stars](https://img.shields.io/github/stars/OpenTalker/video-retalking.svg) ![Github forks](https://img.shields.io/github/forks/OpenTalker/video-retalking.svg)
- [AAAI 2023] [DINet: Deformation Inpainting Network for Realistic Face Visually Dubbing on High Resolution Video](https://fuxivirtualhuman.github.io/pdf/AAAI2023_FaceDubbing.pdf), Virtual Human Group, Netease Fuxi AI Lab, [Code](https://github.com/MRzzm/DINet) ![Github stars](https://img.shields.io/github/stars/MRzzm/DINet.svg) ![Github forks](https://img.shields.io/github/forks/MRzzm/DINet.svg)
- [CVPR 2023] [SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation](https://arxiv.org/pdf/2211.12194.pdf), Xi'an Jiaotong University, [ProjectPage](https://sadtalker.github.io/), [Code](https://github.com/Winfredy/SadTalker) ![Github stars](https://img.shields.io/github/stars/OpenTalker/SadTalker.svg) ![Github forks](https://img.shields.io/github/forks/OpenTalker/SadTalker.svg), [Note](https://github.com/Jason-cs18/awesome-avatar/blob/main/notes/sadtalker.md)
- [CVPR 2023] [DPE: Disentanglement of Pose and Expression for General Video Portrait Editing](https://arxiv.org/abs/2301.06281), MAIS & NLPR, Institute of Automation, Chinese Academy of Sciences, [ProjectPage](https://carlyx.github.io/DPE/), [Code](https://github.com/Carlyx/DPE) ![Github stars](https://img.shields.io/github/stars/Carlyx/DPE.svg) ![Github forks](https://img.shields.io/github/forks/Carlyx/DPE.svg)
- [ICCV 2023] [MODA: Mapping-Once Audio-driven Portrait Animation with Dual Attentions](https://arxiv.org/abs/2307.10008), International Digital Economy Academy (IDEA), China, [ProjectPage](https://liuyunfei.net/projects/iccv23-moda/), [Code](https://github.com/DreamtaleCore/MODA), ![Github stars](https://img.shields.io/github/stars/DreamtaleCore/MODA.svg) ![Github forks](https://img.shields.io/github/forks/DreamtaleCore/MODA.svg)
- [ICCV 2023] [ToonTalker: Cross-Domain Face Reenactment](https://arxiv.org/abs/2308.12866), Tsinghua University, [ProjectPage](https://opentalker.github.io/ToonTalker/), [Code](https://github.com/yuanygong/ToonTalker) ![Github stars](https://img.shields.io/github/stars/yuanygong/ToonTalker.svg) ![Github forks](https://img.shields.io/github/forks/yuanygong/ToonTalker.svg)

### 3D talking-face synthesis
- [ICCV 2021] [AD-NeRF: Audio Driven Neural Radiance Fields for Talking Head Synthesis](https://arxiv.org/abs/2103.11078), University of Science and Technology of China, [ProjectPage](https://yudongguo.github.io/ADNeRF/), [Code](https://github.com/YudongGuo/AD-NeRF) ![Github stars](https://img.shields.io/github/stars/YudongGuo/AD-NeRF.svg) ![Github forks](https://img.shields.io/github/forks/YudongGuo/AD-NeRF.svg) 
- [ECCV 2022] [Learning Dynamic Facial Radiance Fields for Few-Shot Talking Head Synthesis](https://github.com/sstzal/DFRF/blob/show_page/images/DFRF_eccv2022.pdf), Tsinghua University, [ProjectPage](https://sstzal.github.io/DFRF/), [Code](https://github.com/sstzal/DFRF) ![Github stars](https://img.shields.io/github/stars/sstzal/DFRF.svg) ![Github forks](https://img.shields.io/github/forks/sstzal/DFRF.svg)
- [ICLR 2023] [GeneFace: Generalized and High-Fidelity Audio-Driven 3D Talking Face Synthesis](https://arxiv.org/abs/2301.13430), Zhejiang University, [ProjectPage](https://geneface.github.io/), [Code](https://github.com/yerfor/GeneFace) ![Github stars](https://img.shields.io/github/stars/yerfor/GeneFace.svg) ![Github forks](https://img.shields.io/github/forks/yerfor/GeneFace.svg)
- [ICCV 2023] [Efficient Region-Aware Neural Radiance Fields for High-Fidelity Talking Portrait Synthesis](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Efficient_Region-Aware_Neural_Radiance_Fields_for_High-Fidelity_Talking_Portrait_Synthesis_ICCV_2023_paper.html), Beihang University, [ProjectPage](https://fictionarry.github.io/ER-NeRF/), [Code](https://github.com/Fictionarry/ER-NeRF) ![Github stars](https://img.shields.io/github/stars/Fictionarry/ER-NeRF.svg) ![Github forks](https://img.shields.io/github/forks/Fictionarry/ER-NeRF.svg)
- [arXiv 2023] [GeneFace++: Generalized and Stable Real-Time Audio-Driven 3D Talking Face Generation](https://arxiv.org/abs/2305.00787), Zhejiang University

### Talking-body synthesis

#### Co-speech gesture synthesis
- [SIGGRAPH Asia 2020] [Gesture Generation from Trimodal Context](https://arxiv.org/abs/2009.02119), Korea Advanced Institute of Science and Technology (KAIST), [Code](https://github.com/ai4r/Gesture-Generation-from-Trimodal-Context) ![Github stars](https://img.shields.io/github/stars/ai4r/Gesture-Generation-from-Trimodal-Context.svg) ![Github forks](https://img.shields.io/github/forks/ai4r/Gesture-Generation-from-Trimodal-Context.svg)
- [ICCV 2021] [Speech Drives Templates: Co-Speech Gesture Synthesis with Learned Templates](https://openaccess.thecvf.com/content/ICCV2021/papers/Qian_Speech_Drives_Templates_Co-Speech_Gesture_Synthesis_With_Learned_Templates_ICCV_2021_paper.pdf), ShanghaiTech University, [ProjectPage](https://shenhanqian.github.io/sdt), [Code](https://github.com/ShenhanQian/SpeechDrivesTemplates) ![Github stars](https://img.shields.io/github/stars/ShenhanQian/SpeechDrivesTemplates.svg) ![Github forks](https://img.shields.io/github/forks/ShenhanQian/SpeechDrivesTemplates.svg)
- [ICCV 2021] [Audio2Motion: Generating Diverse Gestures from Speech with Conditional Variational Autoencoders](https://openaccess.thecvf.com/content/ICCV2021/papers/Li_Audio2Gestures_Generating_Diverse_Gestures_From_Speech_Audio_With_Conditional_Variational_ICCV_2021_paper.pdf), Harbin Institute of Technology, Shenzhen, [Code](https://github.com/JingLi513/Audio2Gestures) ![Github stars](https://img.shields.io/github/stars/JingLi513/Audio2Gestures.svg) ![Github forks](https://img.shields.io/github/forks/JingLi513/Audio2Gestures.svg)
- [CVPR 2022] [Learning Hierarchical Cross-Modal Association for Co-Speech Gesture Generation](https://arxiv.org/pdf/2203.13161.pdf), The Chinese University of Hong Kong, [ProjectPage](https://alvinliu0.github.io/projects/HA2G), [Code](https://github.com/alvinliu0/HA2G) ![Github stars](https://img.shields.io/github/stars/alvinliu0/HA2G.svg) ![Github forks](https://img.shields.io/github/forks/alvinliu0/HA2G.svg)
- [CVPR 2023] [Taming Diffusion Models for Audio-Driven Co-Speech Gesture Generation](https://arxiv.org/abs/2303.09119), The University of Hong Kong, [Code](https://github.com/Advocate99/DiffGesture) ![Github stars](https://img.shields.io/github/stars/Advocate99/DiffGesture.svg) ![Github forks](https://img.shields.io/github/forks/Advocate99/DiffGesture.svg)
#### Pose2image
- [NeurIPS 2018] [Video-to-Video Synthesis](https://github.com/NVIDIA/vid2vid), NVIDIA, [ProjectPage](https://tcwang0509.github.io/vid2vid/), [Code](https://github.com/NVIDIA/vid2vid) ![Github stars](https://img.shields.io/github/stars/NVIDIA/vid2vid.svg) ![Github forks](https://img.shields.io/github/forks/NVIDIA/vid2vid.svg)
- [ICCV 2019] [Everybody Dance Now](https://github.com/carolineec/EverybodyDanceNow), UC Berkeley, [ProjectPage](https://carolineec.github.io/everybody_dance_now/), [Code](https://github.com/carolineec/EverybodyDanceNow) ![Github stars](https://img.shields.io/github/stars/carolineec/EverybodyDanceNow.svg) ![Github forks](https://img.shields.io/github/forks/carolineec/EverybodyDanceNow.svg)

## Datasets

### Talking-face
<!-- ||||||||
|-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Dataset name|Environment|Year|Resolution|Subject|Duration|Sentence|
: Table caption -->

<table>
	<tr>
	    <th colspan="7"><center>Audio-Visual Datasets for Enlish Speakers</center></th>
	</tr >
	<tr>
	    <td >Dataset name</td>
	    <td>Environment</td>
	    <td>Year</td>
        <td>Resolution</td>
        <td>Subject</td>
        <td>Duration</td>
        <td>Sentence</td> 
	</tr >
    <tr>
	    <td ><a href="https://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1.html">VoxCeleb1</a></td>
	    <td>Wild</td>
	    <td>2017</td>
        <td>360p~720p</td>
        <td>1251</td>
        <td>352 hours</td>
        <td>100k</td> 
	</tr >
    <tr>
	    <td ><a href="https://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox2.html">VoxCeleb2</a></td>
	    <td>Wild</td>
	    <td>2018</td>
        <td>360p~720p</td>
        <td>6112</td>
        <td>2442 hours</td>
        <td>1128k</td> 
	</tr >
    <tr>
	    <td ><a href="https://github.com/MRzzm/HDTF">HDTF</a></td>
	    <td>Wild</td>
	    <td>2020</td>
        <td>720p~1080p</td>
        <td>300+</td>
        <td>15.8 hours</td>
        <td></td> 
	</tr >
    <tr>
	    <td><a href="https://github.com/YuanxunLu/LiveSpeechPortraits">LSP</a></td>
	    <td>Wild</td>
	    <td>2021</td>
        <td>720p~1080p</td>
        <td>4</td>
        <td>18 minutes</td>
        <td>100k</td> 
	</tr >
    <tr>
	    <th colspan="7"><center>Audio-Visual Datasets for Chinese Speakers</center></th>
	</tr >
	<tr>
	    <td >Dataset name</td>
	    <td>Environment</td>
	    <td>Year</td>
        <td>Resolution</td>
        <td>Subject</td>
        <td>Duration</td>
        <td>Sentence</td> 
	</tr >
    <tr>
	    <td ><a href="https://www.vipazoo.cn/CMLR.html">CMLR</a></td>
	    <td>Lab</td>
	    <td>2019</td>
        <td></td>
        <td>11</td>
        <td></td>
        <td>102k</td> 
	</tr >
    <tr>
	    <td > <a href="https://github.com/SpringHuo/MAVD"><b>MAVD</b></a></td>
	    <td>Lab</td>
	    <td>2023</td>
        <td>1920x1080</td>
        <td>64</td>
        <td>24 hours</td>
        <td>12k</td> 
	</tr >
    <tr>
	    <td ><a href="http://cnceleb.org/">CN-Celeb</a></td>
	    <td>Wild</td>
	    <td>2020</td>
        <td></td>
        <td>3000</td>
        <td>1200 hours</td>
        <td></td> 
	</tr >
    <tr>
	    <td ><a href="http://cnceleb.org/">CN-Celeb-AV</a></td>
	    <td>Wild</td>
	    <td>2023</td>
        <td></td>
        <td>1136</td>
        <td>660 hours</td>
        <td></td> 
	</tr >
    <tr>
	    <td ><a href="http://cnceleb.org/"><b>CN-CVS</b></a></td>
	    <td>Wild</td>
	    <td>2023</td>
        <td></td>
        <td>2500+</td>
        <td>300+ hours</td>
        <td></td> 
	</tr >
	<!-- <tr >
	    <td>应用层</td>
	    <td rowspan="3">应用层</td>
	    <td rowspan="3">应用层</td>
	</tr>
	<tr>
	    <td>表示层</td>
	</tr>
	<tr>
	    <td>会话层</td>
	</tr>
	<tr>
	    <td>传输层</td>
	    <td>传输层</td>
       <td>传输层</td>
	</tr>
	<tr>
       <td>网络层</td>
	    <td>网络层</td>
       <td>网络层</td>
	</tr>
	<tr>
	    <td>数据链路层</td>
	    <td rowspan="2">网络接口层</td>
       <td>数据链路层</td>
	</tr>
	<tr>
	    <td>物理层</td>
	    <td>物理层</td>
	</tr> -->
</table>


### Talking-body
TBD

## Metrics

### Talking-face
<table>
	<tr>
	    <th colspan="3"><center>Lip-Sync</center></th>
	</tr >
	<tr>
	    <td >Metric name</td>
	    <td>Description</td>
	    <td>Code/Paper</td>
	</tr >
    <tr>
	    <td >LMD&#8595;</td>
	    <td>Mouth landmark distance</td>
	    <td></td>
	</tr >
    <tr>
	    <td >LMD&#8595;</td>
	    <td>Mouth landmark distance</td>
	    <td></td>
	</tr >
    <tr>
	    <td >MA&#8593;</td>
	    <td>The Insertion-over-Union (IoU) for the overlap between the predicted mouth area and the ground truth area</td>
	    <td></td>
	</tr >
    <tr>
	    <td >Sync&#8593;</td>
	    <td>The confidence score from SyncNet (Sync)</td>
	    <td><a href="https://github.com/Rudrabha/Wav2Lip/tree/master/evaluation">wav2lip</a></td>
	</tr >
    <tr>
	    <td >LSE-C&#8593;</td>
	    <td>Lip Sync Error - Confidence</td>
	    <td><a href="https://github.com/Rudrabha/Wav2Lip/tree/master/evaluation">wav2lip</a></td>
	</tr >
    <tr>
	    <td >LSE-D&#8595;</td>
	    <td>Lip Sync Error - Distance</td>
	    <td><a href="https://github.com/Rudrabha/Wav2Lip/tree/master/evaluation">wav2lip</a></td>
	</tr >
    <tr>
	    <th colspan="3"><center>Image Quality (identity preserving)</center></th>
	</tr >
	<tr>
	    <td >Metric name</td>
	    <td>Description</td>
	    <td>Code/Paper</td>
	</tr >
    <tr>
	    <td >MAE&#8595;</td>
	    <td>Mean Absolute Error metric for image</td>
	    <td><a href="https://github.com/open-mmlab/mmagic/blob/a2135e11f3d66c1a2828c71221ed5e5699ecd919/docs/en/user_guides/metrics.md">mmagic</a></td>
	</tr >
    <tr>
	    <td >MSE&#8595;</td>
	    <td>Mean Squared Error metric for image</td>
	    <td><a href="https://github.com/open-mmlab/mmagic/blob/a2135e11f3d66c1a2828c71221ed5e5699ecd919/docs/en/user_guides/metrics.md">mmagic</a></td>
	</tr >
    <tr>
	    <td >PSNR&#8593;</td>
	    <td>Peak Signal-to-Noise Ratio</td>
	    <td><a href="https://github.com/open-mmlab/mmagic/blob/a2135e11f3d66c1a2828c71221ed5e5699ecd919/docs/en/user_guides/metrics.md">mmagic</a></td>
	</tr >
    <tr>
	    <td >SSIM&#8593;</td>
	    <td>Structural similarity for image</td>
	    <td><a href="https://github.com/open-mmlab/mmagic/blob/a2135e11f3d66c1a2828c71221ed5e5699ecd919/docs/en/user_guides/metrics.md">mmagic</a></td>
	</tr >
    <tr>
	    <td >FID&#8595;</td>
	    <td>Frchet Inception Distance</td>
	    <td><a href="https://github.com/open-mmlab/mmagic/blob/a2135e11f3d66c1a2828c71221ed5e5699ecd919/docs/en/user_guides/metrics.md">mmagic</a></td>
	</tr >
    <tr>
	    <td >IS&#8593;</td>
	    <td>Inception score </td>
	    <td><a href="https://github.com/open-mmlab/mmagic/blob/a2135e11f3d66c1a2828c71221ed5e5699ecd919/docs/en/user_guides/metrics.md">mmagic</a></td>
	</tr >
    <tr>
	    <td >NIQE&#8595;</td>
	    <td>Natural Image Quality Evaluator metric</td>
	    <td><a href="https://github.com/open-mmlab/mmagic/blob/a2135e11f3d66c1a2828c71221ed5e5699ecd919/docs/en/user_guides/metrics.md">mmagic</a></td>
	</tr >
    <tr>
	    <td >CSIM&#8593;</td>
	    <td>The cosine similarity of identity embedding</td>
	    <td><a href="https://github.com/deepinsight/insightface/issues/903">InsightFace</a></td>
	</tr >
    <tr>
	    <td >CPBD&#8593;</td>
	    <td>The cumulative probability blur detection</td>
	    <td><a href="https://pypi.org/project/cpbd/">python-cpbd</a></td>
	</tr >
    <tr>
	    <th colspan="3"><center>Diversity</center></th>
	</tr >
	<tr>
	    <td >Metric name</td>
	    <td>Description</td>
	    <td>Code/Paper</td>
	</tr >
    <tr>
	    <td >Diversity of head motions&#8593;</td>
	    <td>A standard deviation of the head motion feature embeddings extracted from the generated frames using Hopenet (Ruiz et al., 2018) is calculated</td>
	    <td><a href="https://arxiv.org/pdf/2211.12194.pdf">SadTalker</a></td>
	</tr >
     <tr>
	    <td >Beat Align Score&#8593;</td>
	    <td>The alignment of the audio and generated head motions is calculated in Bailando (Siyao et al., 2022)</td>
	    <td><a href="https://arxiv.org/pdf/2211.12194.pdf">SadTalker</a></td>
	</tr >
</table>

### Talking-body
TBD

## Toolbox
1. A general toolbox for AIGC, including common metrics and models https://github.com/open-mmlab/mmagic
2. face3d: Python tools for processing 3D face https://github.com/yfeng95/face3d
3. 3DMM model fitting using Pytorch https://github.com/ascust/3DMM-Fitting-Pytorch
4. OpenFace: a facial behavior analysis toolkit https://github.com/TadasBaltrusaitis/OpenFace
5. autocrop: Automatically detects and crops faces from batches of pictures https://github.com/leblancfg/autocrop
6. OpenPose: Real-time multi-person keypoint detection library for body, face, hands, and foot estimation https://github.com/CMU-Perceptual-Computing-Lab/openpose
7. GFPGAN: Practical Algorithm for Real-world Face Restoration https://github.com/TencentARC/GFPGAN
8. CodeFormer: Robust Blind Face Restoration https://github.com/sczhou/CodeFormer

## Related Links
If you are interested in avatar and digital human, we would also like to recommend you to check out other related collections:
- awesome digital human https://github.com/weihaox/awesome-digital-human
