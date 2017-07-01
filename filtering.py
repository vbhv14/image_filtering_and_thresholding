import matplotlib.pyplot as plt
import numpy as np
from skimage import io, data, filters, img_as_ubyte, exposure 
i=0
j=0
b=np.matrix(np.zeros((3,3))) # x-dir kernel
print b.shape
b[0,0]=-1
b[0,1]=0
b[0,2]=1
b[1,0]=-2
b[1,1]=0
b[1,2]=2
b[2,0]=-1
b[2,1]=0
b[2,2]=1

c=np.matrix(np.zeros((3,3)))   # y-dir kernel
c[0,0]=1
c[0,1]=2
c[0,2]=1
c[1,0]=0
c[1,1]=0
c[1,2]=0
c[2,0]=-1
c[2,1]=-2
c[2,2]=-1
                   
print b,'\n', c
path=r'C:\Users\vbhv\Desktop\abc\clr_wheel.jpg'
img = io.imread(path)
print "input image-", img.shape,type(img)   
imgr=img[:,:,0]
print 'band extracted-', type(imgr), imgr.shape, '\n' 

out = np.empty([810, 810])
print 'output image -', type(out), out.shape, '\n'

while i< 790:
        h=i+1
        while j< 790:
            g=j+1 #clm
            x=imgr[h-1,g-1]*b[0,0]+imgr[h-1,g]*b[0,1]+imgr[h-1,g+2]*b[0,2]+imgr[h,g-1]*b[1,0]+imgr[h,g]*b[1,1]+imgr[h,g+1]*b[1,2]+imgr[h+1,g-1]*b[2,0]+imgr[h+1,g]*b[2,1]+imgr[h+1,g+1]*b[2,2]
            
            y=imgr[h-1,g-1]*c[0,0]+imgr[h-1,g]*c[0,1]+imgr[h-1,g+2]*c[0,2]+imgr[h,g-1]*c[1,0]+imgr[h,g]*c[1,1]+imgr[h,g+1]*c[1,2]+imgr[h+1,g-1]*c[2,0]+imgr[h+1,g]*c[2,1]+imgr[h+1,g+1]*c[2,2]
            x=np.sqrt(x**2)
            y=np.sqrt(y**2)
            ff= np.sqrt(x**2+y**2)
            out[h,g]= ff
        
            j=j+1
        i=i+1
        j=0

print out.min(), imgr.min(), out.max(), img.max(), type(out[0,0]), type(imgr[0,0]),'\n'
a= out.max()
op=img_as_ubyte(out/a)
print type(op), op.shape, type(op[0,0])
io.imsave(r'C:\Users\vbhv\Desktop\abc\test.jpg',op)



plt.subplot(2,2,1)
plt.imshow(imgr,cmap='gray')

plt.subplot(2,2,2)
plt.imshow(out,cmap='gray')

plt.subplot(2,2,3)
hist, bins_center = exposure.histogram(imgr)
plt.plot(bins_center, hist, lw=2)

plt.subplot(2,2,4)
hist1, bins_center1 = exposure.histogram(op)
plt.plot(bins_center1, hist1, lw=2)
plt.show