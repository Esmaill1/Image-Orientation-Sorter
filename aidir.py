import os
from PIL import Image
from time import perf_counter
import glob

start = perf_counter()


Ndirs = ['square','landscape','portrait']

## makes dir for each category
def dirmaker (dirs):
 for dir in dirs:
  FullPath = f"{os.getcwd()}/{dir}"
  os.makedirs(FullPath, exist_ok=True)  

 ## extract image size
def info():
  ldir = os.listdir(os.getcwd()) ## gets the all the dirs in the current dir
  ldir.append(os.getcwd()) ## adding the current dir too
  for ld in ldir : ## list all images in each dir then organize it 
   imagelist = glob.glob(f"{ld}/*.jpg")
   for img in imagelist :
    img0 = Image.open(img)
    imgsize = img0.size
    print(imgsize)
    organizer(img,imgsize)

def organizer(img ,imgsize):
 if imgsize[0] > imgsize[1]:
  print(os.getcwd())
  print(img)
  os.rename(img,f'landscape/{os.path.basename(os.path.normpath(img))}')
 elif imgsize[0] < imgsize[1]:
    os.rename(img,f'portrait/{os.path.basename(os.path.normpath(img))}')
 else:
    os.rename(img,f'square/{os.path.basename(os.path.normpath(img))}')


if __name__ == "__main__":
  
 start = perf_counter()
 dirmaker(Ndirs)
 info()
 print(f"Took {perf_counter() - start:.6f} seconds")