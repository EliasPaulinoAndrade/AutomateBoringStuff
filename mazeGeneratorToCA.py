import random

def printar(lista):
        arquivo=open('labirinto.txt','w')
        saida=""
        for i in lista:
                for j in i:	saida=saida+str(j)+""
                saida=saida+"\n"
        arquivo.write(saida)
        arquivo.close()
tamanhoGround=15
tamanho=(tamanhoGround*2)+1
listaPercorridos=[]
pilhaDeOrdem=[]
quantidadeDeCasas=tamanho*tamanho
quantidadeGround=tamanhoGround*tamanhoGround
quantidadeDeCasasPercorridas=0
labirinto=[["x" if (x==0 or x==tamanho-1) and y!=0 and y!=tamanho-1 else "x" for x in range(tamanho)] if y%2==0 else ["0" if x%2!=0 else "x" for x in range(tamanho)] for y in range(tamanho)]
#labirinto=[["!" if (x==0 or x==tamanho-1) and y!=0 and y!=tamanho-1 else "-" for x in range(tamanho)] if y%2==0 else [" " if x%2!=0 else "!" for x in range(tamanho)] for y in range(tamanho)]
casaAtual=[random.choice([x for x in range(tamanho) if x%2!=0]), random.choice([x for x in range(tamanho) if x%2!=0])]
pilhaDeOrdem.append(casaAtual)
while(True):
        podeNaoPode=["0","0","0","0"]
        if [casaAtual[0]+2,casaAtual[1]] not in listaPercorridos and casaAtual[0]+2<tamanho:
                podeNaoPode[0]="left"
        if [casaAtual[0]-2,casaAtual[1]] not in listaPercorridos and casaAtual[0]-2>=0:
                podeNaoPode[1]="right"
        if [casaAtual[0],casaAtual[1]+2] not in listaPercorridos and casaAtual[1]+2<tamanho:
                podeNaoPode[2]="bottom"
        if [casaAtual[0],casaAtual[1]-2] not in listaPercorridos and casaAtual[1]-2>=0:
                podeNaoPode[2]="top"
        
        pode=[]
        for i in podeNaoPode:
                if i!="0": pode.append(i)
        if len(pode)==0:
                pilhaDeOrdem.pop()
                if(len(pilhaDeOrdem)==0): break;
                casaAtual=pilhaDeOrdem[-1]     
        else:        
                proxCasa=random.choice(pode)
                if proxCasa=="left":
                        labirinto[casaAtual[0]+1][casaAtual[1]]="0"
                        casaAtual=[casaAtual[0]+2,casaAtual[1]]
                        pilhaDeOrdem.append(casaAtual)
                        listaPercorridos.append(casaAtual)
                elif proxCasa=="right":
                        labirinto[casaAtual[0]-1][casaAtual[1]]="0"
                        casaAtual=[casaAtual[0]-2,casaAtual[1]]
                        pilhaDeOrdem.append(casaAtual)
                        listaPercorridos.append(casaAtual)
                elif proxCasa=="bottom":
                        labirinto[casaAtual[0]][casaAtual[1]+1]="0"
                        casaAtual=[casaAtual[0],casaAtual[1]+2]
                        pilhaDeOrdem.append(casaAtual)
                        listaPercorridos.append(casaAtual)
                elif proxCasa=="top":
                        labirinto[casaAtual[0]][casaAtual[1]-1]="0"
                        casaAtual=[casaAtual[0],casaAtual[1]-2]
                        pilhaDeOrdem.append(casaAtual)
                        listaPercorridos.append(casaAtual)

labirinto.insert(0, ["x"]*tamanho)
for linhaind in range(len(labirinto)):
        labirinto[linhaind].insert(0, "x")
printar(labirinto)
input("Labirinto Gerado")
