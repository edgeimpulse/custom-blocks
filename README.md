# Custom Blocks

Custom blocks let you extend Edge Impulse Studio with your own transformation, synthetic data, labeling, processing, learning, and deployment steps. See the [custom blocks documentation](https://docs.edgeimpulse.com/docs/edge-impulse-studio/organizations/custom-blocks) to learn how they work.

This page lists the public custom block example repositories in this GitHub organization. Block collections bundle several related blocks in one repository, and individual blocks are grouped by type below.

<!-- Generated from blocks.json by scripts/generate-readme.py. Do not edit by hand. -->

## Block collections

| Block | Description |
| --- | --- |
| [custom-blocks-akida](https://github.com/edgeimpulse/custom-blocks-akida) | Edge Impulse custom blocks - giving early access to train and deploy akida spiking NNs |
| [deployment-blocks-syntiant](https://github.com/edgeimpulse/deployment-blocks-syntiant) | Examples of how to create a custom deployment block for Syntiant hardware |
| [learning-blocks-sklearn-linear-models](https://github.com/edgeimpulse/learning-blocks-sklearn-linear-models) |  |
| [processing-blocks](https://github.com/edgeimpulse/processing-blocks) | Signal processing blocks |
| [transformation-blocks](https://github.com/edgeimpulse/transformation-blocks) | Repository that contains transformation blocks examples |

## Individual blocks

### Deployment blocks

| Block | Description |
| --- | --- |
| [deployment-block-gradcam](https://github.com/edgeimpulse/deployment-block-gradcam) |  |
| [deployment-block-multi-impulse](https://github.com/edgeimpulse/deployment-block-multi-impulse) | Merge multiple impulses |
| [deployment-block-python](https://github.com/edgeimpulse/deployment-block-python) | Example repository for https://docs.edgeimpulse.com/docs/edge-impulse-studio/organizations/custom-blocks/deployment-blocks |
| [deployment-block-ros2](https://github.com/edgeimpulse/deployment-block-ros2) | Clone Repo & Inject Edge Impulse Model |

### Labeling blocks

| Block | Description |
| --- | --- |
| [labeling-block-audio-spectrogram-transformer](https://github.com/edgeimpulse/labeling-block-audio-spectrogram-transformer) | Label audio samples automatically with Audio Spectrogram Transformer (AST) model fine-tuned on AudioSet. |
| [labeling-block-bounding-box-relabeling-gpt4o](https://github.com/edgeimpulse/labeling-block-bounding-box-relabeling-gpt4o) | Relabel bounding boxes using an LLM |
| [labeling-block-bounding-box-validation-gpt4o](https://github.com/edgeimpulse/labeling-block-bounding-box-validation-gpt4o) | AI labeling block that uses GPT-4o to disable samples which do not conform to provided validation prompts. |
| [labeling-block-existing-ei-project](https://github.com/edgeimpulse/labeling-block-existing-ei-project) |  |
| [labeling-block-images-gpt4o](https://github.com/edgeimpulse/labeling-block-images-gpt4o) | WIP Labeling using ChatGPT |
| [labeling-block-zero-shot-object-detector-astra](https://github.com/edgeimpulse/labeling-block-zero-shot-object-detector-astra) |  |
| [labeling-block-zero-shot-object-detector-owl-vit](https://github.com/edgeimpulse/labeling-block-zero-shot-object-detector-owl-vit) | Zero shot object detector AI Labeling |

### Learning blocks

| Block | Description |
| --- | --- |
| [learning-block-autoencoder-ad](https://github.com/edgeimpulse/learning-block-autoencoder-ad) | A 1D convolutional autoencoder anomaly detection custom learning block for Edge Impulse |
| [learning-block-catboost](https://github.com/edgeimpulse/learning-block-catboost) |  |
| [learning-block-efficientnet](https://github.com/edgeimpulse/learning-block-efficientnet) | EfficientNet transfer learning block for Edge Impulse |
| [learning-block-keras](https://github.com/edgeimpulse/learning-block-keras) | Custom Keras ML block example for Edge Impulse |
| [learning-block-lgbm](https://github.com/edgeimpulse/learning-block-lgbm) |  |
| [learning-block-mobilenet-ssd](https://github.com/edgeimpulse/learning-block-mobilenet-ssd) |  |
| [learning-block-pytorch](https://github.com/edgeimpulse/learning-block-pytorch) | Custom PyTorch ML block example for Edge Impulse |
| [learning-block-rl-core](https://github.com/edgeimpulse/learning-block-rl-core) |  |
| [learning-block-scikit](https://github.com/edgeimpulse/learning-block-scikit) | Scikit learn block |
| [learning-block-sklearn-linear-models](https://github.com/edgeimpulse/learning-block-sklearn-linear-models) |  |
| [learning-block-sklearn-random-forest](https://github.com/edgeimpulse/learning-block-sklearn-random-forest) |  |
| [learning-block-svm](https://github.com/edgeimpulse/learning-block-svm) |  |
| [learning-block-tao-pyt](https://github.com/edgeimpulse/learning-block-tao-pyt) |  |
| [learning-block-tao-tf1](https://github.com/edgeimpulse/learning-block-tao-tf1) |  |
| [learning-block-xgboost](https://github.com/edgeimpulse/learning-block-xgboost) |  |
| [learning-block-yolov5](https://github.com/edgeimpulse/learning-block-yolov5) | YOLOv5 transfer learning model for Edge Impulse |
| [learning-block-yolov5-drpai](https://github.com/edgeimpulse/learning-block-yolov5-drpai) | YOLOv5 transfer learning model for Edge Impulse running on Renesas DRP-AI |

### Processing blocks

| Block | Description |
| --- | --- |
| [processing-block-c-cpp](https://github.com/edgeimpulse/processing-block-c-cpp) | Example of a custom processing block in c/cpp |
| [processing-block-cpp](https://github.com/edgeimpulse/processing-block-cpp) | Example DSP block in C++ |
| [processing-block-edge-detection](https://github.com/edgeimpulse/processing-block-edge-detection) | Processing block for Edge detection in images |
| [processing-block-matlab](https://github.com/edgeimpulse/processing-block-matlab) | Example of a custom processing block in Matlab |
| [processing-block-octave](https://github.com/edgeimpulse/processing-block-octave) | Example of a custom processing block using Octave |
| [processing-block-posenet](https://github.com/edgeimpulse/processing-block-posenet) |  |
| [processing-block-python](https://github.com/edgeimpulse/processing-block-python) | Example of a custom processing block in Python |
| [processing-block-spectral](https://github.com/edgeimpulse/processing-block-spectral) | Example of a custom DSP block with C++ implementation |

### Synthetic data blocks

| Block | Description |
| --- | --- |
| [synthetic-data-block-anglenorm](https://github.com/edgeimpulse/synthetic-data-block-anglenorm) | AngleForge — Edge Impulse custom synthetic data block that normalises image camera angles for a consistent dataset, powered by the Qwen-Image-Edit multi-angle model on Hugging Face. |
| [synthetic-data-block-astra](https://github.com/edgeimpulse/synthetic-data-block-astra) |  |
| [synthetic-data-block-dall-e](https://github.com/edgeimpulse/synthetic-data-block-dall-e) | Use the Dall-E API to generate an image dataset |
| [synthetic-data-block-flux-pro](https://github.com/edgeimpulse/synthetic-data-block-flux-pro) | Use Flux-pro via Replicate's API to generate very realistic images for synthetic data |

### Transformation blocks

| Block | Description |
| --- | --- |
| [transformation-block-image-resize](https://github.com/edgeimpulse/transformation-block-image-resize) | This transformation block resizes all images in an Edge Impulse project using the same methods as in edge_impulse_linux. |
| [transformation-block-mix-audio-noise-background](https://github.com/edgeimpulse/transformation-block-mix-audio-noise-background) | Transformation block that mixes custom background noise into audio files |
| [transformation-block-mix-audio-noise-snr](https://github.com/edgeimpulse/transformation-block-mix-audio-noise-snr) | Synthetic data block to mix noise to audio files with SNR targets |
| [transformation-block-python](https://github.com/edgeimpulse/transformation-block-python) | A template transformation block in Python |
| [transformation-block-text-to-speech](https://github.com/edgeimpulse/transformation-block-text-to-speech) | Use Google text-to-speech API to generate new keywords |
| [transformation-block-whisper-keywords](https://github.com/edgeimpulse/transformation-block-whisper-keywords) |  |
