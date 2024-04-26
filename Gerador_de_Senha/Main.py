import random
import os

letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
numeros = '1234567890'
caracteres_especiais = '!@#$%¨&*?.,:}[]{'

def gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_caracteres, incluir_numeros):
    
    caracteres_escolhidos = ''
    if incluir_maiusculas:
        caracteres_escolhidos += letras_maiusculass
    if incluir_minusculas:
        caracteres_escolhidos += letras_minusculas
    if incluir_caracteres:
        caracteres_escolhidos += caracteres_especiais
    if incluir_numeros:
        caracteres_escolhidos += numeros
    if not caracteres_escolhidos:
        return 'Nenhum Caractere escolhido'
    
    senha = ''.join(random.choices(caracteres_escolhidos,  k = comprimento))
    return senha

print('Bem vindo!')

print('Qual comprimento da senha desejada?')
comprimento = int(input(''))
os.system('cls')

print('Incluir letras maiúsculas na senha? (sim ou não)')
incluir_maiusculas = input('').lower() == 'sim'
os.system('cls')

print('Incluir letras minúsculas? (sim ou não)')
incluir_minusculas = input('').lower() == 'sim'
os.system('cls')

print('Incluir caracteres especiais? (sim ou não)')
incluir_caracteres = input('').lower() == 'sim'
os.system('cls')

print('Incluir numeros? (sim ou não)')
incluir_numeros = input('').lower() == 'sim'

senha_gerada = gerar_senha(comprimento, incluir_maiusculas, incluir_minusculas, incluir_caracteres, incluir_numeros)
print(f'A senha gerada é {senha_gerada}')