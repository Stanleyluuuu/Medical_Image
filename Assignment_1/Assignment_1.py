import numpy as np
import pydicom
import matplotlib.pyplot as plt
from skimage import measure
import os
import pdb


def get_hu(pic):
    pixel_value = np.clip(pic.pixel_array, 0, 255)
    rescale_intercept = pic[0x0028, 0x1052].value
    rescale_slope = pic[0x0028, 0x1053].value
    hounsfield_units = (rescale_slope * pixel_value) + rescale_intercept
    nor_hu = normalize_hu(hounsfield_units)

    return nor_hu

def normalize_hu(hounsfield_units):
    nor_hu = np.array([(x+1024) / 4096 for x in hounsfield_units])

    return np.float32(nor_hu)

datadir = './CT_chest_scans'

folders = os.listdir(datadir)
for folder in folders:
    imagedir = os.path.join(datadir, folder)
    images = os.listdir(imagedir)
    data = {}
    for image in images:
        image_path = os.path.join(imagedir, image)
        pic = pydicom.dcmread(image_path)
        hounsfield_units = get_hu(pic)
        pdb.set_trace()
        data[pic.InstanceNumber] = hounsfield_units
    volume = []
    for ins in sorted(data):
        volume.append(data[ins])
    fig=plt.figure(figsize=(8, 8))
    columns = 5
    rows = 5

    for i in range(5): ## load the data from 9 classes
        # a = list(np.where(labels == i))[0]
        for j in range(5): ## each 5 pictures for every 9 classes
            fig.add_subplot(rows, columns, i * 5 + j + 1)
            plt.imshow(volume[i * 5 + j])
            plt.axis('off')
    plt.savefig('result1.png', cmap=plt.cm.bone)
    pdb.set_trace()
        
pdb.set_trace()


# def get_hu(pic):
#     pixel_value = np.clip(pic.pixel_array, 0, 255)
#     rescale_intercept = pic[0x0028, 0x1052].value
#     rescale_slope = pic[0x0028, 0x1053].value
#     hounsfield_units = (rescale_slope * pixel_value) + rescale_intercept
#     nor_hu = normalize_hu(hounsfield_units)

#     return nor_hu

# def normalize_hu(hounsfield_units):
#     nor_hu = np.array([(x+1024) / 4096 for x in hounsfield_units])

#     return nor_hu

# datadir = './CT_chest_scans'
# ct_hounsfield = []
# folders = os.listdir(datadir)
# for folder in folders:
#     imagedir = os.path.join(datadir, folder)
#     images = os.listdir(imagedir)
#     for image in images:
#         image_path = os.path.join(imagedir, image)
#         pic = pydicom.dcmread(image_path)
#         hounsfield_units = get_hu(pic)
#         ct_hounsfield.append(hounsfield_units)
# pdb.set_trace()
