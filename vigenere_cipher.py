'''
  -- vigenere cipher --
  It is a method of encrypting alphabetic text based on letters.
  You can see more examples and explanation here:
  https://en.wikipedia.org/wiki/Vigenère_cipher

  In my example, I have a key called ROCKET
  and I need to decrypt a text according with this key

  If I have "S" as the first letter on the text
  and "R" as the first letter on the key
  A = 0, B = 1, C = 2, D = 3 [...]
  it means that S = 18 and R = 17
  so it jumps down 1 letter
  18 - 17 = 1
  so starting in A,
  A + 1 =
  0 + 1 =
  = B
  result: with S letter and R key, the real text (plaintext) is B

  and so on.

'''

# hint: start in "if __name__ == '__main__':"

# second method called with three arguments
def letter_jumpdown(letter, position, j):
  print("----------------------")
  # necessary to compare array soon
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  # upper(): responsable to trasform all the letter in upper letter
  # but it already is upper letter or it is another thing but no a letter, keep the same character
  # example 1:
  # using 'S' as the first letter in txt_encrypt
  # char_ascii = ord('S') - 65
  # char_ascii = 83 - 65
  # char_ascii = 18
  #
  # example 2:
  # using 'C' as the second letter in txt_encrypt
  # char_ascii = ord('C') - 65
  # char_ascii = 67 - 65
  # char_ascii = 2
  #
  # example 3:
  # using 'Q' as the third letter in txt_encrypt
  # char_ascii = ord('Q') - 65
  # char_ascii = 81 - 65
  # char_ascii = 16
  char_ascii = ord(letter.upper()) - 65

  # it is necessary when the char_ascii is anything but it is not a letter,
  # so it could be for example "," "!" "?" "."
  # result: the character will not change
  # example 1:
  # using 'S' as the first letter in txt_encrypt
  # 18 is not less than 0 either more than 25, so ignore it
  #
  # example 2:
  # using 'C' as the second letter in txt_encrypt
  # 2 is not less than 0 either more than 25, so ignore it
  #
  # example 3:
  # using 'Q' as the third letter in txt_encrypt
  # 16 is not less than 0 either more than 25, so ignore it
  if char_ascii < 0 or char_ascii > 25:
    return letter

  # if char_ascii is the same than a letter on the key, it will return "A"
  # example 1:
  # using 'S' as the first letter in txt_encrypt
  # 'S' is different than 'R' (position[0]), so ignore it again
  #
  # example 2:
  # using 'C' as the second letter in txt_encrypt
  # 'C' is different than 'O' (position[1]), so ignore it again
  #
  # example 3:
  # using 'Q' as the third letter in txt_encrypt
  # 'Q' is different than 'C' (position[2]), so ignore it again
  elif letter.upper() == position[j]:
    return "A"

  # if char_ascii is not the same than a letter on the key and it is not something random like "." "!" etc
  # it has to enter here
  else:

    # example 1:
    # using 'S' as the first letter in txt_encrypt
    # result = ord('S') - ord('R')
    # result = (83 - 82) % 26 =
    # result = 1
    #
    # example 2:
    # using 'C' as the second letter in txt_encrypt
    # result = ord('C') - ord('O')
    # result = (67 - 79) % 26
    # result = 14
    #
    # example 3:
    # using 'Q' as the third letter in txt_encrypt
    # result = ord('Q') - ord('C')
    # result = (81 - 67) % 26
    # result = 14
    result = (ord(letter.upper()) - ord(position[j]))%26
    print('[-] result: {0}'.format(result))
    # it means that the number has to be more than zero and less than 27
    # because I'm using the alphabet size (which is 26)
    # example 1:
    # result = 1, so it stays here
    #
    # example 2:
    # result = 14, so it stays here
    #
    # example 3:
    # result = 14, so it stays here
    if result > 0 and result < 27:

      # example 1:
      # chr(ord('A') + result)
      # chr(65 + 1)
      # chr(66)
      # B
      # returns B
      #
      # example 2:
      # chr(ord('A') + result)
      # chr(65 + 14)
      # chr(79)
      # 0
      # returns 0
      #
      # example 3:
      # chr(ord('A') + result)
      # chr(65 + 14)
      # chr(79)
      # 0
      # returns 0
      final_result_1 = chr(ord('A') + result)
      print('[-] final result: {0}'.format(final_result_1))
      return final_result_1
    else:
      print('[-] sorry, something is wrong')

# first method called without argument
def main():

  # txt_encrypt is the string that has cryptography, it means we dont understand the text
  txt_encrypt = "SCQ CHL HYYGU OO"
  # txt_decrypt is the empty string which is necessary to save the original text without cryptography soon
  txt_decrypt = ""
  # key for decrypting the cipher
  key = "ROCKET"

  # it goes through each letter of the cryptography text
  # j is to change the letter on the key
  j = 0
  for letter_encrypt in txt_encrypt:
    # txt_decrypt calls letter_jumpdown method with three arguments
    letter = letter_jumpdown(letter_encrypt, key, j)
    txt_decrypt += letter
    # it is to change j, to be always a letter after another
    j = j + 1
    # it means that if j is over it will start again
    if j >= len(key):
        j = 0

  # print plaintext (the real text that we can understand)
  print("The plaintext is: ", txt_decrypt)

# it is necessary for the interpreter to understand that the program must initially runs here
if __name__ == '__main__':
  main()
