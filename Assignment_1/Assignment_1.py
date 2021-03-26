import numpy as np
import pydicom
import matplotlib.pyplot as plt
from skimage import measure
import os
import pdb


# def plot_3d(image, threshold=-300): 
#     # p = image.transpose(2,1,0)
#     p = image
#     verts, faces, normals, values = measure.marching_cubes_lewiner(p, threshold)
#     fig = plt.figure(figsize=(10, 10))
#     ax = fig.add_subplot(111, projection='3d')
#     mesh = Poly3DCollection(verts[faces], alpha=0.1)
#     face_color = [0.5, 0.5, 1]
#     mesh.set_facecolor(face_color)
#     ax.add_collection3d(mesh)
#     ax.set_xlim(0, p.shape[0])
#     ax.set_ylim(0, p.shape[1])
#     ax.set_zlim(0, p.shape[2])

#     plt.show()


# datadir = './CT_chest_scans'

# folders = os.listdir(datadir)
# for folder in folders:
#     imagedir = os.path.join(datadir, folder)
#     images = os.listdir(imagedir)
#     data = {}
#     for image in images:
#         image_path = os.path.join(imagedir, image)
#         pic = pydicom.dcmread(image_path)
#         data[pic.InstanceNumber] = pic.pixel_array
#     volume = []
#     for ins in sorted(data):
#         volume.append(data[ins])
#         # pdb.set_trace()
    
#     plot_3d(np.array(volume))
# # pdb.set_trace()

def get_hu(pic):
    pixel_value = pic.pixel_array
    rescale_intercept = pic[0x0028, 0x1052].value
    rescale_slope = pic[0x0028, 0x1053].value
    hounsfield_units = (rescale_slope * pixel_value) + rescale_intercept

    return hounsfield_units


datadir = './CT_chest_scans'
ct_hounsfield = []
folders = os.listdir(datadir)
for folder in folders:
    imagedir = os.path.join(datadir, folder)
    images = os.listdir(imagedir)
    for image in images:
        image_path = os.path.join(imagedir, image)
        pic = pydicom.dcmread(image_path)
        hounsfield_units = get_hu(pic)
        ct_hounsfield.append(hounsfield_units)


