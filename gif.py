import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames=['cat2.jpeg','cat1.jpg']
images=[]

target_size=Image.open(filenames[0]).size

for filename in filenames:
    img=Image.open(filename).resize(target_size)
    images.append(np.array(img))
iio.imwrite('cat2.gif', images, duration=500,loop=0)