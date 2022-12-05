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

faq_head = Image.open('images/FAQ/FAQ_header.png')
resized_image = faq_head.resize((900, 80), Image.Resampling.LANCZOS)
resized_image.save('images/FAQ/FAQ_header_resize.png')

faq_icon = Image.open('images/icons/FAQ_icon.png')
resized_image = faq_icon.resize((80, 80), Image.Resampling.LANCZOS)
resized_image.save('images/icons/FAQ_icon_resize.png')

chat_icon = Image.open('images/icons/Chat_icon.png')
resized_image = chat_icon.resize((80, 80), Image.Resampling.LANCZOS)
resized_image.save('images/icons/Chat_icon_resize.png')

faq_body = Image.open('images/FAQ/FAQ_body.png')
resized_image = faq_body.resize((900, 400), Image.Resampling.LANCZOS)
resized_image.save('images/FAQ/FAQ_body_resize.png')

desc_body = Image.open('images/home/Description.png')
resized_image = desc_body.resize((800, 100), Image.Resampling.LANCZOS)
resized_image.save('images/home/Description_resize.png')

knowMore_icon = Image.open('images/home/knowMore_icon.png')
resized_image = knowMore_icon.resize((200, 80), Image.Resampling.LANCZOS)
resized_image.save('images/home/knowMore_icon_resize.png')

header = Image.open('images/home/clemsonHeader.png')
resized_image = header.resize((800, 120), Image.Resampling.LANCZOS)
resized_image.save('images/home/clemsonHeader_resize.png')

home = Image.open('images/home/home.png')
resized_image = home.resize((80, 80), Image.Resampling.LANCZOS)
resized_image.save('images/home/home_resize.png')

sos = Image.open('images/home/sos.png')
resized_image = sos.resize((80, 80), Image.Resampling.LANCZOS)
resized_image.save('images/home/sos_resize.png')

### end ###