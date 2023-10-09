# A Microbenchmark for Talking-Face Synthesis
### [**Dataset**](https://drive.google.com/drive/folders/1vBse3rgHd3JfTGNFXC-oUZs5DR9B5Mep?usp=sharing) | [**Website**](https://jason-cs18.github.io/awesome-avatar/benchmarks/) | [**Code**](https://github.com/Jason-cs18/awesome-avatar/tree/main/benchmarks)

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
| ├── [9.3M] may_english.aac
| ├── [9.3M] macron_english.aac
| ├── [3.5M] obama1_english.aac
| ├── [4.6M] laoliang_chinese_audio.mp3
| ├── [4.3M] luoxiang_chinese_audio.mp3
| ├── [8.9M] zuijiapaidang_chinese_audio.mp3
├── source_images
| ├── [294K] may.png
| ├── [202K] macron.png
| ├── [213M] obama1.png
| ├── [206K] zuijiapaidang.png
| ├── [175K] luoxiang.png
| ├── [204K] laoliang.png
├── reference videos
│ ├── [56M] obama1_english.mp4, 03:38.16, 450x450, 46 sentences
│ ├── [96M] may_english.mp4, 04:02.97, 512x512, 35 sentences
│ ├── [146M] macron_english.mp4, 09:30.94, 512x512, 49 sentences
│ ├── [13M] laoliang_chinese.mp4, 04:59.00, 410x380, 40 sentences
│ ├── [14M] luoxiang_chinese.mp4, 04:40.01, 350x500, 32 sentences
│ ├── [28M] zuijiapaidang_chinese.mp4, 09:41.98, 460x450, 85 sentences
```

<table>
	<tr>
	    <th colspan="3"><center>English Speakers</center></th>
    	<tr>
	    	<td >obama1_english.mp4</td>
	    	<td>may_english.mp4</td>
        	<td>macron_english.mp4</td>
		</tr >
    </tr >
    	<tr>
	    	<td><iframe src="https://drive.google.com/file/d/1g-T1nvL0KqBkInIRVSSbOvmC1LiCB36o/preview"></iframe></td>
	    	<td><iframe src="https://drive.google.com/file/d/1UMQZP7j8ORLJpHYiUMc-FexDp_SX7386/preview"></iframe></td>
        	<td><iframe src="https://drive.google.com/file/d/1jxu5SqluMDHFxT1R7dP1k4uWHHnnG9RK/preview"></iframe></td>
		</tr >
    <tr>
	    <th colspan="3"><center>Chinese Speakers</center></th>
    	<tr>
	    	<td >laoliang_chinese.mp4</td>
	    	<td>luoxiang_chinese.mp4</td>
	    	<td>zuijiapaidang_chinese.mp4</td>
		</tr >
    </tr >
    	<tr>
	    	<td><iframe src="https://drive.google.com/file/d/1iBGa6_x4bhfnWblEPtL3NbQwULQdNXCq/preview"></iframe></td>
	    	<td><iframe src="https://drive.google.com/file/d/1d1haMYyA9mH0Wc1NgkEAuHtk30KpLJME/preview"></iframe></td>
        	<td><iframe src="https://drive.google.com/file/d/1H-DhAj2K8EESbCUWvr6ylcUqKIFVJ94k/preview"></iframe></td>
		</tr >
</table>

### Benchmark
To measure the performance of Wav2Lip and SadTalker, we run them on all videos and testing with the following metrics: 
- **Sync**: The confidence score from SyncNet (lip-sync).
- **PSNR**: Peak Signal-to-Noise Ratio (image quality).
- **SSIM**: Structural similarity for image (image quality).
- **FID**: Frchet Inception Distance (image quality).
- **IS**: Inception score (image quality).

### Qualitative Results for One-shot Pipelines

<table>
	<tr>
	    <th colspan="2"><center>English Speakers</center></th>
    	<tr>
	    	<td >marcon_Wav2Lip.mp4</td>
	    	<td>may_Wav2Lip.mp4</td>
        	<td>macron_Wav2Lip.mp4</td>
		</tr >
    </tr >
    <tr>
	    <th colspan="3"><center>Chinese Speakers</center></th>
    	<tr>
	    	<td >laoliang_Wav2Lip.mp4</td>
	    	<td>luoxiang_Wav2Lip.mp4</td>
	    	<td>zuijiapaidang_Wav2Lip.mp4</td>
		</tr >
    </tr >
</table>

<table>
	<tr>
	    <th colspan="3"><center>English Speakers</center></th>
    	<tr>
	    	<td >obama1_SadTalker.mp4</td>
	    	<td>may_SadTalker.mp4</td>
        	<td>macron_SadTalker.mp4</td>
		</tr >
    </tr >
    <tr>
	    <th colspan="3"><center>Chinese Speakers</center></th>
    	<tr>
	    	<td >laoliang_SadTalker.mp4</td>
	    	<td>luoxiang_SadTalker.mp4</td>
	    	<td>zuijiapaidang_SadTalker.mp4</td>
		</tr >
    </tr >
</table>

### Quantitative Results for One-shot Pipelines
<table>
	<tr>
	    <th colspan="6"><center>English Speakers</center></th> <th colspan="6"><center>Chinese Speakers</center></th>
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
    </tr >
		<tr>
	    	<td >Wav2Lip</td>
	    	<td>xxx</td>
	    	<td>xxx</td>
        	<td>xxx</td>
			<td>xxx</td>
        	<td>xxx</td>
	    	<td >Wav2Lip</td>
	    	<td>xxx</td>
	    	<td>xxx</td>
        	<td>xxx</td>
			<td>xxx</td>
        	<td>xxx</td>
		</tr >
		<tr>
	    	<td >SadTalker</td>
	    	<td>xxx</td>
	    	<td>xxx</td>
        	<td>xxx</td>
			<td>xxx</td>
        	<td>xxx</td>
	    	<td >SadTaler</td>
	    	<td>xxx</td>
	    	<td>xxx</td>
        	<td>xxx</td>
			<td>xxx</td>
        	<td>xxx</td>
		</tr >
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

### External Links
1. [Extract Frames using FFmpeg: A Comprehensive Guide](https://ottverse.com/extract-frames-using-ffmpeg-a-comprehensive-guide/)
2. [Whisper Web: ML-powered speech recognition directly in your browser](https://huggingface.co/spaces/Xenova/whisper-web)
3. [moviepy.video.fx.all.crop](https://zulko.github.io/moviepy/ref/videofx/moviepy.video.fx.all.crop.html)
4. [Trim Video: Trim or cut video of any format](https://online-video-cutter.com/)