#Importando as bibliotecas:
import random
from turtle import home
from click import command
from pynput import keyboard
from time import sleep
import os
import platform
import pyautogui
from sys import exit
from pathlib import Path
import json
from itertools import product, permutations
#Importando variaveis de outros arquivos:
from keydic import  key_dic
from logos import logo_blood, logo_force
from comand_line import salvar_json, carregar_json, help_config, comand_line, help_bt
from tempt import temp
#Criando as variáveis padrões e configurações de inicialização:
tasks = 0
resultado = 0
pyautogui.FAILSAFE = False


#Se o SO do usuário for Linux, tenta criar um novo alias, para facilitar o uso do programa:
if platform.system() == 'Linux':
    
    #Com o Os, captura o caminho até este arquivo:
    path_blood = os.path.abspath(__file__)
    
    #Defini o alias para acessar  o programa:
    alias_blood = f'''
    #Alias adicionado automaticamente do program em Python BloodForce    
    alias bf="python3 {path_blood}"'''
    
    #CCalcula a home do usuario:
    home_alias = home = str(Path.home())
    
    #Tenta abrir o "bash_aliases", na pasta home:
    try:
        alias_path = f'{home_alias}/.bash_aliases'
        
        with open(alias_path, 'r', encoding='utf-8') as b_alias:
            bash_read = b_alias.read().split('\n')
    
    #Se não existir, abre o "bashrc", que também consegue colocar os aliases:
    except FileNotFoundError:
        alias_path = f'{home_alias}/.bashrc'
        
        with open(alias_path, 'r', encoding='utf-8') as b_alias:
            bash_read = b_alias.read().split('\n')
            
    #Calculando se o alias já existe, senão, adiciona o alias:
    if not alias_blood in bash_read:
        with open(alias_path, 'a', encoding='utf-8') as b_alias:
            b_alias.write(alias_blood)
            
        os.system(f'source {home_alias}/.bashrc && . {home}/.bashrc ')
            
        

#Abrindo as configurações do programa:
with open('config.json') as config_json:
    config = json.load(config_json)

#Se ativado, limpa as combinações em combinações.txt:
if config['dump']:
    with open('combinações.txt', 'w') as comb:
        comb.write('\n')

#Definindo as Funções:

#Função para calcular o dicioanrio de palavras:    
def dic_lang():
    
    if config['lang'] == 'pt':
        with open('palavras-pt.txt', encoding='utf-8') as palavras_pt:
            dicionario = palavras_pt.read().split('\n')
            
    elif config['lang'] == 'en': 
        with open('palavras-en.txt', encoding='utf-8') as palavras_en:
            dicionario = palavras_en.read().split('\n')
            
    elif config['lang'] == 'enpt':
        with open('palavras-pt.txt', encoding='utf-8') as palavras_pt:
            dicionario_pt = palavras_pt.read().split('\n')
            
        with open('palavras-en.txt', encoding='utf-8') as palavras_en:
            dicionario_en = palavras_en.read().split('\n')
            
        dicionario = dicionario_pt + dicionario_en
        
    
    salvar_json(config)
    carregar_json(config)
    
    #Coloco o "# type: ignore" na frente de qualquer váriavel que não foi definida diretamente.
    #Sugestão do Intellicode, sintaxe do Python 3.10:
    return dicionario # type: ignore

#Função para processar o tipo de caracteres em config.json:
def alfa():
    if config['car'] == 'ltnum':
        caracteres = 'abcdefghijklmnopqrstuvwxyz0123456789'
        
    elif config['car'] == 'lt':
        caracteres = 'abcdefghijklmnopqrstuvwxyz'

    elif config['car'] == 'num':
        caracteres = '0123456789'


    #Se ativado, adiciona a string na config.json na atual:
    if config['caresp']:
        caracteres = caracteres + str(config['caresp']) # type: ignore

    #Se ativado, substitui a string atual pela config.json:
    if config['pcar']:
        caracteres = config['pcar']
        
    return caracteres # type: ignore

#Função para detectar o SO do usuário, e aplica as condições.
#Para Windows, usa "cls", Linux e Mac, usa "clear".
def clear_os():
    sys_os = platform.system()
    
    if sys_os == 'Windows': 
        os.system('cls')
        key_os = '1'
        
    else:
        os.system('clear')
        key_os = '2'

#Função para testar todas as combinações com uma lista:
def permutacão(listap: list):
    lista_perm = list()
    
    padrao_perm = config['dperm']
    perm = permutations(listap, padrao_perm)

    for p in perm:
        lista_perm.append(''.join(p))
    
    with open('combinações.txt', 'a') as comb:
        for i in set(lista_perm):
            comb.write('\n' + i)

#Função para configurar o combesp em config.json:
def comb_esp(lista: list):
    lista_combesp = list()
    
    if config['combesp']['c']:
        care = config['combesp']['c']
        for i in lista:
            lista_combesp.append(care + i)
            
    if config['combesp']['f']:
        care = config['combesp']['f']
        for i in lista:
            lista_combesp.append(i + care)
            
    if config['combesp']['e']:
        care = config['combesp']['e']
        for i in lista:
            lista_combesp.append(i.replace(' ', care))
            
    with open('combinações.txt', 'a') as comb:
        for i in lista_combesp:
            comb.write('\n' + i)
            


#Função para selecionar o tipo de arquivos:
def sel_file():
    
    #Selecionando as palavras, sendo para selecionar um arquivo, ou manualmente:
    print('\033[38;5;122mDigite "F" para abrir um arquivo .txt com cada palvra em uma linha.')
    print('\033[38;5;122mDigite "M" digitar manualmente as palavras.')
    
    #Verifica se as opções são validas:
    while True:
        optxt = input('\033[38;5;99m').strip()
        if optxt != 'f' and optxt != 'F' and optxt != 'm' and optxt != 'M':
            print('\003[38;5;196mERROR: Opção invalida! Tente novamente! ')
        
        else:
            break
    
    #Modo manual iniciado:
    if optxt == 'm' or optxt == 'M':
        clear_os()
        print('''\n\033[38;5;80m[\033[38;5;106m+\033[38;5;80m]\033[38;5;208m Quais são as palavras a serem testadas? Separe por ";"

\033[38;5;214mExemplo:

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "As palvras são:\033[38;5;111m Macarrão, 2003, PSG."
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111mMacarrão ; 2003 ; PSG\033[38;5;208m
''')

        list_comb = input('\033[38;5;99m')
        #Tira espaço das palavras:
        list_comb = list_comb.replace(' ', '')
        #Transfroma em uma lista as palavras:
        list_comb = list_comb.split(';')
        
        
    #Modo de arquivo iniciado
    elif optxt == 'f' or optxt == 'F':
        clear_os()
        print('\033[38;5;184mQual seria o caminho até o seu .txt?\033[38;5;190m\nExemplo: C:/joao/desktop/minhas coisas/senhas.txt\n/home/desktop/pastalinux/senhas.txt\n')
        
        #Verifica se o path do .txt realmente existe:
        while True:
            path_txt = input('\033[38;5;99m')
            try:
                with open(path_txt) as arqT:
                    #Se tiver, transforma em uma lista:
                    listat = arqT.readlines()
                    list_comb = list()
                    #Retira todos os "\n" da lista, transformando em outra:
                    for i in listat:
                        list_comb.append(i.replace('\n', ''))

                    break
            
            except PermissionError:
                print('\033[38;5;196mERRO: Permisão negada ou caminho para um diretório, tente novamente! \n')
                    
            except FileNotFoundError:
                print('\033[38;5;196mERRO: Caminho errado, tente novamente!\n')
                
    #Se ativada, ativa a função temp(), em tempt.py:
    if config['tmp']:
        temp(list_comb) # type: ignore

    #Se não, so escreve em combinações.txt:
    else:
        with open('combinações.txt', 'a') as comb_ap:
            for c in list_comb: # type: ignore
                comb_ap.write(c + '\n')   

print('\n\033[38;5;157mConcluido! ')   

#Função para digitar no teclado as combinações em combinações.txt:
def bf_start(path_file='combinações.txt'):
    
    #Se tiver ativado, pedirá o usúario para digitar:
    if config['user']:
        usuario = config['user']
    
    #Confirma se o usuario quer continuar:
    while True:
        print('\n\033[38;5;203mDeseja continuar? [S/N]')
        comfirmação = input('\033[38;5;99m').strip().lower()
        
        if comfirmação == 'n' or comfirmação == 'nao' or comfirmação == 'não' or comfirmação == 'nn':
            #Ele quebra e sai do programa:
            exit()
        
        elif comfirmação == 's' or comfirmação == 'sim' or comfirmação == 'ss':
            clear_os()
            break
        
        else:
            print('\003[38;5;196mERROR: Opção invalida! Tente novamente! ') 
    
    #Detecda o SO do usuário, para aplicar as condições.
    #Na hora de apertar a tecla para comkeçar o Brute force, a quantidade de vezes que precisa aperatar é diferente para cada sistema:
    if platform.system() == 'Windows':
        key_os = '1x'
        
    else:
        key_os = '2x'
    
    
    #Pede para selecionar a tecla configurada para iniciar:
    print(f'\033[38;5;27mPara iniciar, aperte {key_os} a tecla "{str(config.get("kini", "f9")).capitalize()}"! ')
    print('\033[38;5;27mPara interromper, aperte Ctrl + C no Terminal! ')
    
    try:
        sleep(1)
        #Pega a tecla no config.json
        key_config = key_dic.get(config['kini'], keyboard.Key.f9)
        
        #Verifica se a tecla foi pressionada para começar:
        def tecla_pressionada(key):
            if key == key_config:
                print("\033[38;5;114mIniciado com sucesso! ")
                listener.stop()
        
        #Cria uma variavel quer vai receber a tecla, e veificar se é True ou False:
        listener = keyboard.Listener(on_release = tecla_pressionada)
        #Inicia o mapeamento
        listener.start()
        #Mapea a tecla até ser pressionada:
        listener.join()
            
            
        #Pega cada linha do combinações.txt para digitar:
        with open(path_file, 'r') as comb_read:
            tentativas = comb_read.read().split('\n')
        
        for i in tentativas:
            
            #Se ativado, digitara o úsuario e pressionará enter:
            if config['user']:
                pyautogui.write(usuario) # type: ignore
                pyautogui.press('enter')
                
                if config['denter']['u']:
                    pyautogui.press('enter')
                #Espera o tempo configurado:
                sleep(float(config['ktime']['u']))

            #Digitando uma combinação:
            pyautogui.write(i)
            pyautogui.press('enter')
            
            if config['denter']['s']:
                    pyautogui.press('enter')
            #Espera o tempo configurado:
            sleep(float(config['ktime']['s']))
            
        print('\n\033[35mBrute Force concluido com sucesso! ')
        print('\033[38;5;24mSaindo...')
        sleep(2)
        print('\033[38;5;120mVolte Sempre! ')    
        clear_os()
        #Ele quebra e sai do programa:
        exit()  
    
    except KeyboardInterrupt:
        clear_os()
        print('\033[38;5;120mVolte Sempre! ')
    
def bf_config():
    
    clear_os()
     #Mostrando como se usa o sistema de caracteres: 
    print('''\n\033[38;5;80m[\033[38;5;106m+\033[38;5;80m]\033[38;5;208m Quantos caracteres tem sua senha?

\033[38;5;214mExemplo:

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "Tenho certeza que a senha tem \033[38;5;111m12\033[38;5;208m caracteres!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111m12\033[38;5;208m

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "Tenho certeza que tem no MÁXIMO \033[38;5;111m18\033[38;5;208m caracteres!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111m| 18\033[38;5;208m

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "Tenho certeza que tem no MÍNIMO \033[38;5;111m6\033[38;5;208m caracteres!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111m6 |\033[38;5;208m

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "Tenho certeza que tem no MÍNIMO \033[38;5;111m8\033[38;5;208m caracteres, e no MÁXIMO \033[38;5;111m16\033[38;5;208m caracteres!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111m8 | 16\033[38;5;208m

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "Não faço a menor ideia da \033[38;5;111mquantidade\033[38;5;208m de caracteres!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111m*

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m"Quero  \033[38;5;111mPULAR\033[38;5;208m esta etapa!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111m_''')              
        
    #Calculando o número de caracteres: 
    while True:
        
        #Retira todos os espaços:
        chave_caracteres = input('\n\033[38;5;99m')
        chave_caracteres = chave_caracteres.replace(' ','')
        
        #Se a entrada for "_", carregará os dados salvos em config.json:
        minimo_caracteres = config['carmin']
        maximo_caracteres = config['carmax']

        #Se todos os caracteres forem numerais, ele ja define:
        if chave_caracteres.isnumeric():
    
            minimo_caracteres = int(chave_caracteres)
            maximo_caracteres = int(chave_caracteres)
            break
            
        #Se encontrar a barra vertical, calculo o mínimo e máximo de caracteres:
        elif '|' in chave_caracteres:
            
            #Tenta encontrar o número antes da barra:
            try:
                minimo_caracteres = int(chave_caracteres[: chave_caracteres.find('|')])

            #Se não tiver, define por padrão o mínimo configurado em config.json:
            except ValueError:
                minimo_caracteres = config['minp']

            #Tenta encontrar o número depois da barra:
            try:    
                maximo_caracteres = int(chave_caracteres[chave_caracteres.find('|') + 1 :])
                break
                
            #Se não tiver, define por padrão o máximo configurado em config.json:
            except ValueError:
                maximo_caracteres = config['maxp']
                break
    
        #Se receber o "*", definirá os dois valores de padrão em config.json:
        elif chave_caracteres == '*':
            
            maximo_caracteres = config['maxp']
            minimo_caracteres = config['minp']
    
        else:
            print('\033[38;5;196mERROR: Nenhum número foi digitado! Tente novamente! ')
    
    #Salva as alterções na varialvel config:
    config.update({'carmin' : minimo_caracteres})
    config.update({'carmax' : maximo_caracteres})
    clear_os()
    

    #Mostra quais tipos de caracteres vai ter na senha:
    print('''\n\033[38;5;80m[\033[38;5;106m+\033[38;5;80m]\033[38;5;208m Quais caracteres tem sua senha?

\033[38;5;214mExemplo:

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "A minha senha só vai ter \033[38;5;111mLETRAS\033[38;5;208m do alfabeto!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111mLet\033[38;5;208m

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "A minha senha só vai ter \033[38;5;111mNÚMEROS\033[38;5;208m de 0-9!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111mNum\033[38;5;208m

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "A minha senha vai ter \033[38;5;111mletras e números\033[38;5;208m"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111mletnum\033[38;5;208m

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "A minha senha vai ter \033[38;5;letras, números e caractéres especiais\033[38;5;208m!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111mltnum !;_ (Coloque os caracteres que deseja)\033[38;5;208m

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "Quero selecionar eu mesmo os caracteres \033[38;5;111mDESEJADOS\033[38;5;208m!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111mcar G4& (Coloque os caracteres que deseja)

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m"Quero  \033[38;5;111mPULAR\033[38;5;208m esta etapa!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111m_''')     


    #Calculando quais serão os caracteres: 
    while True:
        
        #Retira todos os espaços:
        caracteres_input = input('\n\033[38;5;99m').lower().strip().split()
        
        #Calcula a saída:
        if caracteres_input == '_':
            alfa()
            break
            
        elif caracteres_input[0] == 'let':
            config.update({'car': 'lt'})
            if len(caracteres_input) == 2:
                config.update({'caresp': caracteres_input[1]})
                
            else:
                config.update({'caresp': False})
                
            config.update({'pcar': False})
            break
        
        
        elif caracteres_input[0] == 'num':
            config.update({'car': 'num'})
            if len(caracteres_input) == 2:
                config.update({'caresp': caracteres_input[1]})
            
            else:
                config.update({'caresp': False})
                
            config.update({'pcar': False})
            break
            
        elif caracteres_input[0] == 'letnum':
            config.update({'car': 'ltnum'})
            if len(caracteres_input) == 2:
                config.update({'caresp': caracteres_input[1]})
                
            else:
                config.update({'caresp': False})
                
            config.update({'pcar': False})
            break
            
        elif caracteres_input[0] == 'car':
            config.update({'pcar': caracteres_input[1]})
            break
        
        else:
            print('\033[38;5;196mERRO: Comando inválido, tente novamente!')
    
    #Depois salva e carrega o json:
    salvar_json(config)
    carregar_json(config)



#Função inicia o processo "cru" do Brute Force Raiz:
def bf_raiz():
    global resultado, tasks
    
    #Iniciando o processo de escrever em combinações.txt todas as combinações geradas:        
    #Processando as configurações:

    #Carrega o maximo e minimo de caracteres
    max_caractere = config['carmax']
    min_caractere = config['carmin']
    
    #Faz um calculo básico para saber as possibilidades de senhas: 
    for i in range(min_caractere, max_caractere + 1):
        resultado += len(alfa()) ** i

    #Se ativado, dobra as possibilidades:
    if config['ltm']:
        resultado *= 2

    #Gerando as combinações (Código retirado do Chat GPT):
    
    #Cria uma função que de entrada usa os caracteres, o tamanho mínimo e o tamanho máximo:
    def test_combinations(string: str, min_length: int, max_length: int, tasks: int):
        combinations = list()
        
        #Passa por cada letra formando cada possibilidade, depois junta e adiciona a lista, logo adiciona 1 em tasks:
        for length in range(min_length, max_length + 1):
            for combo in product(string, repeat=length):
                if tasks >= config['limit']:
                    print('\033[38;5;124mSOBRECARGA: O limite em "config.json" foi ultrapassado! Se quiser continuar, redefine as configurações! Atual limite de combinações: ', config['limit'])
                    exit()
                combinations.append(''.join(combo))
                tasks += 1
            
            #Calcula o resto da divisão para diminuir as chances de imprimir a tela de carregamento:
            if tasks % 5 == 0:
                print(f'\r\033[38;5;35m{tasks / resultado * 100:.2f}% ', end='')
        
        return combinations

    combinations = test_combinations(alfa(), min_caractere, max_caractere, tasks)

    #Escreve todas as combinações da lista em combinações.txt:
    for combo in combinations:
        
            with open('combinações.txt','a') as combinação:
                    combinação.write(combo + '\n')
            tasks += 1
            
            #Se tiver ativado, escreve em dobro, só que captalizada:
            if config['ltm']:
                with open('combinações.txt','a') as combinação:
                    combinação.write(str(combo).title() + '\n')
                    tasks += 1
            
            #Calcula o resto da divisão para diminuir as chances de imprimir a tela de carregamento:
            if tasks % 5 == 0:
                print(f'\r\033[38;5;35m{tasks / resultado * 100:.2f}% ', end='')
            
    #Depois de concluido, limpa a lista:
    combo, combinations = None, None
    print('\n\033[38;5;157mConcluido! ')
    

    #Inicia a digitar no teclado:
    bf_start()
            
            
            
#Função inicia o processo "cru" do Brute Force Combinações:
def bf_comb():
    #Define a a lista com tudo oque esta no combinações.txt:
    with open('combinações.txt') as comb:
        comb_read = comb.read().split('\n')
    
    clear_os()
    
    #Define quais palavras vai escolher:
    sel_file()
    
    print('\033[38;5;60mConcluído, Carregando as configurações...')
            
    #Cria todas as combinações dadas no combinações.txt:
    with open('combinações.txt') as comb:
        comb_read = comb.read().split('\n')
    permutacão(comb_read)

    
    #Define se vai adicionar mais combinações de senhas com caracteres a mais:
    with open('combinações.txt') as comb:
        comb_read = comb.read().split('\n')
    comb_esp(comb_read)

    #Limpa a váriavel:
    comb_read = list()
    
    #Iniciando para digitar no teclado:
    bf_start()



#Função inicia o processo "cru" do Brute Force Aleatorio:
def bf_aleat():
    #Configurando os caracteres:
    bf_config()
    maximo_caracteres = config['carmax']
    minimo_caracteres = config['carmin']
    
    #Definindo o numero de senhas:
    while True:
        
        #Selecionando a quantidade de senhas:
        print('\n\n\033[38;5;159mQuantas senhas pretente criar?')
        try:
            nsenhas = int(input('\033[38;5;196m'))
            break
        except ValueError:
            print('\033[38;5;196mERRO: Digíto invalido, tente novamente!')
    
    #Gerando as senhas:
    count = 0
    senhas = list()
    while count != nsenhas:
        
        #Gerando os dígitos aleatórios:
        for n in range(minimo_caracteres, maximo_caracteres + 1):
            
            senhaT = random.choices(alfa(), k=n)
            senhas.append(''.join(senhaT))
            count += 1
    
    #Escrevendo as senhas:
    with open('combinações.txt', 'a') as  comb_ap:
        for app in senhas:
            comb_ap.write('\n' + app)
    

    #Digitando as senhas:
    bf_start()


#Função inicia o processo "cru" do Brute Force Dicionário:
def bf_dicio():
    #Definindo o numero de senhas:
        while True:
            
            #Selecionando a quantidade de senhas:
            print('\n\n\033[38;5;159mQuantas senhas pretente criar?')
            
            try:
                nsenhas = int(input('\033[38;5;196m'))
                break
            
            except ValueError:
                print('\033[38;5;196mERRO: Digíto invalido, tente novamente!')
        

        #Escolhendo as palavras e escrevendo:
        senhas = list()
        car_separador = config['diccar']
        for n in range(nsenhas):
            
            #Cria "x" combinações, dada pelo usuário. Vem de fábrica, capitalizada:
            senhaT = random.choices(dic_lang(), k=config['dicnum'])
            senhas.append(car_separador.join(senhaT))
            
            #Abre as configurações, e adiciona a lista se tivver como maiúsculo ou minúsculo:
            if config['diclet'] == 'all':
                senhas.append(str(car_separador.join(senhaT)).capitalize())
                senhas.append(str(car_separador.join(senhaT)).upper())
                
            elif config['diclet'] == 'mai':
                senhas.append(str(car_separador.join(senhaT)).upper())

                
            elif config['diclet'] == 'cap':
                senhas.append(str(car_separador.join(senhaT)).capitalize())
                                
                
        with open('combinações.txt', 'a') as comb_app:
            for app in senhas:
                comb_app.write('\n' + app)
        
        bf_start()



#Função inicia o processo "cru" do Brute Force Digitar automaticamente:
def bf_digit():
    print('\n\033[38;5;69mDigite o caminho até o arquivo:')
    while True:
        path_txt = input('\033[38;5;99m').strip()
        
        try:
            #Criando um arquivo "ca1che" para ver se a pasta realmente existe:
            with open(path_txt,'r', encoding='utf-8') as text:
                text_read = text.read().split('\n')
                
                for i in text_read:
                    if i == '':
                        text_read.remove(i)   
                
                break
                
        except FileNotFoundError:
            print('\n\033[38;5;124mCaminho mal-sucedido! Tente novamente!')
            
    bf_start(path_file=path_txt)

#Limpando o terminal de acordo com o sistema operacional:
clear_os()

#Imprimindo as logos:
print(f'\033[31m{logo_blood}\033[m',end='')
print(f'\033[32m{logo_force}\033[m')
print('\033[35mBy: Arthur Speziali! \033[m')
for quebra_linha in range(3):
    print('\n')

#Menu da interface:
while True:
    print('''\033[38;5;60mSelecione a interface desejada:
          \033[38;5;216m
          \033[38;5;140m[1]-\033[38;5;216m Interface simples: 
          \033[38;5;140m[2]- \033[38;5;216mInterface de comando:
          \033[38;5;140m[3]- \033[38;5;216mSobre: 
          \033[38;5;140m[4]- \033[38;5;216mSair:
          ''')
    
    try:
        #Verificando se a opção é valida:
        opção1 = int(input('\033[38;5;99m'))
        if opção1 > 4 and opção1 != 88 or opção1 < 1:
            print('\033[38;5;196mERROR: A opção digita é inválida! Tente novamente!\n')
        
        else:
            break
    
    except ValueError:
        print('\033[38;5;196mERROR: A opção digitada não é um número! Tente novamente!\n')
        
clear_os()

#Modo Desenvolvedor:
if opção1 == 88:
    print('\033[38;5;34m=-=-=Bem vindo ao modo DEV!=-=-\033[m')
    print('ALFA: ', alfa())
    print('TYPE: ', type(alfa()))
        

#Interface simples selecionada:
elif opção1 == 1:
            
    #Menu principal:
    while True:

        #Menu para escolher o tipo de Brute Force:
        print('''\n\033[38;5;124mSeja Bem-Vindo ao \033[31mBlood\033[32mForce\033[38;5;124m, um Sofware de Brute-force! 
Selecione a opção abaixo desejada:

        \033[38;5;140m[1]-\033[92m Brute Force Raiz:
        \033[38;5;140m[2]-\033[92m Brute Force com várias combinações de senhas:
        \033[38;5;140m[3]-\033[92m Brute Force com várias tentativas de senhas:
        \033[38;5;140m[4]-\033[92m Brute Force com dígitos aleatórios: 
        \033[38;5;140m[5]-\033[92m Brute Force com palavras do dícionario aleatórios:
        \033[38;5;140m[6]-\033[92m Digitar automaticamente:
        \033[38;5;140m[7]-\033[92m Configurações avançadas:
        \033[38;5;140m[8]-\033[92m Sair:
        \033[m
        ''')
        
        #Verifica se a opção é valida:
        try:
            opção2 = int(input('\033[38;5;99m'))
            if opção2 > 8 or opção2 < 1:
                print('\033[38;5;196mERROR: A opção digita é inválida! Tente novamente!\n')
            
            else:
                break
        
        except ValueError:
            print('\033[38;5;196mERROR: A opção digitada não é um número! Tente novamente!\n')
    
    #Brute Force Raiz iniciado:
    if opção2 == 1:
        print('\033[38;5;24mIniciando Brute Force Raiz... ')
        print('''\033[38;5;22mO Brute Force Raiz, usa todas as combinções de senhas possíveis! 
Sem nenhuma orientação!''')
        sleep(2)
        
        bf_config()
       
        #Gerando todas as combinações:
        print('''\033[38;5;226mATENÇÃO: Você precisa configurar as opções no menu anterior!
Caso queira configurar, aperte\033[38;5;33m CTRL + C\033[38;5;226m para sair do programa! ''')
        sleep(3)
        
        #Inicia todo o Brute Force:
        bf_raiz()        
        
    
    #Brute Force com combinações iniciado:
    elif opção2 == 2:
        print('\033[38;5;24mIniciando Brute Force com várias combinações de senhas... ')
        print('''\033[38;5;22mO Brute Force com várias combinações de senhas, usa combinações de senhas com
palavras-chaves dada pelo úsario!''')   
        sleep(2)

        bf_comb()
        
    #Brute Force com tentativas iniciado:
    elif opção2 == 3:
        print('\033[38;5;24mIniciando Brute Force com várias tentativas de senhas... \n')    
        print('''\033[38;5;22mO Brute Force com várias tentativas de senhas, usa como senha as 
palavras-chaves dada pelo úsario!''')   
        sleep(2)

        #Define quais palavras vai escolher:
        sel_file()
        
        #Começa a digitar no teclado:
        bf_start()
        
        
    #Brute com digitos aleatorios iniciado:
    elif opção2 == 4:
        print('\033[38;5;24mIniciando Brute Force com vários digítos aleatórios... \n')
        print('''\033[38;5;22mO Brute Force com vários dígitos aleatórios, digita senhas
totalmente aleatórias!''')      
        sleep(2)
        
        bf_aleat()

    #Brute Force com palavras do dicionário:
    elif opção2 == 5:
        print('\033[38;5;24mIniciando Brute Force com palavras do dicionário... \n')
        print('''\033[38;5;22mO Brute Force com palavras do dicionário, usa palavras
do dicionário PT/EN para criar novas senhas!''')      
        sleep(2)
        
        clear_os()
        while True:
            
            print('''\n\033[38;5;80m[\033[38;5;106m+\033[38;5;80m]\033[38;5;208m Quais dicionários você que para a senha?

\033[38;5;214mExemplo:

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "Quero as palavras em \033[38;5;111mPORTUGUÊS\033[38;5;208m!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111mPT\033[38;5;208m

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "Quero as palavras em \033[38;5;111mINGLÊS\033[38;5;208m!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111mEN\033[38;5;208m

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m "Quero prieiro as palavras em \033[38;5;111mINGLÊS & PORTUGUÊS\033[38;5;208m!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111mEN-PT\033[38;5;208m

\033[38;5;80m[\033[38;5;130m-\033[38;5;80m]\033[38;5;208m"Quero  \033[38;5;111mPULAR\033[38;5;208m esta etapa!"
\033[38;5;80m[\033[38;5;75mI\033[38;5;80m]\033[38;5;208m Entrada: \033[38;5;111m_
''')        
            #Calculando a saída dos dicionários:
            lingua = input('\033[38;5;99m').lower()
            lingua = lingua.replace(' ', '')
            if lingua != '_' and lingua == 'en' or lingua == 'pt' or lingua == 'pt-en' or lingua == 'en-pt':
                print('\033[38;5;148mCarregando, aguarde, são muitas palavras!')
            
            if lingua == 'pt':
                config.update({'lang': 'pt'})
                break
                
            elif lingua == 'en':
                config.update({'lang': 'en'})
                break
                
            elif lingua == 'pt-en' or lingua == 'en-pt':
                config.update({'lang': 'enpt'})
                break
                
            elif lingua == '_':
                break
            
            else:
                print('\033[38;5;196mERRO: Opção inválida, tente novamente!')
                
                
        bf_dicio()
            
    
    elif opção2 == 6:
        print('\033[38;5;24mIniciando Digitação automática... Aperte CTRL + C para sair! ')
        print('''\033[38;5;22mA Digitação automática abre o arquivo do usuário e digita linha
por linha, usando as configurações do programa.''')      
        sleep(2)
        
        clear_os()
        
        bf_digit()
    
    #Configurações avançadas iniciado:
    elif opção2 == 7:
            print('\033[38;5;24mIniciando Configurações avançadas... Aperte CTRL + C para sair! ')    
            sleep(2)
            clear_os()
            #Executa a função "comand_line()" em comand_line.py:
            comand_line()
    
    #Sair iniciado:
    elif opção2 == 8:
        print('\033[38;5;24mSaindo...')
        sleep(2)
        print('\033[38;5;120mVolte Sempre! ')
        #Ele quebra e sai do programa:
        exit()
        
        
elif opção1 == 2:
    clear_os()
    while True:
        print('\033[38;5;76mLinha de comando Ativo:\n\n')
        
        try:
            cmd = input('\033[38;5;99m').strip().lower()
            
            if cmd == 'dump':
                clear_os()
            
            elif cmd == 'root':
                bf_raiz()
                
            elif cmd == 'comb':
                bf_comb()
                
            elif cmd == 'temp':  
                sel_file()
                bf_start()

            elif cmd == 'rndm':
                bf_aleat()
                
            elif cmd == 'dict':
                bf_dicio()
                
            elif cmd == 'auto':
                bf_digit()
            
            elif cmd == 'help':
                print(help_bt)
                
            elif cmd == 'conf':
                clear_os()
                print('Configurações iniciadas (Aperte CTRL + C para sair):\n\n')
                
                comand_line()
                    
            else:
                print('\033[38;5;160mComando inválido! Tente novamente ou digite "help" para obter ajuda.\n')
            
        except KeyboardInterrupt:
            clear_os()
            print('\033[38;5;120mVolte Sempre! ')
            exit()
                    
        

#Sobre o criador:
elif opção1 == 3:
    print('''\033[38;5;66mPrograma Python, Open Source.
\033[38;5;209mCompativel com todos os Sistemas Operacionais, mas pensado para se usar no Linux.
\033[38;5;150mCriado por: Arthur Speziali:
\033[38;5;45mFeito com intuidos educacionais! O dono não se responsabiliza por qualquer ato ilegal!
\033[38;5;170mVersão: 1.0          
''')

#Saindo:
elif opção1 == 4:
    print('\033[38;5;24mSaindo...')
    sleep(2)
    print('\033[38;5;120mVolte Sempre! ')
    #Ele quebra e sai do programa:
    exit()
