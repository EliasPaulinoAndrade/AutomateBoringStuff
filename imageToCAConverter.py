import os, sys
import Image

im = Image.open(input("Digite o link da imagem"))
fil = open("codigo.txt", "w");
sizeX, sizeY = im.size 
pix = im.load()
for i in range(sizeX+1):
       fil.write("x");
fil.write("\n");
for i in range(sizeY):
       fil.write("x");
       for j in range(sizeX):
              if(im.load()[j, i]==(0,0,0,255) or im.load()[j, i]==(0,0,0)):
                     fil.write("x");
              else:
                     fil.write("0");
       fil.write("\n");
fil.close()
