## SadTalker: Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation
A VAE-based posenet is integrated with a new talking-face generation pipeline SadTalker to generate diverse head motions on talking-face videos.

![SadTalker overview](https://github.com/Jason-cs18/awesome-avatar/blob/main/assets/sadtalker.png "SadTalker overview")

**What's new:** Wenxuan Zhang from Xi'an Jiaotong University and researchers from Tencent AI Lab released a new generation pipeline named SadTalker to synthesis diverse and stylized talking-face videos.

**Key insights:** Previous works leveraged facial landmarks and keypoints as the intermediate facial representation and were hard to disentangle expression and motion learning. To overcome this issue, SadTalker leveraged a explict 3D face model to decouple representations of expression and head motions. To achieve this goal, the authors designed PoseVAE and ExpNet to learn audio2expression and audio2pose respectively.

<!-- Previous works leverages xxx to achieve xxx but they are limited by xxx. To overcome xxx, authors designed xxx. -->

**How it works:** As shown in the Figure 2, the authors designed a three-stage inference pipeline to synthesize stylized talking-face videos. 
- They first levraged the recent single image deep 3D reconstruction method to extract the 3D face model on the target image, which consists of identity coefficients, expression coefficients and head pose (rotation and translation).
- In the second, they estimated pose and expression coefficients by PoseVAE and ExpNet respectively. Afterwards, they got a motion flow on 3D facial space. During training, the authors used the reconstruction loss and distillation loss to encourage ExpNet to learn the accurate mapping on the whole facial motion and the lip moion resepectively. Similarly, they used the reconstruction loss and KL-divergence loss to encourage PoseVAE to learn accurate and diverse head motions resepectively.
- In the third, they leveraged a modified face vid2vid model to render real face from the estimated 3D facial motion. In training, they first trained face vid2vid in a self-supervised fashion. Then they fine-tune the customized mappingNet in a reconstruction style.
<!-- - they trained ExpNet with the reconstruction loss and distillation loss. The reconstruction loss encouraged the model to learn the accurate mapping in explicit facial motion space and the distillation loss encouraged the model to learn the accurate lip-sync. Similarly, authors trained PoseVAE with the    -->

*Note: Training details are introduced in [the supplementary material](https://openaccess.thecvf.com/content/CVPR2023/supplemental/Zhang_SadTalker_Learning_Realistic_CVPR_2023_supplemental.pdf).*

**Results:** The authors trained SadTalker on VoxCeleb1 with 8 NVIDIA A100 GPUs and tested it on HDTF dataset. Compared with other competitors, it generated a better head motion and more realistic face. But its lip-sync is bad than many other methods.

<!-- The authors evaluated xxx on xxx. Compared with xxx, xxx is better on xxx. But it is worse than xxx on xxx. It is because that xxx. -->

**Why it matters:** This work evaluated a explict 3D face model was a better intermediate facial representation and VAE could be used for estimating head pose from audio. Such insights can help ML researchers build a better and personalized talking-face pipeline.

<!-- This work reveals that xxx but xxx. Such insights deepen our understanding of xxx and can help practitioners explain their outputs. -->

**We're thinking:** Instead of using Wav2Lip as a techer model in ExpNet training, can we use Wav2Lip as ExpNet naively? The 3D-aware face render should have few-shot learning capabilities as same as face vid2vid. With this, we can fine-tune the render with 10~30s video clips of a target person to improve lip-sync results in further.

*Note: Few-shot learning is widely studied in deep generation models. Details can refer to [fs-vid2vid, NeurIPS'19, NVIDIA](https://nvlabs.github.io/few-shot-vid2vid/) and [face-few-shot, ICCV'19, Samsung AI](https://openaccess.thecvf.com/content_ICCV_2019/papers/Zakharov_Few-Shot_Adversarial_Learning_of_Realistic_Neural_Talking_Head_Models_ICCV_2019_paper.pdf).*