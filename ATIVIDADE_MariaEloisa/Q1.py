#1. Escreva um programa que leia o número de questões que um candidato acertou em uma prova que consistia de 50 questões. O programa deve calcular o percentual de acertos deste candidato.

acertos = int(input('Digite o número de acertos:'))
porcentagem = acertos/50 * 100
print(f'O percentual de acertos é de {porcentagem:.0f}%')