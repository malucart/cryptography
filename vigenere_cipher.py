'''
  -- vigenere cipher --
  It is a method of encrypting alphabetic text based on letters.
  You can see more examples and explanation here:
  https://en.wikipedia.org/wiki/Vigenère_cipher

  In my example, I have a key called ROCKET
  and I need to decrypt a text (txt_encrypt) according with this key

  If I have "S" and the first letter in the key is "R"
  A = 1, B = 2, C = 3, D = 4 [...]
  so S = 19
  Now I need to jump down 1 letter (because R = 18)
  (19 - 18) % 26 = 1
  it means that A = 1
  (because I gonna get I H G F)

  and so on.

'''
# coding=utf-8

# hint: start in "if __name__ == '__main__':"
# second method called with two arguments
def letter_jumpdown(letter, position):
  # it is going to be the index of the key, because when the key is finished it has to start again
  j = 0

  x = chr

  # variable responsable to trasform all the letter in upper letter
  # example: if there is "d" it will be "D" which is 68, so 68 - 65 = 3
  # 3 -> [0,1,2,3] -> [A,B,C,D]
  char_ascii = ord(letter.upper()) - 65

  # it is necessary when the char_ascii is anything but it is not a letter,
  # so it could be for example "," "!" "?" "."
  # result: same char_ascii, in other words, it will not change
  if char_ascii < 0 or char_ascii > 25:
      return letter
  # if char_ascii is the same than a letter on the key, it will return "A"
  elif char_ascii == position[j]:
      return "A"

  # if char_ascii is not the same than a letter on the key and it is not something random like "." "!" etc
  # so it will return for example
  # position[j] == D == 68, letter == I == 73
  # it means that (I - D) % 26 = F
  else:
    for i in range(0, 26):
       if i == position[j]:
          x = chr((letter.upper() - i) % 26)
          return x

  # it is to change j, to be always a letter after another
  j = j + 1

  # it is to the key doesn't stop, if it is over it will start again
  if j >= len(position):
    j = 0

  return ("hey, didnt find")

# first method called without argument
def main():

  # txt_encrypt is the string that has cryptography, it means we dont understand it
  txt_encrypt = "SCQ ISN WCWXH FV"
  # txt_decrypt is the empty string which is necessary to save the original text without cryptography soon
  txt_decrypt = ""
  # key for decrypting the cipher
  key = "ROCKET"
  # declare it as a character
  letter_encrypt = chr

  # it goes through each letter of the cryptography text
  for letter_encrypt in txt_encrypt:
    # txt_decrypt calls letter_jumpdown method with two arguments
    txt_decrypt += letter_jumpdown(letter_encrypt, key)

  # print plaintext
  print(txt_decrypt)

# it is necessary for the interpreter to understand that the program must initially runs here
if __name__ == '__main__':
  main()
