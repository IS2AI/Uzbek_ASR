# Uzbek_ASR


This repository provides the recipe for the paper [USC: An Open-Source Uzbek Speech Corpus](https://arxiv.org/abs/2107.14419).

## Authors

The Uzbek speech corpus (USC) has been developed in academic collaboration between ISSAI and [Image and Speech Processing Laboratory, Department of Computer Systems, TUIT](https://tuit.uz/en/kompyuter-tizimlari). 

**Authors:**
- Muhammadjon Musaev;
- Saida Mussakhojayeva;
- Ilyos Khujayorov;
- Yerbolat Khassanov;
- Mannon Ochilov;
- Huseyin Atakan Varol;

## Setup and Requirements 

Our code builds upon [ESPnet](https://github.com/espnet/espnet), and requires prior installation of the framework. Please follow the [installation guide](https://espnet.github.io/espnet/installation.html) and put the repository inside `espnet/egs/` directory.

After succesfull installation of ESPnet & Kaldi, go to `Uzbek_ASR/asr1` directory and create links to the dependencies:
```
ln -s ../../../tools/kaldi/egs/wsj/s5/steps steps
ln -s ../../../tools/kaldi/egs/wsj/s5/utils utils
```
The directory for running the experiments (`Uzbek_ASR/<exp-name`) can be created by running the following script:

```
./setup_experiment.sh <exp-name>
```

## Downloading the dataset
 
Download [USC dataset](https://issai.nu.edu.kz/uzbek-asr/) and untar in the directory of your choice. Specify the path to the data in  `./run.sh` script:
```
dataset_dir=/path-to/ISSAI_USC
```

## Training

To train the models, run the script `./run.sh` inside `Uzbek_ASR/<exp-name>/` folder.

## Pre-trained model

You can find the link to the latest pre-trained [Conformer model](https://issai.nu.edu.kz/wp-content/uploads/2021/07/model.tar.gz). Untar it in `Uzbek_ASR/<exp-name>/`. 

## Inference
To decode a single audio, specify paths to the following files inside `recog_wav.sh` script:
```
lang_model= path to rnnlm.model.best
cmvn= path to cmvn.ark, for example data/train/cmvn.ark
recog_model= path to e2e model, in case of conformer: model.last10.avg.best 
```
Then, run the following script:
```
./recog_wav.sh <path-to-audio-file>
```
