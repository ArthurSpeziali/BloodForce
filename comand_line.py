import json

#Ceiando função de salvar o .json:
def salvar_json(config):
    with open('config.json', 'w') as config_json:
        json.dump(config, config_json)

#Cria função de carregar o .json:
def carregar_json(config):   
    with open('config.json') as config_json:
        config = json.load(config_json)
    return config

#Abre as configurações:
with open('config.json') as config_json:
        config = json.load(config_json)


#Cria a string para ajuda nas configurações e no Brute Force:
help_bt = """
\033[1m\033[38;5;202mINICIALIZAÇÃO:\033[m

\033[38;5;140mdump \033[92m=Limpa o terminal

\033[38;5;140mroot \033[92m=Inicia o Brute Force Raiz.

\033[38;5;140mcomb \033[92m=Inicia o Brute Force com várias combinações de senhas.

\033[38;5;140mtemp \033[92m=Inicia o Brute Force com várias tentativas de senhas.

\033[38;5;140mrndm \033[92m=Inicia o Brute Force com dígitos aleatórios.

\033[38;5;140mdict \033[92m=Inicia o Brute Force com palavras do dícionario aleatórios.

\033[38;5;140mauto \033[92m=Inicia o Digitar automaticamente.

\033[38;5;140mconf \033[92m=Inicia o Configurações Avançadas.

\033[38;5;140mhelp \033[92m=Exibi este painel de ajuda.
"""



help_config = """
\033[1m\033[38;5;202mCONFIGURAÇõES:\033[m

\033[38;5;140m-car \033[92m= Altera o tipo de caractere (Letra, número, letra e numero) do Brute Force Raiz:
                    \033[38;5;220m-lt (Letra), -num (Número), -ltnum (Letra e número).

\033[38;5;140m-ltm \033[92m= Cria e coloca a 1º letra em maiusculo nas combinações:
                    \033[38;5;220mTrue (Ativa), False (Desativa).

\033[38;5;140m-caresp \033[92m= Permiti colocar caracteres especiais a mais:
                    \033[38;5;220m!@#... (Coloque os caracteres que desejar), False (Desativa).
                    
\033[38;5;140m-user \033[92m= Se ativado, o programa colocará o usuario toda vez que a senha for colocada:
                    \033[38;5;220mFalse (Desativa), QuikSilver345 (Especifique o úsuario).

\033[38;5;140m-carmax \033[92m= Define os caracteres máximo padrão (Padrão de fábrica: 24):
                    \033[38;5;220m32 (Somente colocolar o numero desejado).

\033[38;5;140m-carmin \033[92m= Define os caracteres mínimo padrão (Padrão de fabrica: 8):
                    \033[38;5;220m12 (Somente colocar o número desejado).        
                    
\033[38;5;140m-maxp \033[92m= Define o padrão de digitos máximos da senha se não for especificado no Brute Force Raiz:
                    \033[38;5;220m24 (Defina o valor, Padrão: 16)
                    
\033[38;5;140m-minp \033[92m= Define o padrão de digitos mínimos da senha se não for especificado no Brute Force Raiz:
                    \033[38;5;220m6 (Defina o valor, Padrão: 4)

\033[38;5;140m-limit \033[92m= Define o limite de tentativas do Brute Force Raiz e do Digítos aleatórios:
                    \033[38;5;220m150 (Padrão de fábrica: 500 Mil).
                    
\033[38;5;140m-numdic \033[92m= Coloca números no final e começo da palavra no Brute Force com dicionário:
                    \033[38;5;220m-c (No começo), -f (No fim), -cf (No começo e no fim), False (Desativa).
                    \033[38;5;131m2 (Se ativado, especifica o número de numeros que vai ter);
                    
\033[38;5;140m-pcar \033[92m= Personalize os caracteres a serem utilizados:
                    \033[38;5;220mFalse (Desativa), abc!@#789 (Somente colocar os caracteres desejados).
                    
\033[38;5;140m-dump \033[92m= Ao iniciar o programa, ele exclui todas as combinações guardadas anteriormente (combinações.txt):
                    \033[38;5;220mTrue (Ativa), False (Desativa).
                    
\033[38;5;140m-kini \033[92m= Redefine a tecla padrão para iniciar o Brute Force (Somente teclas de função!):
                    \033[38;5;220mpage_down (Somente colocar a tecla desejada).
                    
\033[38;5;140m-ktime \033[92m= Altera o tempo para tentar novamente (Padrão de fábrica: 0.01):
                    \033[38;5;220m-u (Para colocar no usúario), -s (Para colocar na senha), False (Desativa o tempo).
                    \033[38;5;131m5 (Ele esperara 5 segundos!);
                 
\033[38;5;140m-tmp \033[92m= Especifica se em alguns Brute Forces vai alterar a entrada, colocando mais combinções. Exemplo: I:senha 123; O:Senha123, Senha_123, SENHA123... etc (Padrão: False):
                   \033[38;5;220mFalse (Desativa), True (Ativa).

\033[38;5;140m-denter \033[92m= Escolha se quiser dar um duplo enter na hora de digitar a senha:
                      \033[38;5;220m-u (Para colocar no usúario), -s (Para colocar na senha), -su (Para colocar no usuario e senha), False (Desativa o double enter).
                      \033[38;5;131mTrue (Ativa), False (Desativa);
                      
\033[38;5;140m-combesp \033[92m= Se tiver no Brute Force com várias Combinações de senhas, adcionará caracteres especiais para tentar nas combinações.
                       \033[38;5;220m-c (Para colocar estes caracteres no começo), -f (Para colocar no fim), -e (Para colocar nos espaços)
                       \033[38;5;131mFalse (Desativa), &!_ (Especifique os carácteres):
                       
\033[38;5;140m-dperm \033[92m=Define o padrão para quantas palavras vai ter por senha no Brute Force com combinações e no palavras do dicionario (Padrão de fábrica: 2):
                     \033[38;5;220m3(Especifica o numero! PERIGO: Não coloque numeros altos, se não quiser explodir seu computador!).
                     
\033[38;5;140m-lang \033[92m=Define qual idioma será o dicionário no Brute Force com palavras do dicionário:
                    \033[38;5;220m-pt (Para português), -en (Para inglês), -enpt (Paa inglês e português).     
                     
\033[38;5;140m-dicnum \033[92m=Define o padrão do número de palavras em cada senha do Brute Force com dicionário (Padrão de fábrica: 2):
                      \033[38;5;220m3 (Específique o número!)
                      
\033[38;5;140m-diccar \033[92m=Define qual caractere deve separar as palavras na senha do Brute Force dicionário:
                      \033[38;5;220mFalse (Coloca nada entre), _ (Específique o caráctere!).
                      
\033[38;5;140m-diclet \033[92m=Define se vai adicionar a palavra do dicionário do Brute Force dicionário em maiúsculo ou/e capitalizada:
                      \033[38;5;220mFalse (Deixa somente o minúsculo), -cap (Adiciona a palavra em capital), -mai (Adciona a palavra em maiúsculo), -all (Adiciona nos 2 modos).
"""

#Cria um dicionario para verificar se o comando "-kini" está correto antes de salvar no .json:     
key_list = [
    'f1',
    'f2',
    'f3',
    'f4',
    'f5',
    'f6',
    'f7',
    'f8',
    'f9',
    'f10',
    'f11',
    'f12',
    'esc',
    'alt',
    'alt_gr',
    'caps_lock',
    'backspace',
    'ctrl',
    'shift',
    'delete',
    'down',
    'enter',
    'end',
    'home',
    'insert',
    'left',
    'page_down',
    'page_up',
    'scroll_lock',
    'right',
    'print_screen',
    'up',
    'space',
    'tab'
]

#Cria a função de verificar se o comando está certo, e altera a config.json, usado no BloodForce.py:
def comand_line():
    
    while True:
        error = 0
        cmd = input('\033[1m\033[38;5;124m').strip().lower().split()
        print('\033[m')
        
        try:
            if cmd[0] == '-car':
                if cmd[1] == '-lt':
                    config.update({'car': 'lt'})
                elif cmd[1] == '-num':
                    config.update({'car': 'num'})
                elif cmd[1] == '-ltnum':
                    config.update({'car': 'ltnum'})
                else:
                    print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n')
                    error = 1

            elif cmd[0] == '-ltm':
                if cmd[1] == 'true':
                    config.update({'ltm': True})
                elif cmd[1] == 'false':
                    config.update({'ltm': False})
                else:
                    print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n')
                    error = 1

            elif cmd[0] == '-caresp':
                if cmd[1] == 'false':
                    config.update({'caresp': False})
                else:
                    config.update({'caresp': cmd[1]})

            elif cmd[0] == '-user':
                if cmd[1] == 'false':
                    config.update({'user': False})
                    
                else:
                    config.update({'user': str(cmd[1])})


            elif cmd[0] == '-carmax':
                config.update({'carmax': int(cmd[1])})
                            
            elif cmd[0] == '-carmin':
                config.update({'carmin': int(cmd[1])})

            elif cmd[0] == '-limit':
                config.update({'limit': int(cmd[1])})

            elif cmd[0] == '-numdic':
                if cmd[1] == 'false':
                    config.update({'numdic': False})
                elif cmd[1] == '-c':
                    config.update({'numdic': {'pos': 'c', 'carnum': int(cmd[2])}})
                    
                elif cmd[1] == '-f':
                    config.update({'numdic': {'pos': 'f', 'carnum': int(cmd[2])}})
                    
                elif cmd[1] == '-cf':
                    config.update({'numdic': {'pos': 'cf', 'carnum': int(cmd[2])}})
                
                else:
                    print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n')
                    error = 1

            elif cmd[0] == '-pcar':
                if cmd[1] == 'false':
                    config.update({'pcar': False})
                else:
                    config.update({'pcar': cmd[1]})

            elif cmd[0] == '-dump':
                if cmd[1] == 'false':
                    config.update({'dump': False})
                elif cmd[1] == 'true':
                    config.update({'dump': True})
                else:
                    print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n')
                    error = 1

            elif cmd[0] == '-kini':
                if cmd[1] in key_list:
                    config.update({'kini': cmd[1]})
                    
                else:
                    print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n')
                    error = 1

            elif cmd[0] == '-ktime':
                if cmd[1] == '-u':
                    config.update({'ktime': {'u': float(cmd[2])}, {'s': config['ktime']['s']}})
                    
                elif cmd[1] == '-s':
                    config.update({'ktime': {'s': float(cmd[2])}, {'u': config['ktime']['u']}})
                    
                else:
                    print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n')
                    error = 1

            elif cmd[0] == '-h':
                print(help_config + '\n')
                
            elif cmd[0] == '-tmp':
                if cmd[1] == 'true':
                   config.update({'tmp': True})
                   
                elif cmd[1] == 'false':
                   config.update({'tmp': False})

                else:
                    print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n')
                    error = 1

            elif cmd[0] == '-denter':
                if cmd[1] == '-u':                    
                    if cmd[2] == 'true':
                        config.update({'denter': {'u': True}, {'s': config['denter']['s']}})
                    
                    elif cmd[2] == 'false':
                        config.update({'denter': {'u': False}, {'s': config['denter']['s']}})
                        
                    else:
                        print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n')
                        error = 1
                
                elif cmd[1] == '-s':
                    if cmd[2] == 'true':
                        config.update({'denter': {'s': True}, {'u': config['denter']['u']}})
                    
                    elif cmd[2] == 'false':
                        config.update({'denter': {'s': False}, {'u': config['denter']['u']}})
                        
                    else:
                        print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n')
                        error = 1
                        
                elif cmd[1] == '-su':
                    if cmd[2] == 'true':
                        config.update({'denter': {'s': True}, {'u': True}})
                    
                    elif cmd[2] == 'false':
                        config.update({'denter': {'s': False}, {'u': False}})
                        
                    else:
                        print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n')
                        error = 1
                    
                else:
                    print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n')
                    error = 1

            elif cmd[0] == '-maxp':
                config.update({'maxp': int(cmd[1])})
                
            elif cmd[0] == '-minp':
                config.update({'minp': int(cmd[1])})
                
            elif cmd[0] == '-combesp':
                if cmd[1] == '-c':
                    if cmd[2] == 'false':
                        config.update({'combesp': {'c': False}})
                                      
                    else:
                        config.update({'combesp': {'c': cmd[2]}})
                                      
                elif cmd[1] == '-f':
                    if cmd[2] == 'false':
                        config.update({'combesp': {'f': False}})
                        
                    else:
                        config.update({'combesp': {'f': cmd[2]}})

                elif cmd[1] == '-e':
                    if cmd[2] == 'false':
                        config.update({'combesp': {'e': False}})
                        
                    else:
                        config.update({'combesp': {'e': cmd[2]}})
                        
                else:
                    print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n ')
                    error = 1
                    
            elif cmd[0] == '-dperm':
                config.update({'dperm': int(cmd[1])})
                
            elif cmd[0] == '-lang':
                if cmd[1] == 'pt':
                    config.update({'lang': 'pt'})
                    
                elif cmd[1] == 'en':
                    config.update({'lang': 'en'})
                
                elif cmd[1] == 'enpt':
                    config.update({'lang': 'enpt'})
                    
                else:
                    print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n ')
                    error = 1
                    
            
            elif cmd[0] == '-dicnum':
                config.update({'dicnum': int(cmd[1])})
                
            elif cmd[0] == '-diccar':
                if cmd[1] == 'false':
                    config.update({'diccar': ''})
                    
                else:
                    config.update({'diccar': cmd[1]})
                    
                    
            elif cmd[0] == '-diclet':
                if cmd[1] == 'false':
                    config.update({'diclet': False})
                    
                elif cmd[1] == 'all':
                    config.update({'diclet': 'all'})
                    
                elif cmd[1] == '-cap':
                    config.update({'diclet': 'cap'})
                    
                elif cmd[1] == '-mai':
                    config.update({'diclet': 'mai'})                                        
                    
                else:
                    print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n ')
                    error = 1
            
            elif cmd[0] == 'exit':
                break
            
            else:
                print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n ')
                error = 1
                
            if error == 0:
                salvar_json(config)
                print('\033[38;5;243mComando Sucedido! \n')
        
        except:
            print('\033[38;5;160mComando inválido! Tente novamente ou digite "-h" para obter ajuda ou digite "exit" para sair.\n ')
            error = 1
