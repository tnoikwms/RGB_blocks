from PIL import Image, ImageFilter
import cv2
import numpy as np
im = np.array(Image.open('855a1e1e5d5eb4b60dd4b5e52e0065f6.jpg'))
print(type(im))
im_rgb =  cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

print(im_rgb.shape)

class average():
    def __init__(self):
        self.im = im_rgb
        self.h = self.im.shape[0]
        self.w = self.im.shape[1]
        self.rgb_ave = np.zeros(self.im.shape)
        self.rgb_block = np.zeros(self.im.shape)
        self.i = 200
        self.scale = self.h/(self.i*600)
        print(self.scale)
    def cal(self):
        for i in range(1,self.h,int(self.h/self.i)):
            for j in range(1,self.w):
                self.rgb_ave[i][j][0]=self.im[i-1:i+1,j-1:j+1,0].mean()
                self.rgb_ave[i][j][1]=self.im[i-1:i+1,j-1:j+1,1].mean()
                self.rgb_ave[i][j][2]=self.im[i-1:i+1,j-1:j+1,2].mean()
        rgb_ave = self.rgb_ave
        return rgb_ave
    def block(self):
        for i in range(self.i):
            haxis = int(i*self.h/self.i+self.h/(self.i*2))
            for j in range(1,int(self.w),6):
                self.rgb_block[haxis-int(self.rgb_ave[int(self.h/self.i)*(i+1)+1][j][0]*self.scale):haxis+int(self.rgb_ave[int(self.h/self.i)*(i+1)+1][j][0]*self.scale)+1,j:j+2] = [255,0,0]
                self.rgb_block[haxis-int(self.rgb_ave[int(self.h/self.i)*(i+1)+1][j][1]*self.scale):haxis+int(self.rgb_ave[int(self.h/self.i)*(i+1)+1][j][1]*self.scale)+1,j+2:j+4] = [0,255,0]
                self.rgb_block[haxis-int(self.rgb_ave[int(self.h/self.i)*(i+1)+1][j][2]*self.scale):haxis+int(self.rgb_ave[int(self.h/self.i)*(i+1)+1][j][2]*self.scale)+1,j+4:j+6] = [0,0,255]
        rgb_block = self.rgb_block
        return rgb_block

ave = average()
rgb_ave = ave.cal()
rgb_block = ave.block()
cv2.imwrite('rgb_ave.jpg', rgb_ave)
cv2.imwrite('undertale.jpg', rgb_block)