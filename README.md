# Hello, Welcome to the Enterococcus README!

Created by: Sandra Jablonska, Grace Chilton, and Ken Sandoval
# Loyola University Of Chicago: Department of Bioinformatics 

![687474703a2f2f7777772e6c75632e6564752f6d656469612f686f6d652f696d616765732f6c6f796f6c612d6c6f676f2d7461672e706e67](https://github.com/smjablonska/Enterococcus_Repo/assets/120067807/6a50791f-9579-4875-972c-1c8c8dbebfa9)

COMP 383: Final Project

Computational Biology | Spring 2024 | Dr. Heather E. Wheeler

## Overview 
 This Repo is dedicated to utilizing the Automated Records Analysis Pipeline to search publicly available Enterococcus faecalis genomes for phages of interest.

This is a diagram depiction of how the Pipeline runs. 

 ![324483509-7a583a39-71cf-4a55-9e5c-70a8fee0a112](https://github.com/smjablonska/Enterococcus_Repo/assets/120067807/ae1ce7a0-e25f-4c28-93ab-ba255c2cc9de)

The goal of this pipeline is to (Leaving off here) 

## Getting Started

* To clone this directory, run the following on the command line:

    `git clone https://github.com/smjablonska/Enterococcus_Repo.git`

* If you do not have Python installed, follow the instructions on this page:

    https://www.python.org/downloads/

* If you do not have R installed, follow the instructions on this page:

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

    * The following example command is copying the list of E. faecalis subsampled SRA genomes that we are searching for our phage sequence in

        `docker cp Enterococcus_Run.txt ARA_EF:/home/ARA-main/Enterococcus_Run.txt`

* Once you have uploaded everything, run the ARA pipeline inside the docker

    * The input can be SRA IDs or the SRARunInfo from NCBI and the sequences that you are using to query these genomes

        `./ara.pl --input /home/ARA-main/Enterococcus_Run.txt --sequences /home/ARA-main/MZ.fa`

* When the pipeline is finished running, copy the results to your directory using the following command:

    `docker cp ARA_EF:/results/. home/user/ARA-main/results`

# Step Two: Filtering and Statistics

* Run the following on the command line in the Enterococcus_Repo directory:

    `python3 wrapper.py -s MZ.screening.analysis.stats.sorted.by.alignment.txt`

    ```
    -s, --screening_analysis: the screening analysis file output from the ARA pipeline, 
    contains information about the Blast and Bowtie2 runs
    ```

    * This command outputs the results of a chi-squared analysis on the abundancies of each isolation source of the genomes that contain the query sequence.

# What Does This Pipeline Output?

* A list of SRA accession numbers of genomes that contain the specified query sequence: `Filtered_data.csv`

* A list of the isolation sites of the genomes that contain the specified query sequences, along with the number of times each isolation site occurs: `isolation_counts.csv`

* A bar plot to visualize the data included in `isolation_counts.csv`: `isolation_counts.png`

* The results of the chi-square analysis of the data included in `isolation_counts.csv`

# To test this pipeline....Dr. Wheeler

* Take the output 100MZ.screening.analysis.stats.sorted.by.alignment.txt and run it through Step Two. 
