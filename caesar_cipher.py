'''
  -- vigenere cipher --
  It is a method of encrypting alphabetic text based on letters.
  You can see more examples and explanation here:
  https://en.wikipedia.org/wiki/Vigenère_cipher

  In my example, I have a key called ROCKET
  and I need to decrypt a text (txt_encrypt) according with this key

  If I have "S" and the first letter in the key is "R"
  A = 1, B = 2, C = 3, D = 4 [...]
  it means that S = 19 and R = 18
  so it jumps down 1 letter
  19 - 18 = 1
  starting in A, A + 1 = B
  result: with S letter and R key, the real text (plaintext) is B

  Now example with the next letter and key,
  C instead of S, O instead of R
  it means that C = 3 and O = 15
  so it jumps down 14 letters
  starting in A, A + 14 = O
  resukt: with C letter and O key, the plaintext is O

  and so on.

'''

# hint: start in "if __name__ == '__main__':"

# second method called with two arguments
def letter_jumpdown(letter, position, j):
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  # variable responsable to trasform all the letter in upper letter
  # example: if there is "d" it will be "D" which is 68, so 68 - 65 = 3
  # 3 -> [0,1,2,3] -> [A,B,C,D]
  # using "S" as the first letter in txt_encrypt
  # ord('S') == 83
  # so 83 - 65 = 18
  # char_ascii = 18
  #
  # using "Q" as the second letter in txt_encrypt
  # char_ascii = ord('C') - 65
  # char_ascii = 67 - 65
  # char_ascii = 2
  char_ascii = ord(letter.upper()) - 65

  # it is necessary when the char_ascii is anything but it is not a letter,
  # so it could be for example "," "!" "?" "."
  # result: the character will not change, in other words, same ~letter~
  # using "S" as the first letter in txt_encrypt
  # 18 is not less than 0 either more than 25, so ignore it
  #
  # using "C" as the second letter in txt_encrypt
  # 2 is not less than 0 either more than 25, so ignore it
  if char_ascii < 0 or char_ascii > 25:
    return letter
  # if char_ascii is the same than a letter on the key, it will return "A"
  # using "S" as the first letter in txt_encrypt
  # S is different than R (position[j]), next
  #
  # using "C" as the second letter in txt_encrypt
  # C == position[j]
  # C == O
  # C is not equal O, so ignore it
  elif letter.upper() == position[j]:
    return "A"

  # if char_ascii is not the same than a letter on the key and it is not something random like "." "!" etc
  # so it will return for example
  # using "S" as the first letter in txt_encrypt...
  #
  # also using "C" as the second letter in the txt_encrypt...
  else:
    # result = ord('S') - ord('R') = 83 - 82 = 1
    #
    # result = ord('C') - ord('O')
    # result = 67 - 79
    # result = -12
    result = ord(letter.upper()) - ord(position[j])
    # it means that 1 is more than zero and less than 27
    #
    # it means that 2 is more than zero and less than 27
    if result > 0 and result < 27:
      # return chr(ord('A') + 1)
      # return chr(65 + 1)
      # return chr(66)
      # return B // this is the result!
      #
      # return chr(ord('A') + 2)
      # return chr(65 + 2)
      # return chr(67)
      # return B // this is the result!
      return chr(ord("A") + result)
    else:
      # using "C" as the second letter in the txt_encrypt
      for i in alphabet:
        # if i == C:
        #print('[-] i value: {0} - letter value: {1}'.format(i, letter))
        if i == letter.upper():
            # result2 = ord('C') - (-12)
            # result2 = 67 + 12
            # result2 = 79
            # result2 = O // this is the result!!
            result2 = chr(ord(letter.upper()) - result)
            # it is to change j, to be always a letter after another
            #i = i + 1

            # it is to the key doesn't stop, if it is over it will start again
            #if i >= len(alphabet):
             #i = 0

            return result2

# first method called without argument
def main():

  # txt_encrypt is the string that has cryptography, it means we dont understand it
  txt_encrypt = "SCQ CHL HYYGU OO"
  # txt_decrypt is the empty string which is necessary to save the original text without cryptography soon
  txt_decrypt = ""
  # key for decrypting the cipher
  key = "ROCKET"
  # declare it as a character
  letter_encrypt = chr

  # it goes through each letter of the cryptography text
  j = 0
  for letter_encrypt in txt_encrypt:
    # txt_decrypt calls letter_jumpdown method with two arguments
    letter = letter_jumpdown(letter_encrypt, key, j)
    txt_decrypt += letter
    # it is to change j, to be always a letter after another
    j = j + 1

    # it is to the key doesn't stop, if it is over it will start again
    if j >= len(key):
        j = 0

  # print plaintext
  print("The plaintext is: ", txt_decrypt)

# it is necessary for the interpreter to understand that the program must initially runs here
if __name__ == '__main__':
  main()
