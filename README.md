# Hello, Welcome to the Enterococcus README!
## 🚧 🚧 🚧 CAUTION: This README is under construction 🚧 🚧 🚧
# ARA Pipeline installation should follow the respective github of the authors. 

### After installation of ARA pipeline, go into the ARA-main folder and make an image. ara_img can be replaced with another name.  

```docker build -t ara_img . ```

### Next you force the docker to run with a static name that is associated with the image made previously. 

```docker run -t -d --name ARA_EF ara_img```

### Next you actually call the docker. 
```docker exec -it ARA_EF /bin/sh```

### ^ Navigate through home/ARA-main/ and look at what is in the directory. Adjust where you want the example data to be by using cp command. 

### From host to docker. *Need to be in host directory* 
```docker cp Enterococcus_Run.txt ARA_EF:/home/ARA-main/Enterococcus_Run.txt```

### From docker to host.
```docker cp ARA_EF:/results/. home/user/ARA-main/results```

### Once everything is uploaded run ARA pipeline inside docker. Input can be SRA IDS or SRARunInfo and sequences are what you query against. 
```./ara.pl --input /home/ARA-main/Enterococcus_Run.txt --sequences /home/ARA-main/MZ.fa```
