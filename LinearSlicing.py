import cv2
import numpy as np
import matplotlib.pyplot as plt


def binary_slicing(img, A, B,alt,ust):
     img_out= np.full_like(img,alt) #bir matris oluşturup alt değerleri at
     pk=np.logical_and(img >= A, img <=B)
     img_out[pk]=ust
     return img_out

def linear_slicing(img, A,B,ust): #bunda alt yok
     img_out = img.copy()
     pk=np.logical_and(img>=A,img<=B)
     img_out[pk]=ust
     return img_out

def linear_slicing_reverse(img, A,B,ust): #bunda alt yok
     img_out = img.copy()
     pk_kucuk=np.logical_and(img>=0,img<=A) #0-A ARASI
     pk_buyuk=np.logical_and(img>=B,img<=255) #B-255 ARASI
     pk=np.logical_or(pk_kucuk,pk_buyuk)#pk değeri pk küçük ya da pk büyük birleşitr
     img_out[pk]=ust
     return img_out


img_path = "./img/aortic_anogram.tif"
img=cv2.imread(img_path,0)

A=150
B=250
ust=255
alt=10

bs_img = binary_slicing(img,A,B,alt,ust)
ls_img = linear_slicing(img,A,B,ust)
lsr_img = linear_slicing(img,A,B,ust)

hstacked1 = np.hstack((img,bs_img))
hstacked2= np.hstack((img,lsr_img))
vstacked =np.vstack((hstacked1,hstacked2))

plt.imshow(vstacked,cmap='gray')
plt.show()

