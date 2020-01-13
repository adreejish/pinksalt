from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image
import os
import numpy as np
from sklearn.cluster import KMeans

print ("donefromfile")

def showurl(pqr):
	print(pqr)
	script_dir=os.path.dirname(__file__)
	rel_path=".."+pqr
	print (rel_path)
	#rel_path="../media/coverimages/saltwater.jpeg"
	breakpath=pqr.split('/')
	imgname=breakpath[-1]
	randurl=os.path.join(script_dir,rel_path)
	original=Image.open(randurl)
	fig=plt.figure()
	plt.axis('off')
	plt.imshow(original)
	#plt.show()
	#rel_dir="../media/coverimages/compressedimg.png"
	rel_dir="../media/coverimages/" + imgname + "compressed.png"	
	randsave=os.path.join(script_dir,rel_dir)
	#plt.savefig("fromfile.png")
	try:
		fig.savefig(randsave,bbox_inches='tight', pad_inches=0)
		print("try block"+randsave)
	except:
		print("exception raised")
	print("function complete")

#randurl="Home/pinksalt/pink_salt_site/media/coverimages/saltwater"
#randurl="Desktop/projects/img/grid.jpg"

'''
fig=plt.figure()
script_dir=os.path.dirname(__file__)
rel_path="../media/coverimages/fishfillet.jpeg"
randurl=os.path.join(script_dir,rel_path)
original=Image.open(randurl)
plt.imshow(original)
newurl="../media/coverimages/fishfilletcompress.png"
saveurl=os.path.join(script_dir,newurl)
#plt.show()
fig.savefig(saveurl)
'''
