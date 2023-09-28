# awesome-avatar
This is a repository for organizing papers, codes and other resources related to the topic of Avatar (talking-face and talking-body). 

#### 🔆 This project is still on-going, pull requests are welcomed!!
If you have any suggestions (missing papers, new papers, key researchers or typos), please feel free to edit and pull a request.

#### TO DO LIST

- [ ] Main paper list
- [x] Researchers list
- [ ] Toolbox for avatar
- [ ] Add paper link
- [ ] Add paper notes
- [ ] Add codes if have
- [ ] Add project page if have
- [x] Datasets and metrics

## Researchers and labs
1. [Deep Imagination Research (DIR) group @ NVIDIA](https://arunmallya.github.io/)
   - Neural rendering models for human generation: [vid2vid NeurIPS'18](https://tcwang0509.github.io/vid2vid/), [fs-vid2vid NeurIPS'19](https://nvlabs.github.io/few-shot-vid2vid/);
   - Talking-face synthesis: [face-vid2vid CVPR'21](https://nvlabs.github.io/face-vid2vid/), [Implicit NeurIPS'22](https://research.nvidia.com/labs/dir/implicit_warping/), [SPACE ICCV'23](https://research.nvidia.com/labs/dir/space/);
   - Talking-body synthesis: [DreamPose ICCV'23](https://grail.cs.washington.edu/projects/dreampose/);
   - Face enhancement (relighting, restoration, etc): [Lumos SIGGRAPH Asia 2022](https://research.nvidia.com/labs/dir/lumos/);
2. [Aliaksandr Siarohin @ Snap Research](https://research.snap.com/team/team-member.html#aliaksandr-siarohin)
   - Neural rendering models for human generation (focus on flow-based generative models): [Unsupervised-Volumetric-Animation CVPR'23](https://github.com/snap-research/unsupervised-volumetric-animation), [3DAvatarGAN CVPR'23](https://arxiv.org/abs/2301.02700), [3D-SGAN ECCV'22](https://arxiv.org/abs/2112.01422), [Articulated-Animation CVPR'21](https://arxiv.org/abs/2104.11280), [Monkey-Net CVPR'19](https://arxiv.org/abs/1812.08861), [FOMM NeurIPS'19](http://papers.nips.cc/paper/8935-first-order-motion-model-for-image-animation);
3. [Ziwei Liu @ NTU](https://liuziwei7.github.io/index.html)
   - Talking-face synthesis: [StyleSync CVPR'23](https://hangz-nju-cuhk.github.io/projects/StyleSync), [AV-CAT SIGGRAPH Asia 2022](https://hangz-nju-cuhk.github.io/projects/AV-CAT), [StyleGANX ICCV'23](https://www.mmlab-ntu.com/project/styleganex/), [StyleSwap ECCV'22](https://hangz-nju-cuhk.github.io/projects/StyleSwap), [PC-AVS CVPR'21](https://hangz-nju-cuhk.github.io/projects/PC-AVS), [Speech2Talking-Face IJCAI'21](https://www.ijcai.org/proceedings/2021/0141.pdf), [VToonify SIGGRAPH Asia 2022](https://www.youtube.com/watch?v=0_OmVhDgYuY);
   - Talking-body synthesis: [MotionDiffuse arXiv'22](https://mingyuan-zhang.github.io/projects/MotionDiffuse.html);
   - Face enhancement (relighting, restoration, etc): [Relighting4D ECCV'22](https://www.youtube.com/watch?v=NayAw89qtsY);
4. [Xiaodong Cun @ Tencent AI Lab](https://vinthony.github.io/academic/): 
   - Talking-face synthesis: [StyleHEAT ECCV'22](https://arxiv.org/abs/2203.04036), [VideoReTalking SIGGRAPH Asia'22](https://arxiv.org/abs/2211.14758), [ToolTalking ICCV'23](https://arxiv.org/abs/2308.12866), [DPE CVPR'23](https://arxiv.org/abs/2301.06281), [CodeTalker CVPR'23](https://arxiv.org/abs/2301.06281), [SadTalker CVPR'23](https://arxiv.org/abs/2211.12194);
   - Talking-body synthesis: [LivelySpeaker ICCV'23](https://arxiv.org/abs/2306.00926);

## Papers
Example: [Conference'year] [Title](https://github.com/Jason-cs18/awesome-avatar), First-author Affiliation, [ProjectPage](https://github.com/Jason-cs18/awesome-avatar), [Code](https://github.com/Jason-cs18/awesome-avatar)
### 2D talking-face synthesis
- [MM 2020] [Wav2Lip: Accurately Lip-sync Videos to Any Speech](https://arxiv.org/abs/2008.10010), The International Institute of Islamic Thought (IIIT), India, [ProjectPage](https://bhaasha.iiit.ac.in/lipsync/), [Code](https://github.com/Rudrabha/Wav2Lip) ![Github stars](https://img.shields.io/github/stars/Rudrabha/Wav2Lip.svg) ![Github forks](https://img.shields.io/github/forks/Rudrabha/Wav2Lip.svg)
- [CVPR 2021] [Pose-Controllable Talking Face Generation by Implicitly Modularized Audio-Visual Representation](https://arxiv.org/abs/2104.11116), The Chinese University of Hong Kong, [ProjectPage](https://hangz-nju-cuhk.github.io/projects/PC-AVS), [Code](https://github.com/Hangz-nju-cuhk/Talking-Face_PC-AVS) ![Github stars](https://img.shields.io/github/stars/Hangz-nju-cuhk/Talking-Face_PC-AVS.svg) ![Github forks](https://img.shields.io/github/forks/Hangz-nju-cuhk/Talking-Face_PC-AVS.svg)
- [ICCV 2021] [PIRenderer: Controllable Portrait Image Generation via Semantic Neural Rendering](https://arxiv.org/abs/2109.08379), Peking University, [ProjectPage](https://renyurui.github.io/PIRender_web/), [Code](https://github.com/RenYurui/PIRender) ![Github stars](https://img.shields.io/github/stars/RenYurui/PIRender.svg) ![Github forks](https://img.shields.io/github/forks/RenYurui/PIRender.svg)
- [ECCV 2022] [StyleHEAT: One-Shot High-Resolution Editable Talking Face Generation via Pre-trained StyleGAN](https://arxiv.org/pdf/2203.04036.pdf), Tsinghua University, [ProjectPage](https://feiiyin.github.io/StyleHEAT/), [Code](https://github.com/OpenTalker/StyleHEAT) ![Github stars](https://img.shields.io/github/stars/OpenTalker/StyleHEAT.svg) ![Github forks](https://img.shields.io/github/forks/OpenTalker/StyleHEAT.svg)
- [SIGGRAPH Asia 2022] [VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing In the Wild](https://github.com/OpenTalker/video-retalking), Xidian University, [ProjectPage](https://opentalker.github.io/video-retalking/), [Code](https://github.com/OpenTalker/video-retalking) ![Github stars](https://img.shields.io/github/stars/OpenTalker/video-retalking.svg) ![Github forks](https://img.shields.io/github/forks/OpenTalker/video-retalking.svg)
- [AAAI 2023] [DINet: Deformation Inpainting Network for Realistic Face Visually Dubbing on High Resolution Video](https://fuxivirtualhuman.github.io/pdf/AAAI2023_FaceDubbing.pdf), Virtual Human Group, Netease Fuxi AI Lab, [Code](https://github.com/MRzzm/DINet) ![Github stars](https://img.shields.io/github/stars/MRzzm/DINet.svg) ![Github forks](https://img.shields.io/github/forks/MRzzm/DINet.svg)
- [CVPR 2023] [SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation](https://arxiv.org/pdf/2211.12194.pdf), Xi'an Jiaotong University, [ProjectPage](https://sadtalker.github.io/), [Code](https://github.com/Winfredy/SadTalker) ![Github stars](https://img.shields.io/github/stars/OpenTalker/SadTalker.svg) ![Github forks](https://img.shields.io/github/forks/OpenTalker/SadTalker.svg)
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
xxx
#### Co-speech gesture synthesis
xxx
#### Pose2image
xxx

## Datasets
### Talking-face
### Talking-body

## Metrics
### Talking-face
### Talking-body

## Toolbox
1. A general toolbox for AIGC, including common metrics and models https://github.com/open-mmlab/mmagic
2. face3d: Python tools for processing 3D face https://github.com/yfeng95/face3d
3. 3DMM model fitting using Pytorch https://github.com/ascust/3DMM-Fitting-Pytorch
4. OpenFace: a facial behavior analysis toolkit https://github.com/TadasBaltrusaitis/OpenFace
5. autocrop: Automatically detects and crops faces from batches of pictures https://github.com/leblancfg/autocrop
6. OpenPose: Real-time multi-person keypoint detection library for body, face, hands, and foot estimation https://github.com/CMU-Perceptual-Computing-Lab/openpose