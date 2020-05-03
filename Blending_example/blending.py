#we are using numpy to generate RBGA array and PIL to save images from array to jpg
import numpy as np
from PIL import Image

#initialization of images as a RGBA array [R,G,B,alpha] using np.zeros function [y,x,type]
image_1 = np.zeros([100, 200, 4], dtype=np.uint8)
image_1[:, :100] = [255, 128, 0, 255] #Orange left side
image_1[:, 100:] = [0, 0, 255, 255]   #Blue right side

image_2 = np.zeros([100, 200, 4], dtype=np.uint8)
image_2[:, :100] = [255, 255, 255, 255] #white left side
image_2[:, 100:] = [0, 255, 0, 255] #green left side

#empty arrays
image_3 = np.zeros([100, 200, 4], dtype=np.uint8)
image_4 = np.zeros([300, 300, 4], dtype=np.uint8)

#transparency coefficient
d = 0.5

#alpha blending - second image over first with transparency d
for x in range(200):
    for y in range(100):
        image_3[y, x] = d * image_2[y, x] + (1 - d) * image_1[y, x]

#shift and blend of two images
#first image coordinates
x1_coord = 10
y1_coord = 80
#transparency
d_1 = 0.9

#second image coordinates
x2_coord = 100
y2_coord = 150
#transparency
d_2 = 0.5

#blending of first image
for x in range(x1_coord,200+x1_coord):
    for y in range(y1_coord,100+y1_coord):
        if(x < 300 and y <300):
            image_4[y, x] = d_1*image_1[y - y1_coord, x - x1_coord]

#blending of second image
for x in range(x2_coord,200+x2_coord):
    for y in range(y2_coord,100+y2_coord):
        if(x < 300 and y <300):
            image_4[y, x] = d_2*image_2[y - y2_coord, x - x2_coord]+(1-d_2)*image_4[y, x]


#first image
img = Image.fromarray(image_1)
img.save('first_image.png')

#second image
img = Image.fromarray(image_2)
img.save('second_image.png')

#alpha blending result
img = Image.fromarray(image_3)
img.save('alpha_blending.png')

#blending with shift
img = Image.fromarray(image_4)
img.save('shift_result.png')

#####################################################################

#open image and convert to array
image_5 = np.array(Image.open('flower.jpg'))
image_6 = np.array(Image.open('lena.jpg'))

#transparency coefficient
d = 0.8

#alpha blending
for x in range(np.shape(image_5)[1]):
    for y in range(np.shape(image_5)[0]):
        image_5[y, x] = d * image_5[y, x] + (1 - d) * image_6[y, x]

img = Image.fromarray(image_5)
img.save('lena_with_flower.png')