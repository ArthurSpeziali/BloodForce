#Se ativada em config.json, cria uma função que testará mais combinações, com espaço, underline, letra maiuscula e minuscula:
def temp(lista: list):
    palavras = []
    palavras_novas = []

    #Abre o combinações.txt, percorre cada linha e executa as verificações:
    with open('combinações.txt', 'a') as comb_app:
        
        comb_app.write('\n')   
        for i in lista:
            #Se tiver espaço em branco, troca por um "_", tira o espaço, escreve as mudanças na lista:
            if ' ' in i:
                palavras.append(i.replace(' ', ''))
                palavras.append(i.replace(' ', '_'))
            
            #Se um "_", troca por um espaço em branco, tira o espaço, escreve as mudanças na lista:
            if '_' in i:
                palavras.append(i.replace('_', ' '))
                palavras.append(i.replace('_', ''))

        #Cria uma função que pecorre cada letra da lista anterior, e executará as verificações:
        def letras(palavras):
            for x in palavras:
                
                #Verifica se só tem número em uma string na lista de forma dinâmica;
                try:
                    type_i = int(x)
                except:
                    try:
                        type_i = float(x)
                    except:
                        type_i = x
                
                #Se não for número, executará as verificações e escreve em uma nova lista:
                if type(type_i) == str:
                    
                    #Se a string não tiver totalmente em letras minúscula, deixará todas as letras em minúsculas:
                    if not x.islower():
                        palavras_novas.append(x.lower())
                    
                    #Se a string não tiver totalmente em letras maiúsculas, deixará todas as letras em maiúsculas:
                    if not x.isupper():
                        palavras_novas.append(x.upper())
                
                #Se a primeira letra da sting não for numeral, e se for minúscula, captaliza a palavras:
                if x[0].isalpha() and x[0].islower():
                    palavras_novas.append(x.capitalize())

    #Executa as duas funções:
    letras(palavras)
    letras(lista)
    
    #Junta todas as 3 listas em uma só, e remove todas as strings repetidas na nova lista:
    comb_lista = set(palavras + palavras_novas + lista)
    for app in comb_lista:
        
        #Escreve a nova lista na combinações.txt, cada combinação em uma linha:
        with open('combinações.txt', 'a') as comb_app:
            comb_app.write(app + '\n')
