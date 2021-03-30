               ####3D Organelle Project##########
#For this I have made "generic" scripts for each distance metric - it is slow
#but it is easier to trouble shoot - re run and it saves memory.
#With 64gb RAM the highest resolution I could get it working with is 40nm*40m
#keeping the depth at 50nm.The images are reduced in script using "zoom"
#this is very slow but keeps the option open to run at highest res possible

#Currently there are 5 Scripts which run independtly 
#1) Cell wall to mitochodnria (obstructed) 'CW to MIT-GEODESIC.py'
#2) Chl to mitochondria (obstructed) 'CHL to MIT-GEODESIC.py'
#3) Airspace to mitochdria (obstrucetd) 'AIR to MIT-GEODESIC.py'
#4) Airspace to chl (obstruced) 'AIR to CHL-GEODESIC.py'
#5) Airspace to micondria (unobstruced)

#The cell which is analysed is deteremied by changing the "sammple" text
#and the organelle_name - All cells have the same naming structure 
#D= data 
#C = cell

                         #######
           ############### D2C1 ###########
           
###############################################################################
################Cell Wall To Mitochondria (Geodsic Path)#####################
image_dir = 'C:/Users/Richard/Desktop/GTRDIST/';sample="D2C1_"
import runpy;import os;os.chdir('C:/Users/Richard/Desktop/Organelles/OrganelleScripts/')
####
chl_name='D2C1CHL.tif'   
mit_name='D2C1MIT.tif'
cell_w_org_name="D2C1VAC.tif"
cell_name="D2C1CELL.tif"
air_name="D2C1AIR.tif"
####
exec(open('CW to MIT-GEODESIC.py').read())
%reset -f
###############################################################################
###################Chloroplast To Mitochondria (Geodsic Path)################
image_dir = 'C:/Users/Richard/Desktop/GTRDIST/';sample="D2C1_"
import runpy;import os;os.chdir('C:/Users/Richard/Desktop/Organelles/OrganelleScripts/')
####
chl_name='D2C1CHL.tif'   
mit_name='D2C1MIT.tif'
cell_w_org_name="D2C1VAC.tif"
cell_name="D2C1CELL.tif"
air_name="D2C1AIR.tif"
####
exec(open('CHL to MIT-GEODESIC.py').read())
%reset -f

###############################################################################
###################Airspace To Mitochondria (Geodsic Path)###################
image_dir = 'C:/Users/Richard/Desktop/GTRDIST/';sample="D2C1_"
import runpy;import os;os.chdir('C:/Users/Richard/Desktop/Organelles/OrganelleScripts/')
####
chl_name='D2C1CHL.tif'   
mit_name='D2C1MIT.tif'
cell_w_org_name="D2C1VAC.tif"
cell_name="D2C1CELL.tif"
air_name="D2C1AIR.tif"
####
exec(open('AIR to MIT-GEODESIC.py').read())
%reset -f

###############################################################################

###############################################################################
#################Airspace to Chloroplasts (Geodsic Path)########################
image_dir = 'C:/Users/Richard/Desktop/GTRDIST/';sample="D2C1_"
import runpy;import os;os.chdir('C:/Users/Richard/Desktop/Organelles/OrganelleScripts/')
####
chl_name='D2C1CHL.tif'   
mit_name='D2C1MIT.tif'
cell_w_org_name="D2C1VAC.tif"
cell_name="D2C1CELL.tif"
air_name="D2C1AIR.tif"
#### 
exec(open('AIR to CHL-GEODESIC.py').read())
%reset -f
###############################################################################
