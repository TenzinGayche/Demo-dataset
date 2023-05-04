
# ziping wav file to wav.tar.gz


import tarfile
import os.path

source_dir = 'wav1'
output_filename = 'wav.tar.gz'
def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

#extracting wav.tar.gz to wav file
def extract_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "r:gz") as tar:
        tar.extractall(source_dir)

extract_tarfile(output_filename, source_dir)