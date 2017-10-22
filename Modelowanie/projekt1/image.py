import cv2
import numpy as np
import PIL.Image as Image
import libtiff
import tifffile as tiff
import geopandas as gpd

dataframe = gpd.read_file('dane_wejsciowe\L1_2_BDOT10k__OT_ADJA_A.shp')
dataframe.plot()
# print(type(dataframe))

# a = tiff.imread('dane_wejsciowe/Mozaika_ADM.tif')
# img = cv2.imread('dane_wejsciowe/Mozaika_ADM.tif', flags=cv2.IMREAD_COLOR)
# # print(a[100,100])
# # print(a.shape)
# rows = a.shape[0]
# columns = a.shape[1]
#
# for row in range(rows):
#     for column in range(columns):
#         print(a[row, column])