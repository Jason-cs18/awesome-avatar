## SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation
A VAE-based poseNet is integrated with a new talking-face generation pipeline SadTalker to generate diverse head motions on talking-face videos.

![SadTalker overview](https://github.com/Jason-cs18/awesome-avatar/blob/main/assets/sadtalker.png "SadTalker overview")

**What's new:** Wenxuan Zhang from Xi'an Jiaotong University and researchers from Tencent AI Lab have released a new generation pipeline named SadTalker to synthesis diverse and stylized talking-face videos.

**Key insights:** Facial landmarks and keypoints were previously used as the intermediate facial representation in works, but they were found to be difficult to disentangle with expressions and movements. To address this issue, SadTalker leveraged a explicit 3D face model to decouple the representations of expression and head motions. As a result, they designed PoseVAE and ExpNet to learn audio-to-expression and audio-to-pose, respectively.

<!-- Previous works leverages xxx to achieve xxx but they are limited by xxx. To overcome xxx, authors designed xxx. -->

**How it works:** As shown in the Figure 2, the authors designed a three-stage inference pipeline to synthesize stylized talking-face videos. 
- They first leveraged the recent single image deep 3D reconstruction method to extract the 3D face model on the target image, which consists of identity coefficients, expression coefficients and head pose (rotation and translation).
- Secondly, they estimated the pose and expression coefficients using PoseVAE and ExpNet, respectively. After that, they obtained a motion flow in the 3D facial space. During training, the authors used reconstruction loss and distillation loss to motivate ExpNet to learn accurate mapping on the entire facial motion and the lip motion, respectively. Similarly, reconstruction loss and KL-divergence loss were used to motivate PoseVAE to learn accurate and diverse head motions, respectively.
- In the third, they leveraged a modified face vid2vid model to render real face from the estimated 3D facial motion. In training, they first trained face vid2vid in a self-supervised fashion. Then they fine-tuned the customized mappingNet in a reconstruction style.
<!-- - they trained ExpNet with the reconstruction loss and distillation loss. The reconstruction loss encouraged the model to learn the accurate mapping in explicit facial motion space and the distillation loss encouraged the model to learn the accurate lip-sync. Similarly, authors trained PoseVAE with the    -->

*Note: Training details are introduced in [the supplementary material](https://openaccess.thecvf.com/content/CVPR2023/supplemental/Zhang_SadTalker_Learning_Realistic_CVPR_2023_supplemental.pdf).*

**Results:** The authors trained SadTalker on VoxCeleb1 with 8 NVIDIA A100 GPUs and tested it on HDTF dataset. Compared with other competitors, it generated a better head motion and more realistic face. But its lip-sync is bad than other methods.

<!-- The authors evaluated xxx on xxx. Compared with xxx, xxx is better on xxx. But it is worse than xxx on xxx. It is because that xxx. -->

**Why it matters:** This study demonstrated that an explicit 3D face model was a more accurate intermediate representation of the facial characteristics than previous methods. Additionally, the use of VAE models for estimating head pose from audio was shown to improve the naturalness of the synthesis videos. These findings have the potential to enhance the quality of talking-face pipelines for machine learning researchers.

<!-- This work reveals that xxx but xxx. Such insights deepen our understanding of xxx and can help practitioners explain their outputs. -->

**We're thinking:** Instead of using Wav2Lip as a teacher model in ExpNet training, can we use Wav2Lip as ExpNet directly? The 3D-aware face render should have similar capabilities to face vid2vid, allowing for fine-tuning of the render with 10~30s video clips of a target person to improve lip-sync results.

*Note: Few-shot learning is widely studied in deep generation models. Details can refer to [fs-vid2vid, NeurIPS'19, NVIDIA](https://nvlabs.github.io/few-shot-vid2vid/) and [face-few-shot, ICCV'19, Samsung AI](https://openaccess.thecvf.com/content_ICCV_2019/papers/Zakharov_Few-Shot_Adversarial_Learning_of_Realistic_Neural_Talking_Head_Models_ICCV_2019_paper.pdf).*