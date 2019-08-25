'''
	-- caesar cipher --
	In cryptography, a caesar cipher is a type of substitution cipher and each letter in the plaintext is jumped down 
	using the same number (key). 
	For example, with the key 1, I becomes H, F would becomes E, Z becames Y, and so on. 
	"The method is named after Julius Caesar, who apparently used it to communicate with his generals".

	The idea in this code is to find the plaintext (the original text without criptography). 

	hint: I found it and it is in spanish language

'''

# hint: start in "if __name__ == '__main__':"
# second method called with two arguments
def letter_jumpdown(letter, position):
    # variable responsable to trasform all the letter in upper letter
    # example: if there is "d" it will be "D" which is 68, so 68 - 65 = 3 
    # 3 -> [0,1,2,3] -> [A,B,C,D]
    char_ascii = ord(letter.upper()) - 65     
    
    # it is necessary when the char_ascii is anything but it is not a letter, 
    # so it could be for example "," "!" "?" "."   
    # result: same char_ascii, in other words, it will not change                                     
    if char_ascii < 0 or char_ascii > 25:   
        return letter

    # according the previous example, 3 % 26 = 3
    # then, new_letter is 3 + position (let's use 1, and the argument was -jumpdown, remember?
    # so it is -1)
    # = 3 - 1 = 2
    # 2 % 26 = 2
    # 2 + 65 = 67 -> "C"
    decimal_ascii = (char_ascii) % 26
    new_letter = chr(((decimal_ascii  + position) % 26) + 65)

    # returns "C"
    return new_letter

# first method called without argument 
def main():
	# txt_encrypt is the string that has cryptography, it meaans we dont understand it
    txt_encrypt = "Jz, jrsvj hlv pr ccvmf le irkf dzireufkv Kvexf hlv srzcri tfekzxf yfp (Up) Mz hlv kl dzirur pr vjkrsr ccrdreufdv Dléjkirdv vc trdzef hlv pf mfp (fy) Kl, kl vivj vc zdre p pf jfp vc dvkrc Dv mfp rtvitreuf p mfp ridreuf vc gcre Jfcf tfe gvejricf jv rtvcvir vc glcjf (fy pvry) Pr, pr dv vjkr xljkreuf drj uv cf efidrc Kfufj dzj jvekzufj mre gzuzveuf dáj Vjkf yrp hlv kfdricf jze ezexúe rglif Uvjgrtzkf Hlzvif ivjgziri kl tlvccf uvjgrtzkf Uvar hlv kv uzxr tfjrj rc fzuf Grir hlv kv rtlviuvj jz ef vjkrj tfedzxf Uvjgrtzkf Hlzvif uvjelurikv r svjfj uvjgrtzkf Wzidf ve crj grivuvj uv kl crsvizekf P yrtvi uv kl tlvigf kfuf le dreljtizkf Jlsv jlsv Jlsv, jlsv, jlsv Hlzvif mvi srzcri kl gvcf Hlzvif jvi kl izkdf Hlv cv vejvñvj r dz sftr Klj clxrivj wrmfizkfj (wrmfizkf, wrmfizkf srsp) Uvardv jfsivgrjri klj qferj uv gvczxif Yrjkr gifmftri klj xizkfj P hlv fcmzuvj kl rgvcczuf Jz kv gzuf le svjf mve urdvcf Pf jv hlv vjkrj gvejreufcf Ccvmf kzvdgf zekvekreufcf Drdz vjkf vj ureuf p ureufcf Jrsvj hlv kl tfirqfe tfedzxf kv yrtv sfd sfd! Jrsvj hlv vjr svsr vjkr sljtreuf uv dz sfd sfd! Mve gilvsr uv dz sftr grir mvi tfdf kv jrsv Hlzvif hlzvif mvi tlrekf rdfi r kz kv trsv Pf ef kvexf gizjr pf dv hlzvif uri vc mzrav Vdgvtvdfj cvekf, uvjglvj jrcmrav Grjzkf r grjzkf, jlrmv jlrmvtzkf Efj mrdfj gvxreuf, gfhlzkf r gfhlzkf Tlreuf kl dv svjrj tfe vjr uvjkivqr Mvf hlv vivj drcztzr tfe uvcztruvqr Grjzkf r grjzkf, jlrmv jlrmvtzkf Efj mrdfj gvxreuf, gfhlzkf r gfhlzkf P vj hlv vjr svccvqr vj le ifdgvtrsvqrj Gvif gr dfekricf rhlí kvexf cr gzvqr Uvjgrtzkf Hlzvif ivjgziri kl tlvccf uvjgrtzkf Uvar hlv kv uzxr tfjrj rc fzuf Grir hlv kv rtlviuvj jz ef vjkrj tfedzxf Uvjgrtzkf Hlzvif uvjelurikv r svjfj uvjgrtzkf Wzidf ve crj grivuvj uv kl crsvizekf P yrtvi uv kl tlvigf kfuf le dreljtizkf Jlsv, jlsv, jlsv, jlsv, jlsv Hlzvif mvi srzcri kl gvcf Hlzvif jvi kl izkdf Hlv cv vejvevj r dz sftr Klj clxrivj wrmfizkfj (wrmfizkf, wrmfizkf srsp) Uvardv jfsivgrjri klj qferj uv gvczxif Yrjkr gifmftri klj xizkfj P hlv fcmzuvj kl rgvcczuf Uvjgrtzkf Mrdfj r yrtvicf ve ler gcrpr ve Glvikf Iztf Yrjkr hlv crj fcrj xizkve Rp Sveuzkf Grir hlv dz jvccf jv hlvuv tfekzxf Grjzkf r grjzkf, jlrmv jlrmvtzkf Efj mrdfj gvxreuf, gfhlzkf r gfhlzkf Hlv cv vejvñvj r dz sftr Klj clxrivj wrmfizkfj (wrmfizkf, wrmfizkf srsp) Grjzkf r grjzkf, jlrmv jlrmvtzkf Efj mrdfj gvxreuf, gfhlzkf r gfhlzkf Yrjkr gifmftri klj xizkfj P hlv fcmzuvj kl rgvcczuf Uvjgrtzkf . Uvjgrtzkf jvizr ldr sfr jveyr grir kirsrcyfj wlklifj, erf rtyr?"
    
    # txt_decrypt is the empty string which is necessary to save the original text without cryptography soon
    txt_decrypt = ""

    # empty string which is necessary to save the jump down (key)
    message_jumpdown = ""
    # it starts in 0 and it goes until 25, because of the alphabet.
    # it goes through each letter of the alphabet 
    for jumpdown in range(0, 26):

    	# print which jump down is
        message_jumpdown = "\nJump down in {}\n".format(jumpdown)
        # it goes through each letter of the cryptography text
        for letter_encrypt in txt_encrypt:
        	# txt_decrypt calls letter_jumpdown method with two arguments
        	# in brief, the original text will be txt_decrypt + (letter encrypted - jumpdown)
        	# for the first case, the first letter encrypted is "J" because the first jumpdown is 0,
        	# so there is no any jump down, consequentely, txt_decrypt is the txt_encrypt
        	# for the second case, the first letter encrypted is "I" because the second jumpdown is 1,
        	# so there is 1 jump down, consequentely, txt_decrypt is all the letters - 1
            txt_decrypt += letter_jumpdown(letter_encrypt, -jumpdown) 

        # print the jump down (key), plaintext and it ask you if you can understand it 
        print(message_jumpdown)
        print(txt_decrypt)
        print("\nIs it decrypted? [1 - YES; 2 - NO]")
        # user types 1 or 2
        console = input()
        # if user types 1, the program is finished
        if console.upper() == '1'.upper():
            break

        # reset the old information here, so the print is more organized
        txt_decrypt = ''

# it is necessary for the interpreter to understand that the program must initially runs here
if __name__ == '__main__':
	main()
	
