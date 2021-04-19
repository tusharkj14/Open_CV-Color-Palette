import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# str_name = ' '   # The name of the mage file from which the color palette is to be made. It is contained in an "images" folder in the same directory
src = cv2.imread('images/{}.jpg'.format(str_name))
src2 = cv2.cvtColor(src,  cv2.COLOR_BGR2RGB)
img = cv2.resize(src2, (780, 540),interpolation = cv2.INTER_NEAREST)
C = img.reshape(-1, img.shape[-1])
df_pixel = pd.DataFrame({
    'red' : C[:,0],
    'green' : C[:,1],
    'blue' : C[:,2]
})

def set_pixel(X):
    d1 = X[0]
    d2 = X[1]
    d3 = X[2]
    return str(d1)+','+str(d2)+','+str(d3)

df_pixel['Pixels'] = df_pixel[['red','green','blue']].apply(set_pixel, axis=1)
# df_pixel.drop(['red','green','blue'], axis=1, inplace=True)

A = []
for i in df_pixel['Pixels'].value_counts().head(10).index:
    A. append([[int(j) for j in str(i).split(',')] for k in range(10)])

plt.figure(figsize=(10,10))
plt.imshow(np.array(A))
plt.savefig('images/color-palette_{}.jpeg'.format(str_name))
color_palatte = Image.open('images/color-palette_{}.jpeg'.format(str_name))

cv2.imshow('Main_photo', src)

color_palatte.rotate(90).show()


cv2.waitKey(0)
cv2.destroyAllWindows()
