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
    pic.save('reduce.png','png')
    return()

def grew():
    path='reduce.png'
    pic=Image.open(path,'r')
    pic=pic.convert('L')
    pic.save('grew.png','png')
    pic.close
    os.remove(path)

def dic_pixel():
    path='pixel.txt'
    dic={}
    file=open(path,'r')
    temp=file.readlines()
    file.close
    for temp_1 in temp:
        if len(temp_1)>=3:
            for i in range(len(temp_1)):
                if temp_1[i]==':':
                    break
            dic[int(temp_1[:i])]=temp_1[i+1:][0]
    return(dic)

def png_txt(name):
    grew_png='grew.png'
    pic=Image.open(grew_png,'r')
    width,height=pic.size
    min=255
    max=0
    for i in range(1,height):
        for j in range(1,width):
            color=pic.getpixel((j,i))
            if color>max:
                max=color
            if color<min:
                min=color
    k=105/(max-min)
    a=150-105*min/(max-min)
    file=open('%s.txt'%(name,),'w')
    pixel_dic=dic_pixel()
    i=1
    jjjjjjj=1.0000
    while i<height:
        j=1
        while j<width:
            file.write(pixel_dic[math.floor(pic.getpixel((j,i))*k+a+0.5)])
            j+=1
        file.write('\n')
        jjjjjjj+=768*202/59/1417*660*679/1079/383
        i=math.floor(jjjjjjj+0.5)
    file.close
    os.remove('grew.png')
    return

def main():
    alex=("""
*@@@@@#)   5@#      #@4                )@@)      @@          @@@@@@@@$  @@^     0@*       
3@0   7@@*  $@@    @@6                 @@@@      @@_        _@@          @@*   @@)        
3@0    @@$   7@@  @@*      @@@)       9@11@#     @@_        _@@           @@6^@@          
3@@@@@@@_     !@@@@^       @@@)      _@@  @@^    @@_        _@@@@@@@@*     4@@@           
3@0    #@@      @@                   @@)  )@@    @@_        _@@            @@@@_          
3@0     @@      @@                  1@@@@@@@@2   @@_        _@@          ^@@_ @@7         
3@0    @@@      @@         @@@)     @@_     @@   @@_        _@@         5@@    @@9        
2@@@@@@#_       @@         @@@)    #@#      9@#  @@@@@@@@@_  @@@@@@@@@ 0@0      #@@       
                                                                                            
Please choose a file(directory)!!!
""")
    path=input(alex)
    name=input("Please slect your file name!!!\n")
    print('Your file will at this directory!!!\nName:%s.txt'%(name,))
    try:
        reduce(path)
        print('PIC reduced!!!')
        grew()
        print('PIC is now grew!!!')
        png_txt(name)
    except:
        print('Maybe no such file or directory!!!\nMaybe your file is not a PICTURE!!!\nTry Again!!!')
    else:
        print('Successfully Done!!!')
    return

if __name__=='__main__':
    main()