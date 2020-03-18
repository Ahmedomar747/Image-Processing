import matplotlib.pyplot as plt 
import numpy as np
from PIL import Image


def HP_filter_FD(W,H,D0,n):
    HP = np.zeros([W,H])
    c_i = (W//2)
    c_j = (H//2)
    for i in range(-c_i,c_i):
        for j in range(-c_j,c_j):
            dist = np.sqrt((i ** 2) + (j ** 2))
            if dist != 0:
                HP[c_i+i,c_j+j] = 1 / (1 + (D0/dist)**(2*n))
    return HP

def HB_filter_FD(W,H,D0,A):
    HP = HP_filter_FD(W,H,D0)
    A_mat = np.ones([W,H]) * (A-1)
    HB = np.multiply(A_mat,HP)
    return HB




img = np.asarray(Image.open("Moon.jpg"))


Width = img.shape[0]
Height = img.shape[1]

HB = HB_filter_FD(Width,Height,50,3)

newimg_FD = HB * FD

newimg_fd_unshifted = np.fft.ifftshift(img_fd_shifted)
newimg = np.fft.ifft2(newimg_fd_unshifted)
newimg = np.abs(newimg)




img_fd = np.fft.fft2(img)
img_fd_shifted = np.fft.fftshift(img_fd)


plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.subplot(122),plt.imshow(newimg, cmap = 'gray')
plt.show()