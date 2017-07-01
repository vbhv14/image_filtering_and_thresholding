print j,g
print i,h
from skimage import img_as_ubyte 
print out.min(), imgr.min(), out.max(), img.max(), type(out[0,0]), type(imgr[0,0])

print type(op), op.shape, type(op[0,0])
print op.max(), op.min()
boole=  imgr < 188
ac=img_as_ubyte(boole)
plt.imshow(boole,cmap='gray')
print 'lol', ac.shape, type(ac), ac.shape, type(ac[1,1])
io.imsave(r'C:\Users\vbhv\Desktop\abc\Band,,,_thresh_without_sobel.jpg',ac)