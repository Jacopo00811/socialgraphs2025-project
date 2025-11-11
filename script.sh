#!/bin/bash
#BSUB -J SpotifyGraph
#BSUB -q hpc
#BSUB -W 24:00
#BSUB -R "rusage[mem=1024MB]"
#BSUB -o SpotifyGraph_%J.out
#BSUB -e SpotifyGraph_%J.err
#BSUB -R "select[model == XeonGold6126]"
#BSUB -R "span[hosts=1]"
#BSUB -n 4
##BSUB -u s215158@dtu.dk
#BSUB -B 
#BSUB -N 

module load python3/3.11.9
source .venv/bin/activate
python3 Scraper.py