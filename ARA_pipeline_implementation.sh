# ARA pipeline implementation script #

## Requirements ##
# Docker or Mamba, unfinished

## Installation ##
# Using docker
cd ARA-main/
docker build -t ara_img .

# Docker usage example
docker run -it ara_img /home/ARA-main/ara.pl --input /home/ARA-main/example/SraRunInfo.csv --sequences /home/ARA-main/example/Arabidopsis_thaliana.TAIR10.ncrna.fa
