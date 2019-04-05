import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
from PIL import Image
import subprocess
import pandas as pd
import argparse

"""

im = Image.open("test.jpg")

crop_rectangle = (50, 50, 200, 200)
cropped_im = im.crop(crop_rectangle)

cropped_im.show()
"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
	help="path to input image")
ap.add_argument("-e", "--excel", type=str,
	help="path to output excel")
args = vars(ap.parse_args())
#im = np.array(Image.open('sam.jpeg'), dtype=np.uint8)
ipfile = args["image"]
opfile=args["excel"]
im2 = Image.open(ipfile)

size = (575,356)
#im = im.resize((575,356),Image.ANTIALIAS)
im2 = im2.resize((574,359),Image.ANTIALIAS)
im = np.array(im2, dtype=np.uint8)
# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

# Create a Rectangle patch

#regnoKA
regnoKA = patches.Rectangle((140,4),280,28,linewidth=1,edgecolor='r',facecolor='none')
regnoKACrop = im2.crop((140,4,420,30))
regnoKACrop.save('regnoKA.jpeg')
regDateKA = patches.Rectangle((0,48),203,16,linewidth=1,edgecolor='r',facecolor='none')
regDateKACrop = im2.crop((0,48,203,64))
regDateKACrop.save('regDateKACrop.jpeg')

chasisNoKA = patches.Rectangle((0,65),286,16,linewidth=1,edgecolor='r',facecolor='none')
chasisNoKACrop = im2.crop((0,65,286,81))
chasisNoKACrop.save('chasisNoKACrop.jpeg')


engineNoKA = patches.Rectangle((0,83),220,18,linewidth=1,edgecolor='r',facecolor='none')
engineNoKACrop = im2.crop((0,83,217,99))
engineNoKACrop.save('engineNoKACrop.jpeg')


ownerNameKA = patches.Rectangle((0,115),215,13,linewidth=1,edgecolor='r',facecolor='none')
ownerNameKACrop = im2.crop((0,115,215,128))
ownerNameKACrop.save('ownerNameKACrop.jpeg')


addressKA = patches.Rectangle((0,150),417,52,linewidth=1,edgecolor='r',facecolor='none')
addressKACrop = im2.crop((0,150,417,202))
addressKACrop.save('addressKACrop.jpeg')

modelKA = patches.Rectangle((0,227),300,17,linewidth=1,edgecolor='r',facecolor='none')
modelKACrop = im2.crop((0,231,300,248))
modelKACrop.save('modelKACrop.jpeg')

mfgDateKA = patches.Rectangle((0,284),195,12,linewidth=1,edgecolor='r',facecolor='none')
mfgDateKACrop = im2.crop((0,281,195,296))
mfgDateKACrop.save('mfgDateKACrop.jpeg')

fuelKA = patches.Rectangle((0,300),195,13,linewidth=1,edgecolor='r',facecolor='none')
fuelKACrop = im2.crop((0,301,195,314))
fuelKACrop.save('fuelKACrop.jpeg')

# Add the patch to the Axes
ax.add_patch(regnoKA)
ax.add_patch(regDateKA)
ax.add_patch(chasisNoKA)
ax.add_patch(engineNoKA)
ax.add_patch(ownerNameKA)
ax.add_patch(addressKA)
ax.add_patch(modelKA)
ax.add_patch(mfgDateKA)
ax.add_patch(fuelKA)
plt.show()


"""
cmd = ['echo', 'I like potatos']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
o, e = proc.communicate()
print('Output: ' + o.decode('ascii'))
print('Error: '  + e.decode('ascii'))
print('code: ' + str(proc.returncode))
"""

def returnImageText():
    answerString = {}
    keys = ['RegisterNumber','RegisterDate','ChasisNo','EngineNo','OwnerName','address','model','mfgDate','fuel']
    #Pass the path to the tesseract api
    image_file_names = ['regnoKA.jpeg','regDateKACrop.jpeg','chasisNoKACrop.jpeg','engineNoKACrop.jpeg','ownerNameKACrop.jpeg','addressKACrop.jpeg','modelKACrop.jpeg','mfgDateKACrop.jpeg','fuelKACrop.jpeg']
    j=0
    for i in image_file_names:
        cmd = ['tesseract',i,'op'+i]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()
        #print('Output : '+o.decode('ascii'))
        fp = open('op'+i+'.txt','r')
        stringTemp = ""
        line = fp.readline()
        while line:
            stringTemp += " "+line
            line = fp.readline()   
	#print('hello')
        #print(i+": "+stringTemp)
        answerString[keys[j]] = stringTemp.split()[2:]
        j = j+1
        fp.close()
    for i in answerString.keys():
        print(str(i)+" -- > "+' '.join(answerString[i]))
    for i,j in answerString.items():
        answerString[i]=[' '.join(j)]
    print(answerString)
    df=pd.DataFrame(answerString)
    print(df)
    df.to_excel(opfile)
    
#returnImageText('G:\Hackathon\opencv-text-recognition\images\example_01.jpg')
returnImageText()







