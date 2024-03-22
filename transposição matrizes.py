matriz_linhas= int (input('Quantas linhas têm sua matriz?\n'))
matriz_colunas= int (input('Quantas colunas têm sua matriz?\n'))
matriz= []
for linha in range (matriz_linhas):
    elementos_linha= list (map (int, input(f'Digite os elementos da linha {linha+1}\n').split()))
    nova_linha=[]
    for i in elementos_linha:
        nova_linha.append (i)
    matriz.append(nova_linha)
matriz_transposta= []
for coluna in range(matriz_colunas):
    linha_transposta= []
    for linha in range (matriz_linhas):
        linha_transposta.append (matriz[linha][coluna])
    matriz_transposta.append(linha_transposta)
for i in range (len (matriz_transposta)):
    print (*matriz_transposta[i])
