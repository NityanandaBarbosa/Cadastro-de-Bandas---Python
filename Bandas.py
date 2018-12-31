import os
from time import sleep
def cadastro(x):
    arquivo = open('banda.txt', 'r')
    v = []
    for i in arquivo:
        i = i.split(',')
        for x in i:
            v.append(x)
    arquivo.close()
    a = input("Insira o da nome da banda\n")
    if a not in v:
        b = input('Qual estilo músical da banda.\n')
        b=b.lower()
        c = input('Qual numero de integrantes da banda.\n')
        d = input('Qual numero de música da banda.\n')
        x = (f'{a},{b},{c},{d},\n')
        arquivo = open('banda.txt', 'a')
        arquivo.write(x)
        arquivo.close()
    else:
        print('Nome da banda ja usado, retornaremos ao menu.\n')
def dois(n):
    arquivo=open('banda.txt','r')
    for i in arquivo:
        n = ''
        info=i.split(',')
        c=0
        for i in info:
            if c<=3:
                n+= (f'{i} ')
            else:
                z=0
            c+=1
        print(n)
    print()
    arquivo.close()
def tres(n):
    geral=[]
    generos=[]
    v=[]
    arquivo = open('banda.txt', 'r')
    n = ''
    for i in arquivo:
        c=0
        info = i.split(',')
        for i in info:
            if c==0:
                v.append(i)
            if c==1:
                v.append(i)
                if i not in generos:
                    generos.append(i)
            c+=1
    for i in generos:
        x=i
        n = ''
        c=0
        n+=(f'{i}:\n')
        for a in v:
            if a == x:
                n+=(f'    {v[c-1]}\n')
            else:
                z=0
            c += 1
        print(n)
    arquivo.close()
def quatro(n):
    geral=[]
    arquivo=open('banda.txt','r')
    maior=0
    menor=0
    for i in arquivo:
        info=i.split(',')
        geral.append(info)
    c=0
    for i in range(len(geral)):
        geral[i][3]
        x=int(geral[i][3])
        if c==0:
            maior=x
            menor=x
        if c>0:
            if x>maior:
                maior=x
            if x<menor:
                menor=x
        c+=1
    for i in range(len(geral)):
        c=0
        n=''
        for i in geral[i]:
            if c == 0:
                n+=f'{i}'
            if c==3:
                i=int(i)
                if i == maior:
                    print(f'{n} é a banda com mais músicas')
                if i == menor:
                    print(f'{n} é a banda com menos músicas')
            c+=1
    print()
def cinco(n1):
    arquivo=open('banda.txt','r')
    n=''
    geral = []
    for i in arquivo:
        info= i.split(',')
        geral.append(info)
    print(geral)
    arquivo.close()
    banda = input('Diga a banda que ira ser apagado\n')
    for i in range(len(geral)):
        v = []
        if banda in geral[i]:
            print(f'A banda {banda} foi deletada\n')
        if banda not in geral[i]:
            c = 0
            for i in geral[i]:
                if c<=3:
                    n+=(f'{i},')
                if c==4:
                    n+=(f'{i}')
                c+=1

    arquivo1=open('banda.txt','w')
    arquivo1.writelines(n)
    arquivo1.close()

escolha = 0
while(escolha!=6):
    limpa="\n"
    i=int(input('1-Cadastar nova banda\n2-Mostrar bandas cadastradas\n3-Mostrar bandas por gênero\n4-Mostrar bandas com maior e menor número de bandas\n5-Apagar uma banda por nome\n6-Sair\n'))
    while(i<=0 or i>6):
        i = int(input('Opção invalida,digite numeros do menu\n'))
    linha = ''
    escolha=i
    if escolha==1:
        cadastro(linha)
    elif escolha==2:
        dois(linha)
    elif escolha==3:
        tres(linha)
    elif escolha==4:
        quatro(linha)
    elif escolha==5:
        cinco(linha)