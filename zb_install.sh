#!/bin/bash

# Update the system
echo "updating the system"
sudo apt-get update

# Install packages
echo "installing htop and screen"
sudo apt install -y htop
sudo apt install -y screen

# Install Miniconda
echo "installing miniconda"
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash

# Start Jupyter setup
echo "Setup complete. Now starting on Jupyter setup"
eval "$(cat ~/.bashrc | tail -n +10)"
#source ~/.bashrc

# Create and enter the environment
conda create -y --name env python=3.9 
conda activate env

# Install Jupyter Notebook
conda install -y -c conda-forge notebook
conda install -y -c conda-forge nb_conda_kernels
conda install -y nb_conda
echo "Finished installing all Jupyter notebook stuff"

# Export environment to requirements.yml
conda list --export > requirements.yml


