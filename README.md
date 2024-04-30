# Hello, Welcome to the Enterococcus README!

## Getting Started

* To clone this directory, run the following on the command line:

    `git clone https://github.com/smjablonska/Enterococcus_Repo.git`

* If you do not have Python installed, follow the instructions on this page:

    https://www.python.org/downloads/

* If you do not have R installed, follow the instrutions on this page:

    https://rstudio-education.github.io/hopr/starting.html

* If you do not have Docker installed, follow the instructions on this page:

    https://docs.docker.com/get-docker/

## Make sure you have the following dependencies:

* The following libraries are part of the standard library of Python version 2.7 or later:

    argparse
    
    os

    sys

    csv

* You will need to install the following Python libraries:

    pandas

    matplotlib

    numpy

* You will need the following R packages:

    readr

    stats

    argparse


# Step One: The Automated Record Analysis (ARA) Pipeline

* ARA Pipeline installation should follow the directions on [this GitHub](https://github.com/maurya-anand/ARA/tree/main)

    * We utilize the Docker installation method in this GitHub!!

* After installation of the ARA pipeline, navigate to the ARA-main folder in your directory

    * Make an image using the following command:

        `docker build -t ara_img .`

* Open the docker terminal with following command, note this is creating a container named ARA_EF:

    `docker run -t -d --name ARA_EF ara_img`

* Call the docker

    `docker exec -it ARA_EF /bin/sh`

* Upload the correct files to the docker

    * You will need the list of SRA numbers of the genomes you are searching against, and the sequences that you are searching for

    * The following example command is copying the list of E. faecalis SRA genomes that we are searching for our phage sequence in

        `docker cp Enterococcus_Run.txt ARA_EF:/home/ARA-main/Enterococcus_Run.txt`

### Once everything is uploaded run ARA pipeline inside docker. Input can be SRA IDS or SRARunInfo and sequences are what you query against. 
```./ara.pl --input /home/ARA-main/Enterococcus_Run.txt --sequences /home/ARA-main/MZ.fa```

### Once results are outputted, copy them to your host directory through the cp command. 

### From docker to host.
```docker cp ARA_EF:/results/. home/user/ARA-main/results```
