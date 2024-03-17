#!/bin/bash

# download .gz file from encode
wget https://www.encodeproject.org/files/ENCFF986FWM/@@download/ENCFF986FWM.bed.gz
# install gzip
sudo apt-get install gzip
# use gzip to get .bed file
gunzip ENCFF986FWM.bed.gz
# install bedtools (must do all basic package installs on node first for bedtools to work)
sudo apt install bedtools
# make new folder for export
mkdir reference
# use bedtools to convert the narrowpeak file to a nucleotide file
bedtools getfasta -fi /proj/SIUE-CS590-490/reference/hg38.fa -bed /users/ZackB/ENCFF986FWM.bed -fo /users/ZackB/ENCFF986FWM.txt

