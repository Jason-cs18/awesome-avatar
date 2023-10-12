# A Microbenchmark for Talking-Face Synthesis
### [**Dataset**](https://drive.google.com/drive/folders/1vBse3rgHd3JfTGNFXC-oUZs5DR9B5Mep?usp=sharing) | [**Website**](https://jason-cs18.github.io/awesome-avatar/benchmarks/)

This repository contains the datasets and testing scripts for talking-face synthesis.

> A microbenchmark serves as a valuable tool for researchers to conduct speedy evaluations of new algorithms. This repository can be easily customized and applied to diverse audio-visual talking-face datasets.

### Datasets
In this benchmark, we collect 3 videos for English speakers and 3 videos for Chinese speakers.

<!-- <img src="https://github.com/Jason-cs18/awesome-avatar/blob/main/benchmarks/assets/file_structure.png"/>

![File Structure](https://github.com/Jason-cs18/awesome-avatar/blob/main/benchmarks/assets/file_structure.png "Magic Gardens") -->

<!-- ![](https://github.com/Jason-cs18/awesome-avatar/blob/main/benchmarks/assets/file_structure.png) -->

#### File Structure
```
├── driving_audios
| ├── [9.3M] may_english_audio.aac
| ├── [3.3M] macron_english_trim_audio.aac
| ├── [3.5M] obama1_english_audio.aac
| ├── [780K] laoliang_chinese_50s_audio.mp3
| ├── [4.3M] luoxiang_chinese_audio.mp3
| ├── [8.9M] zuijiapaidang_chinese_audio.mp3
├── source_images
| ├── [294K] may.png
| ├── [202K] macron.png
| ├── [213M] obama1.png
| ├── [206K] zuijiapaidang.png
| ├── [175K] luoxiang.png
| ├── [204K] laoliang.png
├── reference_videos
│ ├── [56M] obama1_english.mp4, 03:38.16, 25fps, 450x450, 46 sentences
│ ├── [96M] may_english.mp4, 04:02.97, 25fps, 512x512, 35 sentences
│ ├── [24M] macron_english_trim.mp4, 00:03:31.92, 25fps, 512x512, 49 sentences
│ ├── [3.6M] laoliang_chinese_50s.mp4, 00:00:49.85, 30fps, 410x380, 40 sentences
│ ├── [14M] luoxiang_chinese.mp4, 04:40.01, 25fps, 350x500, 32 sentences
│ ├── [28M] zuijiapaidang_chinese.mp4, 09:41.98, 30fps, 460x450, 85 sentences
```

<table>
	<tr>
	    <th colspan="3"><center>English Speakers</center></th>
    	<tr>
	    	<td ><center>obama1_english.mp4</center></td>
	    	<td><center>may_english.mp4</center></td>
        	<td><center>macron_english.mp4</center></td>
		</tr >
    </tr >
    	<tr>
	    	<td><iframe src="https://drive.google.com/file/d/1g-T1nvL0KqBkInIRVSSbOvmC1LiCB36o/preview"></iframe></td>
	    	<td><iframe src="https://drive.google.com/file/d/1UMQZP7j8ORLJpHYiUMc-FexDp_SX7386/preview"></iframe></td>
        	<td><iframe src="https://drive.google.com/file/d/1ReG45fm8wnz_a3ZJ3qOhPJGgS8LywKaS/preview"></iframe></td>
		</tr >
    <tr>
	    <th colspan="3"><center>Chinese Speakers</center></th>
    	<tr>
	    	<td ><center>laoliang_chinese.mp4</center></td>
	    	<td><center>luoxiang_chinese.mp4</center></td>
	    	<td><center>zuijiapaidang_chinese.mp4</center></td>
		</tr >
    </tr >
    	<tr>
	    	<td><iframe src="https://drive.google.com/file/d/1jk9gX2R7KcD_Q2WF-zs7e2Es3lfKBCpK/preview"></iframe></td>
	    	<td><iframe src="https://drive.google.com/file/d/1d1haMYyA9mH0Wc1NgkEAuHtk30KpLJME/preview"></iframe></td>
        	<td><iframe src="https://drive.google.com/file/d/1H-DhAj2K8EESbCUWvr6ylcUqKIFVJ94k/preview"></iframe></td>
		</tr >
</table>

### Benchmark
To measure the performance of Wav2Lip and SadTalker, we run them on all videos and testing with the following metrics: 
- **Sync↑**: The confidence score from SyncNet (lip-sync);
- **PSNR↑**: Peak signal-to-noise ratio (identity-preserving);
- **SSIM↑**: Structural similarity for image (identity-preserving);
- **FID↓**: Frchet inception distance (image quality);

### Implementation (off-the-shelf tools)
1. Sync: [syncnet_python](https://github.com/joonson/syncnet_python) ![Github stars](https://img.shields.io/github/stars/joonson/syncnet_python.svg) 
2. PSNR, SSIM: [ffmpeg-quality-metrics](https://github.com/slhck/ffmpeg-quality-metrics) ![Github stars](https://img.shields.io/github/stars/slhck/ffmpeg-quality-metrics.svg) 
3. FID, ~~IS~~: [IQA-PyTorch](https://github.com/chaofengc/IQA-PyTorch) ![Github stars](https://img.shields.io/github/stars/chaofengc/IQA-PyTorch.svg)  


### Qualitative Results for One-shot Pipelines


<table>
	<tr>
	    <th colspan="3"><center>English Speakers</center></th>
    	<tr>
	    	<td ><center>obama1_Wav2Lip.mp4<br><b>PSNR:</b> 32.287, <b>SSIM:</b> 0.951, <b>FID:</b> 18.993</center></td>
	    	<td><center>may_Wav2Lip.mp4<br><b>PSNR:</b> 32.572, <b>SSIM:</b> 0.936, <b>FID:</b> 33.941</center></td>
        	<td><center>macron_Wav2Lip.mp4<br><b>PSNR:</b> 35.737, <b>SSIM:</b> 0.969, <b>FID:</b> 6.121</center></td>
		</tr >
    </tr >
	<tr>
    	<tr>
	    	<td><iframe src="https://drive.google.com/file/d/159jlICcQEs5A-_bxnH752fjL49P4uzuw/preview"></iframe></td>
	    	<td><iframe src="https://drive.google.com/file/d/195V0U8rjnce4aujAI2AZhpCwqKddXHGA/preview"></iframe></td>
        	<td><iframe src="https://drive.google.com/file/d/1Z0bIbqmVgNdECxgYLedUPVpW6uwquE1z/preview"></iframe></td>
		</tr >
    </tr >
    <tr>
	    <th colspan="3"><center>Chinese Speakers</center></th>
    	<tr>
	    	<td ><center>laoliang_Wav2Lip.mp4<br><b>PSNR:</b> 31.444, <b>SSIM:</b> 0.939, <b>FID:</b> 19.192</center></td>
	    	<td><center>luoxiang_Wav2Lip.mp4<br><b>PSNR:</b> 34.367, <b>SSIM:</b> 0.971, <b>FID:</b> 23.631</center></td>
	    	<td><center>zuijiapaidang_Wav2Lip.mp4<br><b>PSNR:</b> 20.364, <b>SSIM:</b> 0.783, <b>FID:</b> 49.04</center></td>
		</tr >
		<tr>
	    	<td><iframe src="https://drive.google.com/file/d/1SKfceJZ_142bETjqc-FyCtem-SSFlWI4/preview"></iframe></td>
	    	<td><iframe src="https://drive.google.com/file/d/15Dt0-5rRbWiYDW4GuzfZGxK8ndjk2MOy/preview"></iframe></td>
        	<td><iframe src="https://drive.google.com/file/d/12iFMIexJkpG9dDmatfFD9yd-LG-bk1dw/preview"></iframe></td>
		</tr >
    </tr >
</table>

<table>
	<tr>
	    <th colspan="3"><center>English Speakers</center></th>
    	<tr>
	    	<td ><center>obama1_SadTalker.mp4<br><b>PSNR:</b> 20.587, <b>SSIM:</b> 0.754, <b>FID:</b> 24.051</center></td>
	    	<td><center>may_SadTalker.mp4<br><b>PSNR:</b> 19.211, <b>SSIM:</b> 0.701, <b>FID:</b> 46.182</center></td>
        	<td><center>macron_SadTalker.mp4<br><b>PSNR:</b> 18.729, <b>SSIM:</b> 0.763, <b>FID:</b> 98.982</center></td>
		</tr >
    </tr >
	<tr>
    	<tr>
	    	<td><iframe src="https://drive.google.com/file/d/1xw0gsxCIGJOKpdAudHM1M5mc7qFaQnBv/preview"></iframe></td>
	    	<td><iframe src="https://drive.google.com/file/d/1wAFcDyK_Yma4pBHNQZAUJzWEzIsL6rS0/preview"></iframe></td>
        	<td><iframe src="https://drive.google.com/file/d/1y8NmIkXmgCXYKXxJKAEhYwjsh1LSiTiq/preview"></iframe></td>
		</tr >
    </tr >
    <tr>
	    <th colspan="3"><center>Chinese Speakers</center></th>
    	<tr>
	    	<td ><center>laoliang_SadTalker.mp4<br><b>PSNR:</b> 18.536, <b>SSIM:</b> 0.672, <b>FID:</b> 52.362</center></td>
	    	<td><center>luoxiang_SadTalker.mp4<br><b>PSNR:</b> 14.363, <b>SSIM:</b> 0.598, <b>FID:</b> 104.221</center></td>
	    	<td><center>zuijiapaidang_SadTalker.mp4<br><b>PSNR:</b> 17.359, <b>SSIM:</b> 0.725, <b>FID:</b> 4.781</center></td>
		</tr >
		<tr>
	    	<td><iframe src="https://drive.google.com/file/d/1i5fu_iYkg98a6vRvPw7tg8Z2mRvp4PV3/preview"></iframe></td>
	    	<td><iframe src="https://drive.google.com/file/d/1Ln5WBpa2PMWT0vDMfB0M_Una_o5j2QL3/preview"></iframe></td>
        	<td><iframe src="https://drive.google.com/file/d/1m8itAbvVVi5kx67_00mUo7vpTGs0gwpw/preview"></iframe></td>
		</tr >
    </tr >
</table>

### Quantitative Results for One-shot Pipelines

<table>
	<tr>
	    <th colspan="5"><center>English Speakers</center></th> <th colspan="5"><center>Chinese Speakers</center></th>
    	<tr>
	    	<td >Pipeline</td>
	    	<td>Sync↑</td>
	    	<td>PSNR↑</td>
        	<td>SSIM↑</td>
			<td>FID↓</td>
			<td >Pipeline</td>
	    	<td>Sync↑</td>
	    	<td>PSNR↑</td>
        	<td>SSIM↓</td>
			<td>FID↓</td>
		</tr >
		<tr>
	    	<td >Wav2Lip</td>
	    	<td>xxx</td>
	    	<td>33.532</td>
        	<td>0.952</td>
			<td>19.685</td>
        	<!-- <td>xxx</td> -->
	    	<td >Wav2Lip</td>
			<td>xxx</td>
	    	<td>28.725</td>
        	<td>0.897</td>
			<td>30.621</td>
        	<!-- <td>xxx</td> -->
		</tr >
		<tr>
	    	<td >SadTalker</td>
	    	<td>xxx</td>
	    	<td>19.509</td>
        	<td>0.739</td>
			<td>56.407</td>
        	<!-- <td>xxx</td> -->
	    	<td >SadTaler</td>
	    	<td>xxx</td>
	    	<td>16.753</td>
        	<td>0.665</td>
			<td>68.120</td>
        	<!-- <td>xxx</td> -->
		</tr >
	</tr>
</table>


*Because NeRF based renderers (GeneFace and ER-NeRF) are person-dependent, we train them on the first 3 minutes of marcon and zuijiapaidang respectively.*


### Qualitative Results for Few-shot Pipelines

<table>
	<tr>
	    <th colspan="2"><center>English Speakers</center></th>
    	<tr>
	    	<td >marcon_GeneFace.mp4</td>
	    	<td>macron_ER-NeRF.mp4</td>
		</tr >
    <tr>
	    <th colspan="2"><center>Chinese Speakers</center></th>
    	<tr>
	    	<td >zuijiapaidang_GeneFace.mp4</td>
	    	<td>zuijiapaidang_ER-NeRF.mp4</td>
		</tr >
    </tr >
</table>


### Quantitative Results for Few-shot Pipelines


<table>
	<tr>
	    <th colspan="6"><center>marcon (English)</center></th><th colspan="6"><center>zuijiapaidang (Chinese)</center></th>
    	<tr>
	    	<td >Pipeline</td>
	    	<td>Sync↑</td>
	    	<td>PSNR↑</td>
        	<td>SSIM↓</td>
			<td>FID↓</td>
        	<td>IS↑</td>
			<td >Pipeline</td>
	    	<td>Sync↑</td>
	    	<td>PSNR↑</td>
        	<td>SSIM↓</td>
			<td>FID↓</td>
        	<td>IS↑</td>
		</tr >
		<tr>
	    	<td >GeneFace</td>
	    	<td>xxx</td>
	    	<td>xxx</td>
        	<td>xxx</td>
			<td>xxx</td>
        	<td>xxx</td>
	    	<td >GeneFace</td>
	    	<td>xxx</td>
	    	<td>xxx</td>
        	<td>xxx</td>
			<td>xxx</td>
        	<td>xxx</td>
		</tr >
		<tr>
	    	<td >ER-NeRF</td>
	    	<td>xxx</td>
	    	<td>xxx</td>
        	<td>xxx</td>
			<td>xxx</td>
        	<td>xxx</td>
	    	<td >ER-NeRF</td>
	    	<td>xxx</td>
	    	<td>xxx</td>
        	<td>xxx</td>
			<td>xxx</td>
        	<td>xxx</td>
		</tr >
</table>


## External Links
1. [Extract Frames using FFmpeg: A Comprehensive Guide](https://ottverse.com/extract-frames-using-ffmpeg-a-comprehensive-guide/)
2. [Whisper Web: ML-powered speech recognition directly in your browser](https://huggingface.co/spaces/Xenova/whisper-web)
3. [moviepy.video.fx.all.crop](https://zulko.github.io/moviepy/ref/videofx/moviepy.video.fx.all.crop.html)
4. [Trim Video: Trim or cut video of any format](https://online-video-cutter.com/)