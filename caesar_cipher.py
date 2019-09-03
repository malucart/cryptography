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
def letter_jumpdown(letter, position):
  # it is going to be the index of the key, because when the key is finished it has to start again
  j = 0

  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  # variable responsable to trasform all the letter in upper letter
  # example: if there is "d" it will be "D" which is 68, so 68 - 65 = 3
  # 3 -> [0,1,2,3] -> [A,B,C,D]
  char_ascii = ord(letter.upper()) - 65


  # it is necessary when the char_ascii is anything but it is not a letter,
  # so it could be for example "," "!" "?" "."
  # result: the character will not change, in other words, same ~letter~
  if char_ascii < 0 or char_ascii > 25:
    return letter
  # if char_ascii is the same than a letter on the key, it will return "A"
  elif char_ascii == position[j]:
    return "A"

  # if char_ascii is not the same than a letter on the key and it is not something random like "." "!" etc
  # so it will return for example
  # position[j] -> R -> 82, letter -> S -> 83
  # it means that (I - D) % 26 = F
  else:
    result = ord(letter) - ord(position[j])
    if result < 0 and result < 27:
      return (ord("A") + result)
    else:
      for i in range(len(alphabet), 0):
        if i == letter:
            i += result
            return i;

  # it is to change j, to be always a letter after another
  j = j + 1

  # it is to the key doesn't stop, if it is over it will start again
  if j >= len(position):
    j = 0

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
  print("The plaintext is: ", txt_decrypt)

# it is necessary for the interpreter to understand that the program must initially runs here
if __name__ == '__main__':
  main()
