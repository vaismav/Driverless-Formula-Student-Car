from PIL import Image
import os
import image_utilities as image_util

def getNextImage():
    PATH = os.getcwd()+"/samples/1.png"
    return Image.open(PATH,"r") 

if __name__ == "__main__":
     image = getNextImage()
     image.show()