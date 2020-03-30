from cv2 import cv2
import numpy as np
from PIL import Image, ImageColor
from matplotlib import pyplot as plt


class ImageFilters:
    def __init__(self):
        pass

    def colorBlend(self,image,color='#000000',extent=0):
        '''
        Blends the given Image with the color passed upto certain extent passed

        extent supposed to be within 0 and 0.5

        Note: Use values between 0 and 0.75 for good usage

        Datatypes: image:nparray format BGR, extent: float between 0 and 0.5, color:Strings supported by ImageColor module

        Defaults: color=White, extent=0
        '''
        try:
            if (extent<0 or extent>0.5):

                # Create Custom Error

                raise TypeError
            else:
                image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
                img_formatted = Image.fromarray(image)
                color = ImageColor.getrgb(color)
                shade = Image.new('RGB', img_formatted.size, color)
                blendim = Image.blend(img_formatted,shade,extent)
                blendim = np.array(blendim)
        except:
            blendim = image
            blendim = cv2.cvtColor(blendim , cv2.COLOR_BGR2RGB)
        return blendim

    def cartoon(self,image):
        '''
        Cartoonise Image!

        Datatypes: image:nparray format BGR
        
        '''
        numdown,numbilateral = 2,7
        color = image
        for _ in range(numdown):
            color = cv2.pyrDown(color)
        for _ in range(numbilateral):
            color = cv2.bilateralFilter(color, d=9, sigmaColor=9, sigmaSpace=7)
        for _ in range(numdown):
            color = cv2.pyrUp(color)
        cartoon = cv2.bitwise_and(color, cv2.cvtColor(cv2.adaptiveThreshold(cv2.medianBlur(cv2.cvtColor(image, cv2.COLOR_RGB2GRAY), 7),
        255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2), cv2.COLOR_GRAY2RGB))
        cartoon = cv2.cvtColor(cartoon , cv2.COLOR_BGR2RGB)
        return cartoon

    


if __name__ == "__main__":
    # img = cv2.imread('Image.jpg')
    # image1=Filter(img)
    # plt.subplot(121),plt.imshow(image1.sharpen(amount=2)),plt.title('blend'),plt.xticks([]),plt.yticks([])
    # plt.subplot(122),plt.imshow(cv2.cvtColor(img , cv2.COLOR_BGR2RGB)),plt.title('original'),plt.xticks([]),plt.yticks([])
    # plt.show()
    pass