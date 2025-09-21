import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames=['cat-1.jpeg','cat-2.jpeg']
images=[]

target_size=Image.open(filenames[0]).size

for filename in filenames:
    img=Image.open(filename).resize(target_size)
    images.append(np.array(img))

iio.imwrite('cat.gif', images, duration=500,loop=0)
