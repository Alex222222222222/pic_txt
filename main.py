from __future__ import print_function
import PIL
import math
import os
from PIL import Image
#用于将图片缩小至合适的大小

def reduce(path):
    pic = Image.open(path,'r')
    width,height=pic.size
    width_=512
    k=width_/width
    height_=math.floor(height*k)
    pic.thumbnail((width_,height_))
    pic.save('done.png','png')
    return()

def grew(path):
    pic=Image.open(path,'r')
    pic=pic.convert('L')
    pic.save('grew.png','png')
    pic.close
    os.remove(path)

def dic(path):
    file=open(path):
    

if __name__=='__main__':
    path='test.png'
    reduce(path)
    grew('done.png')