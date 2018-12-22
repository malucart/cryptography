#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Como funciona a Cifra de Troca de Data (fonte:
#http://pt.wikihow.com/Criar-Cifras-e-C%C3%B3digos-Secretos)

#o Passo 1: Escolha uma data. Escolha uma data. Um
#exemplo pode ser o aniversário de Steven Spielberg:
#18 de Dezembro de 1946. Escreva esta data usando
#números e barras (18/12/46) e depois remova as
#barras, deixando você com um número de seis dígitos
#que você usará para cifrar sua mensagem: 121846.

#o Passo 2: Atribua os números a letras. Presumindo
#que a mensagem seja "Eu gosto dos filmes de Steven
#Spielberg". Abaixo da mensagem, você escreverá o
#número de seis dígitos repetidamente até chegar ao
#fim: 18 12461 812 461218 12 461812 461812461.

import sys 


data = sys.argv[1]
text = sys.argv[2]
cif = sys.argv[3]

#Abrindo arquivo com dado cifrado
arquivo_decifrado = open(data, 'r')
arquivo_cifrado = open(text, 'w') 
texto_cifrado = ''
cifra = str(cif)

dataFull = arquivo_decifrado.read()
dataUpperCase = dataFull.upper()

i = 0
cif_i = 0

while i < len(dataUpperCase):
    # ASCII
    # A = 65
    # Z = 90
    if(cif_i == 6):
        cif_i = 0
    if(ord(dataUpperCase[i]) == 32):
        texto_cifrado = texto_cifrado + " "
    else:
        if(ord(dataUpperCase[i]) + int(cifra[cif_i]) > 90):
            texto_cifrado = texto_cifrado + chr(ord(dataUpperCase[i]) - 26 + int(cifra[cif_i]))
        elif(ord(dataUpperCase[i]) + int(cifra[cif_i]) < 65):
            texto_cifrado = texto_cifrado + chr(ord(dataUpperCase[i]) + 26 + int(cifra[cif_i]))
        else:
            texto_cifrado = texto_cifrado + chr(ord(dataUpperCase[i]) + int(cifra[cif_i]))
    i = i + 1
    cif_i = cif_i + 1

print("Texto Decifrado: "+dataUpperCase)
print("Texto Cifrado: "+texto_cifrado)
arquivo_cifrado.write(texto_cifrado)
