# to_ncs_graph

Its a cool tepository for making .meta 
file from .h5 weight file and json model 
file. 
clone this repo
cd to_ncs_graph
python to_ncs_graph.py -m path/to/model -w path/to/weight

Then you will get a TF_Model folder ans 
logs folder. TF_Model file contains the 
.meta file that you want and logs folder 
contains the file writer buffer protocols 
uses for visualizing graphs using 
tensorboard. 

Use mvNCCompile for making graphs from 
.meta file that is already been 
converted.
