import matplotlib.pyplot as plt  # <-------APAGUE A PRIMEIRA TRALHA SE FOR O CASO DE VOCÊ MEXER NO CÁDIGO AFIM DE UTILIZAR O MATPLOTLIB...
import time as t
import random as ran

reset = False
while reset == False:

    print('-' * 50)
    print('PROGRAMA DE PRÁTICA DE DIGITAÇÃO:')
    print('-' * 50)
    print('\nSeja bem vindo.\nO objetivo do jogo é escrever corretamente as frases que aparecerem no menor tempo possível.\nO jogo vai começar.')

    ##----------------------------------------------------------------------
    ## Essa lista 'frases' possui 30 frases diferentes até o momento.
    frases = ['Dobby é um elfo livre!', 'A antigravitação dos jogadores de basket é uma loucura.',
              'Wingardium Leviosa é um feitiço para iniciantes. Eu acho...',
              'Aprende a escrever na areia da praia o que é melhor esquecer. Frase de Malba Tahan',
              'Um bolinho de chocolatinho muito do gostosinho.', 'Um bolinho de chocolate muito do gostosinho.',
              'Guitarra é um instrumento de corda. Normalmente possui 6 cordas.',
              'If You é uma música eletrônica do grupo Magic Box. Essa música é nostálgica.',
              'A emissora Globo é uma fábrica de lixo que não serve para nada. É sério.',
              'Três pratos de trigo para três tigres felizes para cacete.', 'Basketball Motivation 2021: Good Vibes!',
              'Maratonistas de elite correm uma distância de 42km em uma média de 2h 10m.',
              'O único exercício físico que eu faço é correr atrás de dinheiro.',
              'O tempo muda tudo, menos a minha capacidade de ser trouxa.',
              'Não siga as minhas pegadas, eu também estou perdido.',
              'Michael Jordan enterra bolas de basquetebol da linha de arremesso.',
              'Kuroko Tetsuya é um moleque branquelo de cabelo azul claro que manda bem no basquete. Principalmente nos passes.',
              'Kagami Taiga é um rapaz alto e forte, de cabelo vermelho, que joga basquete no estilo "Michael Jordan"',
              'A seleção de basquete do Japão não é tão boa quanto o anime Kuroko no Basket faz parecer.2021.',
              'Todo mundo pensa que a capital da Austrália é Sidney, mas na verdade é Camberra.',
              'Máscara para se proteger de vírus? Isso não te protege de nada.',
              'Akatsuki é uma organização filantrópica com métodos pacíficos.',
              'Asta de Black Clover consegue ser mais gritalhão que Naruto, Timmy Turner e Ash Ketchun juntos.',
              'Uma gatinha muito da cheirosinha', 'Atualmente, a tua mente atua ou mente.',
              'A seleção do Brasil de futebol foi pentacampeã no ano de 2002.',
              'Um hacker de elite vale mais que mil soldados na linha de frente.',
              'A linguagem de programação C é a mãe de várias outras linguagens.',
              'O sistema operacional Kali Linux é baseado em Debian e foi feito para Hackers Éticos.',
              'Ubuntu, Fedora, OpenSUSE, Manjaro ou Linux Mint? Qual é o melhor?']

    vez = ['1ª','2ª','3ª','4ª','5ª','6ª','7ª','8ª','9ª','10ª','11ª','12ª','13ª','14ª','15ª','16ª','17ª','18ª','19ª','20ª']

    #vez = ['PRIMEIRA', 'SEGUNDA', 'TERCEIRA', 'QUARTA', 'QUINTA', 'SEXTA', 'SÉTIMA', 'OITAVA', 'NONA', 'DÉCIMA',
    #      'DÉCIMA PRIMEIRA', 'DÉCIMA SEGUNDA', 'DÉCIMA TERCEIRA', 'DÉCIMA QUARTA', 'DÉCIMA QUINTA', 'DÉCIMA SEXTA',
    #      'DÉCIMA SÉTIMA', 'DÉCIMA OITAVA', 'DÉCIMA NONA', 'VIGÉSIMA']

    tempos = []

    frases_uti = []  ## As frases utilizadas vão entrar nessa lista para o programa conseguir diferenciar qual frase já foi utilizada ou não
    ## Para evitar que durante um jogo a frase se repita.

    #----- VALIDAÇÃO DE ENTRADA DA QUANTIDADE DE FRASES QUE O USUÁRIO DESEJA ESCREVER, ABAIXO.vvvvvvvvvvvvvvvvvvvvvvvvvv
    valid_system = False
    while valid_system == False:
        numFrases = input('Digite a quantidade de frases para digitar. [MIN: 1 MAX: 30]: ')
        try:
            numFrases = int(numFrases)
            if numFrases <= 0 or numFrases > 30:
                print('\nDeve digitar no mínimo uma frase e no máximo 30.')
            else:
                valid_system = True
        except:
            print('\n\nPor favor, digite apenas números inteiros. [MIN: 1 MAX: 30].')
    #----- VALIDAÇÃO DE ENTRADA DA QUANTIDADE DE FRASES QUE O USUÁRIO DESEJA ESCREVER, ACIMA.^^^^^^^^^^^^^^^^^^^^^^^^^^^


    input(str('\nDigite sem errar as frases que vão aparecer.\nPronto para digitar? Pressione ENTER para iniciar: '))

    ciclos = 0
    total = 0
    while ciclos < numFrases:

        inicio = t.time()

        ## VALIDANDO ENTRADA DE DADOS------------------------------------------------
        valid_frase = False
        frase_escolhida = ran.choice(frases)

        if frase_escolhida in frases_uti:  ## Esse condicional fará com que a frase não apareça no caso de ela for repetida.--------------------
            continue
        else:

            while valid_frase == False:
                frase_escrita = input('\n' + frase_escolhida + '\n\n')

                if frase_escrita == frase_escolhida:
                    valid_frase = True
                    print('-' * 50)
                else:
                    print('Erro na digitação.')

            ##---------------------------------------------------------------------------

            fim = t.time()
            tempo = round(fim - inicio, 2)
            tempos.append(tempo)
            total += tempo  ## Variável que vai se somar a cada tempo calculado a um total que será mostrado no final.
            ciclos += 1

        frases_uti.append(frase_escolhida)  ## A cada ciclo a frase utilizada vai entrar nessa lista "frases_uti"
        ##-------------------------------------------------------------------------------------------------------------------------------------

    print('-' * 50)
    print('RESULTADO:\n')

    x = 0
    for i in tempos:
        print(vez[x] + ' FRASE: ' + str(i) + ' segundos')
        x += 1
    total = str(round(total, 2))
    print('\nTOTAL: ' + total + ' segundos')
    print('-' * 50)

#///////////////////////////////////////// VVV GRÁFICO VVV /////////////////////////////////////////////////////////////
    #abiss = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30] #<--- EIXO X [ABISCISSA]
    x = 0
    abiss = []
    for i in tempos:
        abiss.append(vez[x] + ' FRASE')
        x += 1

    orden = tempos                                                                               #<--- EIXO Y [ORDENADA]
    plt.plot(abiss,orden)
    plt.show()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    ## VALIDAÇÃO DE DADOS PARA (S OU N)
    valid_reset = False
    while valid_reset == False:
        escolha_reset = input('Deseja jogar novamente? (S ou N): ').lower()


        if escolha_reset == 's' or escolha_reset == 'n':
            valid_reset = True
        else:
            print('Digite apenas S ou N.')

    if escolha_reset == 's':
        print('\n' * 150)
    else:
        reset = True

print('\nObrigado por jogar!\nEm caso de erro no jogo ou qualquer dúvida, meu e-mail é: gregory.valadares@gmail.com.\nFIM DO JOGO...')