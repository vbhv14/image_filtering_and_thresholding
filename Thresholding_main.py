import matplotlib.pyplot as plt
from skimage import data
from skimage import filters
from skimage import filter as filters
from skimage import exposure

camera = imgr
val = filters.threshold_otsu(camera)

hist, bins_center = exposure.histogram(camera)

plt.figure(figsize=(9, 4))
plt.subplot(131)
plt.imshow(camera, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(132)
plt.imshow(camera < val, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.subplot(133)
plt.plot(bins_center, hist, lw=2)
plt.axvline(val, color='k', ls='--')

plt.tight_layout()
plt.show()
print val

boo= camera < 200 
a= camera > 0
boole = a * boo
ac=img_as_ubyte(boole)
plt.imshow(boole,cmap='gray')
print 'lol', ac.shape, type(ac), ac.shape, type(ac[1,1])
io.imsave(r'C:\Users\vbhv\Desktop\abc\Otsu_thresh_without_sobel.jpg',ac)