##D2C1
#Geomertic Distance from AIR to CW
import numpy as np
import os
from scipy.ndimage.morphology import distance_transform_edt, binary_erosion
import skfmm
import imageio
import skimage.io as io
from skimage import img_as_ubyte, img_as_bool, img_as_float32
from skimage.util import invert
from skimage.measure import label, regionprops, marching_cubes_lewiner, mesh_surface_area
import matplotlib.pyplot as plt
from scipy import stats
from scipy.ndimage import zoom
import gc

def Erosion3DimJ(input_img):
    tmp = np.zeros(input_img.shape)
    for i in range(input_img.shape[0]):
        tmp[i, :, :] = binary_erosion(input_img[i, :, :])
    return tmp

def Threshold(input_img, Th_value):
    tmp = np.zeros(input_img.shape, dtype=np.bool)
    if isinstance(Th_value, int):
        tmp[input_img == Th_value] = 1
    else:
        if isinstance(Th_value, float):
            tmp[input_img > 0. & input_img < 1.] = 1
        else:
            for th_val in range(len(Th_value)):
                tmp[input_img == Th_value[th_val]] = 1
    return tmp
#os.chdir('C:/Users/Richard/Desktop/GTRDIST/')
#output ="C:/Users/Richard/Desktop/GTRDIST/output/"

#image_dir = 'C:/Users/Richard/Desktop/GTRDIST/'
#sample="D2C1_"
###############################################################################
voxel_dims = [0.05,0.04,0.04] 
##############################################################################
chl=io.imread(image_dir + chl_name)
chl=zoom(chl, (1, 0.5, 0.5)) #This is the same as Image > adjust >size in FIJI
chl[chl==0] = 0
chl[chl==1] = 255
chl=img_as_bool(chl)
###############################################################################
# cell_w_org = io.imread(image_dir + 'D2C1Vac50.tif')
# cell_w_org[cell_w_org==0] = 0
# cell_w_org[cell_w_org==1] = 255
# cell_w_org=img_as_bool(cell_w_org)
###############################################################################
# cell = io.imread(image_dir + 'D2C1Cell50.tif')
# cell[cell==0] = 0
# cell[cell==1] = 255
# cell=img_as_bool(cell)
###############################################################################
air=io.imread(image_dir + air_name)
air=zoom(air, (1, 0.5, 0.5)) #This is the same as Image > adjust >size in FIJI
air[air==0] = 0
air[air==1] = 255
air=img_as_bool(air)
###############################################################################
mito = io.imread(image_dir + mit_name)
mito=zoom(mito, (1, 0.5, 0.5))
mito[mito==0] = 0
mito[mito==1] = 255
mito=img_as_bool(mito)
###############################################################################
#chl = chl[50:700]
#mito = mito[50:700]
#cell_w_org = cell_w_org[50:700]
#cell = cell[50:700]
#air=air[50:700]
# Create chl and mito array
chl_mito = chl + mito
# Create mask
# cell_w_org_mask = ~cell_w_org.astype(bool)
#io.imshow(cell_w_org_mask[100])
###############################################################################
# Get chl outline
chl_outline_smaller = Erosion3DimJ(invert(chl))
chl_edge = invert(Threshold(invert(chl)-chl_outline_smaller, 0))
chl_edge[0,:,:] = False
chl_edge[-1,:,:] = False
chl_edge[:,0,:] = False
chl_edge[:,-1,:] = False
chl_edge[:,:,0] = False
chl_edge[:,:,-1] = False
###############################################################################
#io.imsave(sample+'_chl_edge.tif', img_as_ubyte(chl_edge[30]))
###############################################################################
air_masked_array = np.ma.masked_array(invert(air), chl_mito)
##############################################################################
D_geo_from_air = skfmm.distance(air_masked_array, dx=voxel_dims)
###############################################################################
L_geo_edge_air_chl = np.asarray(D_geo_from_air[(chl_edge == True)])
##############################################################################
np.savetxt(sample+"L_geo_edge_air_chl.csv", L_geo_edge_air_chl, delimiter=",")
#############################################################################