# ICCV'23, Oct 4-6, 2023
In this page, we provide a short review of recent advances (21 papers) on the digital human, including 3D face reconstruction, talking-face synthesis, talking-body synthesis, and talking-face video editing.

## Workshops and Tutorials
1. To NeRF or not to NeRF: 
A View Synthesis Challenge for Human Heads https://sites.google.com/view/vschh/home
2. The 11th IEEE International Workshop on Analysis and Modeling of Faces and Gestures https://web.northeastern.edu/smilelab/amfg2023/
## 3D Face Reconstruction (3)

![](https://project-hiface.github.io/img/detail.gif)

<!-- <video src='https://project-hiface.github.io/video/video_demo.mp4' width=/> -->

- [Speech4Mesh: Speech-Assisted Monocular 3D Facial Reconstruction for Speech-Driven 3D Facial Animation](https://openaccess.thecvf.com/content/ICCV2023/papers/He_Speech4Mesh_Speech-Assisted_Monocular_3D_Facial_Reconstruction_for_Speech-Driven_3D_Facial_ICCV_2023_paper.pdf), University of Science and Technology of China, [FLAME-Universe (3DMM alternative)](https://github.com/TimoBolkart/FLAME-Universe).
- [HiFace: High-Fidelity 3D Face Reconstruction by
Learning Static and Dynamic Details](https://openaccess.thecvf.com/content/ICCV2023/papers/Chai_HiFace_High-Fidelity_3D_Face_Reconstruction_by_Learning_Static_and_Dynamic_ICCV_2023_paper.pdf), National University of Singapore, [ProjectPage](https://project-hiface.github.io/). 
- [ASM: Adaptive Skinning Model for High-Quality 3D Face Modeling](https://openaccess.thecvf.com/content/ICCV2023/papers/Yang_ASM_Adaptive_Skinning_Model_for_High-Quality_3D_Face_Modeling_ICCV_2023_paper.pdf), Tencent AI Lab.
## Talking-Face Synthesis

### Metrics and Benchchmarks (1)
- [On the Audio-visual Synchronization for Lip-to-Speech Synthesis](https://openaccess.thecvf.com/content/ICCV2023/papers/Niu_On_the_Audio-visual_Synchronization_for_Lip-to-Speech_Synthesis_ICCV_2023_paper.pdf), The Hong Kong University of Science and Technology.

### 2D Talking-Face Synthesis (11)
*keywords: emotion, diffusion priors, memory network, StyleGAN2*;

![](https://github.com/StelaBou/HyperReenact/raw/master/images/architecture.png)

- [Emotional Listener Portrait: Realistic Listener Motion Simulation in Conversation](https://openaccess.thecvf.com/content/ICCV2023/html/Song_Emotional_Listener_Portrait_Neural_Listener_Head_Generation_with_Emotion_ICCV_2023_paper.html), University of Rochester.​
- [Talking Head Generation with Probabilistic Audio-to-Visual Diffusion Priors](https://openaccess.thecvf.com/content/ICCV2023/html/Yu_Talking_Head_Generation_with_Probabilistic_Audio-to-Visual_Diffusion_Priors_ICCV_2023_paper.html), Xiaobing.AI, [ProjectPage](https://zxyin.github.io/TH-PAD/).​
- [Efficient Emotional Adaptation for Audio-Driven Talking-Head Generation](https://openaccess.thecvf.com/content/ICCV2023/papers/Gan_Efficient_Emotional_Adaptation_for_Audio-Driven_Talking-Head_Generation_ICCV_2023_paper.pdf), Zhejiang University, [ProjectPage](https://yuangan.github.io/eat/), [Code](https://github.com/yuangan/EAT_code), [Blog](https://zhuanlan.zhihu.com/p/658569026).​
- [Implicit Identity Representation Conditioned Memory Compensation Network for Talking Head Video Generation](https://openaccess.thecvf.com/content/ICCV2023/papers/Hong_Implicit_Identity_Representation_Conditioned_Memory_Compensation_Network_for_Talking_Head_ICCV_2023_paper.pdf), The Hong Kong University of Science and Technology, [ProjectPage](https://harlanhong.github.io/publications/mcnet.html), [Code](https://github.com/harlanhong/ICCV2023-MCNET).​
- [ToonTalker: Cross-Domain Face Reenactment](https://openaccess.thecvf.com/content/ICCV2023/papers/Gong_ToonTalker_Cross-Domain_Face_Reenactment_ICCV_2023_paper.pdf), Tsinghua University, [ProjectPage](https://opentalker.github.io/ToonTalker/), [Code](https://github.com/yuanygong/ToonTalker).​
- [Robust One-Shot Face Video Re-enactment using Hybrid Latent Spaces of StyleGAN2](https://openaccess.thecvf.com/content/ICCV2023/papers/Oorloff_Robust_One-Shot_Face_Video_Re-enactment_using_Hybrid_Latent_Spaces_of_ICCV_2023_paper.pdf), University of Maryland, [ProjectPage](https://trevineoorloff.github.io/FaceVideoReenactment_HybridLatents.io/).
- [EMMN: Emotional Motion Memory Network for Audio-driven Emotional Talking Face Generation](https://openaccess.thecvf.com/content/ICCV2023/papers/Tan_EMMN_Emotional_Motion_Memory_Network_for_Audio-driven_Emotional_Talking_Face_ICCV_2023_paper.pdf), Shanghai Jiao Tong University.
- [EmoTalk: Speech-Driven Emotional Disentanglement for 3D Face Animation](https://openaccess.thecvf.com/content/ICCV2023/papers/Peng_EmoTalk_Speech-Driven_Emotional_Disentanglement_for_3D_Face_Animation_ICCV_2023_paper.pdf), Renmin University of China, [ProjectPage](https://ziqiaopeng.github.io/emotalk/), [Code](https://github.com/psyai-net/EmoTalk_release).
- [HyperReenact: One-Shot Reenactment via Jointly Learning to Refine and
Retarget Faces](https://openaccess.thecvf.com/content/ICCV2023/papers/Bounareli_HyperReenact_One-Shot_Reenactment_via_Jointly_Learning_to_Refine_and_Retarget_ICCV_2023_paper.pdf), Kingston University London, [Code](https://github.com/StelaBou/HyperReenact).
- [MODA: Mapping-Once Audio-driven Portrait Animation with Dual Attentions](https://openaccess.thecvf.com/content/ICCV2023/papers/Liu_MODA_Mapping-Once_Audio-driven_Portrait_Animation_with_Dual_Attentions_ICCV_2023_paper.pdf), International Digital Economy Academy (IDEA), [ProjectPage](https://liuyunfei.net/projects/iccv23-moda/), [Code](https://github.com/DreamtaleCore/MODA).
- [SPACE: Speech-driven Portrait Animation with Controllable Expression](https://openaccess.thecvf.com/content/ICCV2023/papers/Gururani_SPACE_Speech-driven_Portrait_Animation_with_Controllable_Expression_ICCV_2023_paper.pdf), NVIDIA, [ProjectPage](https://research.nvidia.com/labs/dir/space/).
### 3D Talking-Face Synthesis (1)
*keywords: efficiency*;

- [Efficient Region-Aware Neural Radiance Fields for High-Fidelity Talking Portrait Synthesis](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Efficient_Region-Aware_Neural_Radiance_Fields_for_High-Fidelity_Talking_Portrait_Synthesis_ICCV_2023_paper.html), Beihang University, [Code](https://github.com/Fictionarry/ER-NeRF).

## Talking-Face Video Editing (1)

*keywords: GAN inversion, StyleGAN*;

- [RIGID: Recurrent GAN Inversion and Editing of Real Face Videos](https://openaccess.thecvf.com/content/ICCV2023/papers/Xu_RIGID_Recurrent_GAN_Inversion_and_Editing_of_Real_Face_Videos_ICCV_2023_paper.pdf), The University of Hong Kong, [ProjectPage](https://cnnlstm.github.io/RIGID/), [Code](https://github.com/cnnlstm/RIGID).

## Talking-Body Synthesis (4)

*keywords: continual learning, lively, one-shot*;

- [Continual Learning for Personalized Co-Speech Gesture Generation](https://openaccess.thecvf.com/content/ICCV2023/html/Ahuja_Continual_Learning_for_Personalized_Co-speech_Gesture_Generation_ICCV_2023_paper.html), CMU, [ProjectPage](https://chahuja.com/cdiffgan/), [Dataset](https://chahuja.com/pats/).​
- [LivelySpeaker: Towards Semantic-Aware Co-Speech Gesture Generation](https://openaccess.thecvf.com/content/ICCV2023/html/Zhi_LivelySpeaker_Towards_Semantic-Aware_Co-Speech_Gesture_Generation_ICCV_2023_paper.html), ShanghaiTech University, [Code](https://github.com/zyhbili/LivelySpeaker). ​
- [DINAR: Diffusion Inpainting of Neural Textures for One-Shot Human Avatars](https://openaccess.thecvf.com/content/ICCV2023/html/Svitov_DINAR_Diffusion_Inpainting_of_Neural_Textures_for_One-Shot_Human_Avatars_ICCV_2023_paper.html), Samsung AI Center, [Code](https://github.com/SamsungLabs/DINAR).​
- [One-shot Implicit Animatable Avatars with Model-based Priors](https://openaccess.thecvf.com/content/ICCV2023/html/Huang_One-shot_Implicit_Animatable_Avatars_with_Model-based_Priors_ICCV_2023_paper.html), Zhejiang University, [Code](https://github.com/huangyangyi/ELICIT).
