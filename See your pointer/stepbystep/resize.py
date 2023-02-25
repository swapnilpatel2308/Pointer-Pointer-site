# importing Image class from PIL package
from PIL import Image
import os
# creating a object

folder = r"DATA"

for image in os.listdir(folder):
    im=Image.open(folder+"\\"+image)
    im = im.resize((1100,750))
    im.save(folder+"\\"+image)
