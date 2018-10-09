def letra_deslocada(letra, posicao):
    valor_ascii = ord(letra.upper()) - 65     #letra maiúscula começa com 65, logo -65 seria para tudo
                                              #acontecer só entre as letras maiusculas (só ver a tabela)
    if valor_ascii < 0 or valor_ascii > 25:   #maior que 25 é depois de Z que é "["
        return letra

    referencia_numerica = (valor_ascii) % 26
    nova_letra = chr(((referencia_numerica + posicao) % 26) + 65)

    return nova_letra


if __name__ == '__main__':

    txt_cifrado = open("txt_cifrada", 'r')
    txt_decifrado = open("txt_decifrada", 'w')

    txt_cifrado = txt_cifrado.read()
    txt_decifrado = ''
    msg_deslocamento = ''
    for deslocamento in range(26):

        msg_deslocamento = "Deslocamento em {}\n".format(deslocamento)
        for letra_cifrada in txt_cifrado:
            txt_decifrado += letra_deslocada(letra_cifrada, -deslocamento)

        print(msg_deslocamento)
        print(txt_decifrado)
        print("Conseguiu descriptografar?! (1 p/ sim ; 2 p/ nao)")
        fim = input()
        if fim.upper() == '1'.upper():
            break

        txt_decifrado = ''

    txt_decifrado.write(msg_deslocamento + txt_decifrado)

    txt_cifrado.close()
txt_decifrado.close()
