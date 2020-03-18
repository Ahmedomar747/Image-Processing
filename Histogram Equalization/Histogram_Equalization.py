import matplotlib.pyplot as plt 
import numpy as np
from PIL import Image

img = np.asarray(Image.open("Sphinx.png"))

Width = img.shape[0]
Height = img.shape[1]

H = np.zeros(256,dtype=int)
Hc = np.zeros(256,dtype=int)
EH = np.zeros(256,dtype=int)

new_img = np.zeros(img.shape)



for _,w in enumerate(img):
    for _,v in enumerate(w):
        H[v] += 1
        

for i in range(len(H)):
    for j in range(i):
        Hc[i] += H[j]

for i,v in enumerate(Hc):
    EH[i] = np.floor(v * 255 / (Width * Height))

new_img_arr = np.multiply(img,(max(EH) - min(EH))) + min(EH)

new_img = Image.fromarray(new_img_arr)
new_img.show()      