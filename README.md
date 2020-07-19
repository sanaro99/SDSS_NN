# Predicting Star/Galaxy/Quasar using NN 

The data consists of 10,000 observations of space taken by the SDSS. Every observation is described by 17 feature columns and 1 class column which identifies it to be either a star, galaxy or quasar.
Number of features were reduced to 7 after analyzing the data. The 7 features:
- Ultraviolet (u) better of DeV/Exp magnitude fit
- Green (g)  better of DeV/Exp magnitude fit
- Red ( r )  better of DeV/Exp magnitude fit
- Near Infrared (i)  better of DeV/Exp magnitude fit
- Infrared (z)  better of DeV/Exp magnitude fit
- redshift value

The Thuan-Gunn astronomic magnitude system. u, g, r, i, z represent the response of the 5 bands of the telescope.

The data is then fed to a Sequential Neural Network with 70:30 ratio for training and testing.

Model accuracy: 99%
Model loss: 0.035

The trained model is then used for prediction through a Tkinter GUI application. Sample screenshots of the same are attached below:-

![ss1.png](screenshots/ss1.png?raw=true "")
\
\
![ss2.png](screenshots/ss2.png?raw=true "")


