import sys 


data = sys.argv[1]
text = sys.argv[2]
cif = sys.argv[3]

#Abrindo arquivo com dado cifrado
arquivo_decifrado = open(data, 'w')
arquivo_cifrado = open(text, 'r') 
texto_decifrado = ''
cifra = str(cif)

dataFull = arquivo_cifrado.read()
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
        texto_decifrado = texto_decifrado + " "
    else:
        if(ord(dataUpperCase[i]) - int(cifra[cif_i]) > 90):
            texto_decifrado = texto_decifrado + chr(ord(dataUpperCase[i]) + 26 - int(cifra[cif_i]))
        elif(ord(dataUpperCase[i]) - int(cifra[cif_i]) < 65):
            texto_decifrado = texto_decifrado + chr(ord(dataUpperCase[i]) + 26 - int(cifra[cif_i]))
        else:
            texto_decifrado = texto_decifrado + chr(ord(dataUpperCase[i]) - int(cifra[cif_i]))
    i = i + 1
    cif_i = cif_i + 1

print("Texto Cifrado: "+dataUpperCase)
print("Texto Decifrado: "+texto_decifrado)
arquivo_decifrado.write(texto_decifrado)

arquivo_decifrado.close()
arquivo_cifrado.close()
