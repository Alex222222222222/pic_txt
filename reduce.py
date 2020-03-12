from __future__ import print_function
import PIL
import math
from PIL import Image
#用于将图片缩小至合适的大小

def reduce(path):
    pic = Image.open(path,'r')
    width,height=pic.size
    width_=512
    k=width_/width
    height_=math.floor(height*k)
    print(str(width_)+','+str(height_))
    pic.thumbnail((width_,height_))
    pic.save('done.png','png')
    return()

if __name__=='__main__':
    path='test.png'
    print(reduce(path))