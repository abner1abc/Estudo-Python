def insereCircular(novoNo):
    if inicioLista==None:                      #lista vazia
        inicioLista=novoNo
        finalLista=novoNo
        novoNo.proximo=novoNo
    else:
        finalLista.proximo=novoNo              #insere o nó
        finalLista=novoNo                      #atualiza ponteiros
        finalLista.proximo=inicioLista