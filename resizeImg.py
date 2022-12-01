import sys
import yaml
# Importing Image class from PIL module
from PIL import Image

if len(sys.argv) <= 4: #insufficient command line arguments passed
  print("four arguments required: imgSrc.png imgTarg xTiles yTiles"); sys.exit(-1)

cmdName, imgSrcFn, imgTargFn, xTilesR, yTilesR = sys.argv # extract command-line arguments

xTiles = int(xTilesR); yTiles = int(yTilesR) #convert "R" raw=text to number

im = Image.open(imgSrcFn)
 
# Size of the image in pixels (size of original image) 
width, height = im.size

widthTile  = width/xTiles
heightTile = height/yTiles

for i in range(xTiles):
  for j in range(yTiles):
    left = widthTile * i;  right = left + widthTile
    top  = heightTile * j; bottom = top + heightTile
    
    im1 = im.crop((left, top, right, bottom))
    resized_image = im1.resize((160, 160), Image.Resampling.LANCZOS)

    outFn = "%s/%i_%i.png" % (imgTargFn, j+1, i+1)
    resized_image.save(outFn)

### end ###