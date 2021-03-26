import numpy as np
import pydicom
import matplotlib.pyplot as plt
import skimage
import os
import pdb

datadir = './CT_chest_scans'
ct_pixel = []
ct_hounsfield = []
folders = os.listdir(datadir)
for folder in folders:
    imagedir = os.path.join(datadir, folder)
    images = os.listdir(imagedir)
    for image in images:
        image_path = os.path.join(imagedir, image)
        pic = pydicom.dcmread(image_path)
        pixel_value = pic.pixel_array
        ct_pixel.append(pixel_value)
        rescale_intercept = pic[0x0028, 0x1052].value
        rescale_slope = pic[0x0028, 0x1053].value
        hounsfield_units = (rescale_slope * pixel_value) + rescale_intercept
        ct_hounsfield.append(hounsfield_units)
print("Maximum of raw data pixels =", np.amax(ct_pixel))
print("Minimum of raw data pixels =", np.amin(ct_pixel))
print("Mean of raw data pixels =", np.mean(ct_pixel))
print("Standard deviation of raw data pixels =", np.std(ct_pixel))
print("Maximum of Hounsfield units =", np.amax(ct_hounsfield))
print("Minimum of Hounsfield units =", np.amin(ct_hounsfield))
print("Mean of Hounsfield units =", np.mean(ct_hounsfield))
print("Standard deviation of Hounsfield units =", np.std(ct_hounsfield))
# pdb.set_trace()
