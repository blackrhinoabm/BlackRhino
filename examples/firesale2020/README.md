This simulation uses an extension of Greenwood et al (2015) to stress-test the South 
African banking sector given shock scenarios. 

The model is calibrated to cross-sectional balane sheet data of the BA 900 forms. 

Usage:

To run the model on one asset class and three shock scenarios type 
**python firesale.py -0.5 -0.2 -0.2 m_14** 


m_14 is one of 23 asset classes. It's also possible to specify shocks and simulation parameters in the config files firesale.xml, shock.xml. 


Important: use python 2.7 and pandas <= 19.0.2 to run. 
 
 

