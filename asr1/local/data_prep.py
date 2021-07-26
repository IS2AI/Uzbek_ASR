#!/usr/bin/env python
import sys, argparse, re, os, random, glob
import pandas as pd
from pathlib import Path
import wave
import contextlib

seed=1234

def get_args():
    parser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--dataset_dir", help="Input data directory", required=True)
    print(' '.join(sys.argv))
    args = parser.parse_args()
    return args


def get_duration(file_path):
    duration = None
    if os.path.exists(file_path) and Path(file_path).stat().st_size > 0:
        with contextlib.closing(wave.open(file_path,'r')) as f:
            frames = f.getnframes()
            if frames>0:
                rate = f.getframerate()
                duration = frames / float(rate)
    return duration if duration else 0

def get_text(dataset_dir, file):
    txt_file = os.path.join(dataset_dir, file + '.txt') 
    with open(txt_file, 'r', encoding='utf-8') as f:
        return f.read().strip()

def prepare_data(dataset_dir, path_root):
    total_duration = 0
    wav_format = '-r 16000 -c 1 -b 16 -t wav - downsample |'
    
    files = [os.path.basename(x).replace('.wav', '') for x in glob.glob(dataset_dir + '/*.wav')]
    files.sort()
    with open(path_root + '/text', 'w', encoding="utf-8") as f1, \
    open(path_root + '/utt2spk', 'w', encoding="utf-8") as f2, \
    open(path_root + '/wav.scp', 'w', encoding="utf-8") as f3:
        for filename in files:
            wav_path = os.path.join(dataset_dir, filename + '.wav') 
            total_duration += get_duration(wav_path) 
            transcription = get_text(dataset_dir, filename)
            f1.write(filename + ' ' + transcription + '\n')
            f2.write(filename + ' ' + filename + '\n')
            f3.write(filename + ' sox ' + wav_path  + ' ' + wav_format +  '\n') 
            
    return total_duration / 3600

def main():
    args = get_args()
    
    dataset_dir = args.dataset_dir
    
    train = []
    dev = []
    test = []
    train_dir_name = 'train'
    dev_dir_name = 'dev'
    test_dir_name = 'test'
    
    save_data_root = 'data/'
    
    train_root = save_data_root + train_dir_name
    dev_root = save_data_root + dev_dir_name
    test_root = save_data_root + test_dir_name
    
    train_dir = os.path.join(dataset_dir, train_dir_name)
    print('duration of train data:', prepare_data(train_dir, train_root))
        
    dev_dir = os.path.join(dataset_dir, dev_dir_name)
    print('duration of dev data:', prepare_data(dev_dir, dev_root))
        
    test_dir = os.path.join(dataset_dir, test_dir_name)
    print('duration of test data:', prepare_data(test_dir, test_root))

if __name__ == "__main__":
    main()
