# A Microbenchmark for Talking-Face Synthesis
### [**Google Drive**](https://drive.google.com/drive/folders/1vBse3rgHd3JfTGNFXC-oUZs5DR9B5Mep?usp=sharing) | [**Website**](https://jason-cs18.github.io/awesome-avatar/benchmarks/) | [**Code**](https://github.com/Jason-cs18/awesome-avatar/tree/main/benchmarks)

This repository contains the datasets and testing scripts for talking-face synthesis.

> A microbenchmark serves as a valuable tool for researchers to conduct speedy evaluations of new algorithms. This repository can be easily customized and applied to diverse audio-visual talking-face datasets.

### Datasets
In this benchmark, we collect 4 videos for English speakers and 3 videos for Chinese speakers.

<!-- <img src="https://github.com/Jason-cs18/awesome-avatar/blob/main/benchmarks/assets/file_structure.png"/>

![File Structure](https://github.com/Jason-cs18/awesome-avatar/blob/main/benchmarks/assets/file_structure.png "Magic Gardens") -->

<!-- ![](https://github.com/Jason-cs18/awesome-avatar/blob/main/benchmarks/assets/file_structure.png) -->

#### File Structure
>  ```
>  ├── driving audios
>  ├── source image
>  ├── reference videos
>  │ ├── [56M] obama1_english.mp4, 03:38.16, 450x450, 46 sentences
>  │ ├── [96M] may_english.mp4, 04:02.97, 512x512, 35 sentences
>  │ ├── [234M] shaheen_english.mp4, 04:28.08, 512x512, 37 sentences
>  │ ├── [146M] macron_english.mp4, 09:30.94, 512x512, 49 sentences
> ```

<table>
	<tr>
	    <th colspan="4"><center>English Speakers</center></th>
    	<tr>
	    	<td >obama1_english.mp4</td>
	    	<td>may_english.mp4</td>
	    	<td>shaheen_english.mp4</td>
        	<td>macron_english.mp4</td>
		</tr >
    </tr >
    	<tr>
	    	<td><iframe src="https://drive.google.com/file/d/1g-T1nvL0KqBkInIRVSSbOvmC1LiCB36o/preview"></iframe></td>
	    	<td><iframe src="https://drive.google.com/file/d/1UMQZP7j8ORLJpHYiUMc-FexDp_SX7386/preview"></iframe></td>
        	<td><iframe src="https://drive.google.com/file/d/1tUU8yRM4mcwEhbuM-rt1MkH-xuYBS2Ar/preview"></iframe></td>
        	<td><iframe src="https://drive.google.com/file/d/1jxu5SqluMDHFxT1R7dP1k4uWHHnnG9RK/preview"></iframe></td>
		</tr >
    <tr>
	    <th colspan="4"><center>Chinese Speakers</center></th>
    	<tr>
	    	<td >xxx.mp4</td>
	    	<td>xxx.mp4</td>
	    	<td>xxx.mp4</td>
        	<td>xxx.mp4</td>
		</tr >
    </tr >
</table>

### Benchmarks
To measure the performance of Wav2Lip and SadTalker, we run them on all videos and testing with the following metrics: 
- **Sync**: The confidence score from SyncNet (lip-sync).
- **PSNR**: Peak Signal-to-Noise Ratio (image quality).
- **SSIM**: Structural similarity for image (image quality).
- **FID**: Frchet Inception Distance (image quality).
- **IS**: Inception score (image quality).

Because NeRF based renderers (GeneFace and ER-NeRF) are person-dependent, we train them on *the first 3 minutes* of marcon and xxx respectively.

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

<table>
	<tr>
	    <th colspan="6"><center>marcon (English)</center></th>
    	<tr>
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
		</tr >
		<tr>
	    	<td >ER-NeRF</td>
	    	<td>xxx</td>
	    	<td>xxx</td>
        	<td>xxx</td>
			<td>xxx</td>
        	<td>xxx</td>
		</tr >
	<tr>
	<tr>
	    <th colspan="6"><center>xxx (Chinese)</center></th>
    	<tr>
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
		</tr >
		<tr>
	    	<td >ER-NeRF</td>
	    	<td>xxx</td>
	    	<td>xxx</td>
        	<td>xxx</td>
			<td>xxx</td>
        	<td>xxx</td>
		</tr >
	<tr>
</table>

### External Links
1. [FFmpeg 101: Top 10 Command Options You Need to Know (with Examples)](https://www.bannerbear.com/blog/ffmpeg-101-top-10-command-options-you-need-to-know-with-examples/)
2. [Whisper Web: ML-powered speech recognition directly in your browser](https://huggingface.co/spaces/Xenova/whisper-web)