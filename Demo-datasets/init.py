
# ziping wav file to wav.tar.gz


import tarfile
import os.path
from datasets import DownloadManager

source_dir = '/Users/tenzingayche/Downloads/wav 2'
output_filename = 'wav.tar'
def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

#extracting wav.tar.gz to wav file
def extract_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "r:gz") as tar:
        tar.extractall(source_dir)
_url='https://github.com/TenzinGayche/Demo-dataset/raw/master/wav.tar.gz'
# dl_manager = DownloadManager()
# a=dl_manager.download_and_extract(_url)
# print(a)
# os.listdir(a)
make_tarfile(output_filename, source_dir)
