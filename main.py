import sys

def cypher():
  n = check(sys.argv)
  plain = input('plaintext: ')
  print()
  print('Ciphered text: \n')

  ciphered = caesar(plain, n)

  for start in range(0, len(ciphered), 50):
    line = ciphered[start:start+50]
    for x in range(0, len(line), 5):
      block = ciphered[line + x : line + x + 5]
      print(''.join(block), end=' ')
    print()


def caesar(plain, n):
  plain = plain.upper
  c = []
  for letter in plain:
    if not letter.isalpha():
      continue
    offset = 65
    pi = ord(letter) - offset
    ci = (pi + n) % 26
    c.append(chr(ci+offset))
  return c

def check(arg):
  if len(arg) != 2 or arg[1].isalpha():
    exit('Usage is as follows ==> python caesar.py k')
  return int(arg[1])