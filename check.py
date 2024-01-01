import os
import sys


KITTI12 = '/storage/datasets/kitti/stereo_2012'
KITTI15 = '/storage/datasets/kitti/stereo_2015'
CGI = '/storage/scratch2/e18-4yp-stereo-imaging/CGI-Stereo/pretrained_models/CGI_Stereo/'



if __name__ == "__main__":
    print(os.getcwd())

    cmd ='python3 save_disp.py --datapath_12 ' + KITTI12 + ' --datapath_15 ' + KITTI15 
    print("Disparity save for KITTI: ",cmd)
    os.system(cmd)
