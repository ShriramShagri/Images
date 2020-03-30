from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

class ImageConverters:
    def __init__(self):
        pass

    def blur(self,image,kernel_size=(5,5),sigma=0):
        '''
        Takes average of all pixel under kernel area.

        Argument kernel_size takes kernel size default as (5,5)

        image is the image to be blurred

        Returns numpy array of format RGB
        '''
        try:
            blurim = cv2.GaussianBlur(image ,kernel_size, sigma)
        except:
            blurim = image
        finally:
            blurim = cv2.cvtColor(blurim , cv2.COLOR_BGR2RGB)
        return blurim

    def sharpen(self,image,kernel_size=(5,5), sigma=1.0, amount=1.0, threshold=0):
        '''
        Returns Sharpened Image using unsharp algorithm

        input image f(x,y) and produced image g(x,y)

        g(x,y) = f(x,y)-f_smooth(x,y)

        amount issimply amount of sharpening i.e higher the value of amount sharper the image

        threshold is the threshold for the low contrast mask 

        i.e the pixels for which the difference between theinput and blurred images is less than threshold will remain unchanged

        Datatypes: kernel:Tuple of integers, sigma,amount,threshold:float
        
        '''
        blurred = cv2.GaussianBlur(image,kernel_size,sigma)
        sharpened = float(amount+1)*image-float(amount)*blurred
        sharpened = np.maximum(sharpened,np.zeros(sharpened.shape))
        sharpened = np.minimum(sharpened,255*np.ones(sharpened.shape))
        sharpened = sharpened.round().astype(np.uint8)
        if threshold > 0:
            low_contrast_mask = np.absolute(image-blurred)<threshold
            np.copyto(sharpened,image,where=low_contrast_mask)
        sharpened = cv2.cvtColor(sharpened , cv2.COLOR_BGR2RGB)
        return sharpened

    


if __name__ == "__main__":
    # img = cv2.imread('Image.jpg')
    # image1=Filter(img)
    # plt.subplot(121),plt.imshow(image1.sharpen(amount=2)),plt.title('blend'),plt.xticks([]),plt.yticks([])
    # plt.subplot(122),plt.imshow(cv2.cvtColor(img , cv2.COLOR_BGR2RGB)),plt.title('original'),plt.xticks([]),plt.yticks([])
    # plt.show()
    pass