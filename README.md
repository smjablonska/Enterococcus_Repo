# Hello, Welcome to the Enterococcus README!
## 🚧 🚧 🚧 CAUTION: This README is under construction 🚧 🚧 🚧
# ARA Pipeline installation should follow the respective github of the authors 

## After installation of ARA pipeline, go into the ARA-main folder and make an image. ara_img can be replaced with another name.  

```docker build -t ara_img . ```

##Next you force the docker to run with a static name that is associated with the image made previously 

```docker run -t -d --name ARA_EF ara_img```
