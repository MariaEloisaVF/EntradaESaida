acertos = int(input('Digite o número de questões certas:'))
erros = int(input('Digite o número de questões erradas:'))
branco = int(input('Digite o número de questões em branco:'))

pontuacao1 = acertos * 3
pontuacao2 = erros  * 1
pontuacao3 = branco * 0

total = pontuacao1 + pontuacao2 + pontuacao3

print(f'A pontuação final é {total}')