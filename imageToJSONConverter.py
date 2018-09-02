import os, sys
from PIL import Image

imagem = Image.open("haha.png")

largura, altura = imagem.size
painelDePixels = imagem.load()

pseudoJson = "["
for indiceLinha in range(altura):
    for indiceColuna in range(largura):
        pseudoJson += "{\nindexPathX: " + str(indiceColuna) + " \nindexPathY: " + str(indiceLinha) + " \ncor: " + str(painelDePixels[indiceLinha, indiceColuna]) + "\n}, \n"
pseudoJson += "]"

print(pseudoJson)
