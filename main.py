from PIL import Image
from PIL import ImageDraw
import numpy as np

while True:
    try:
        print 'h'
        image = raw_input('your image:')
        im = Image.open(image)
        break
    except IOError as Errno:
        print('i could not find your image')

def cropimage():
    width = im.size[0]/2
    height = im.size[1]/2
    offset = (height/3)*2
    box = (width-offset,height-offset,width+offset,height+offset)
    return box

def setFilter():
    box = cropimage()
    ic = im.crop(box)
    data = np.array(ic)
    r,g,b,_ = data.T[:5]
    selectFilter = raw_input('which color should turn negative?\n')
    if all(c in 'rgb' for c in selectFilter):
        for i in range(0,len(selectFilter)):
            if(selectFilter[i] == 'r'):
                r = 255-r
                print(selectFilter[i])
            elif(selectFilter[i] == 'g'):
                g = 255-g
                print(selectFilter[i])
            elif(selectFilter[i] == 'b'):
                b = 255-b
                print(selectFilter[i])
    else:
        print 'no match'
    filter = Image.fromarray(np.dstack([item.T for item in (r,g,b)]))
    getPoly(filter)
    return filter

def getPoly(filter):
    width = im.size[0]/2
    height = im.size[1]/2
    offset = (height/3)*2
    dr = ImageDraw.Draw(filter)
    zeroPointw = width-offset
    zeroPointh = height-offset
    widthOffset = width+offset
    heightOffset = height+offset
    cor = (0,0,widthOffset-zeroPointw-0,heightOffset-zeroPointh-0)
    dr.line((cor[0],cor[1],cor[0], cor[3]),width=3)
    dr.line((cor[0],cor[1],cor[2],cor[1]), width= 3)
    dr.line((cor[0],cor[3],cor[2],cor[3]), width=3)
    dr.line((cor[2],cor[1],cor[2],cor[3]), width=3)

filter = setFilter()
box = cropimage()
im.paste(filter,box)
im.save('polypy'+image)

