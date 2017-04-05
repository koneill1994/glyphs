
# list to allow numbers to be translated into their constituent english digits
digits=[
  'zero',
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine',
  'ten'
]

# all 26 english letters are in the list
# so if a word is not itself part of the list
# make it up from its constituent chars

def is_int(k):
  try:
    int(k)
    return True
  except ValueError:
    return False


with open('scrambled_list.txt') as f:
    words = f.readlines()

# input text to have its common words translated into the scrambled_list.txt encoding

while True:
  m=raw_input('').split()
  p=''
  for n in m:
    try:
      p+=str(words.index(n.lower()+'\n'))
    except ValueError:
      if(is_int(n)):
        for char in n:
          p+=str(words.index(digits[int(char)]+'\n'))  +' '
      else:
        for char in n:
          p+=str(words.index(char.lower()+'\n'))+' '
    if(p[-1]!=' '): p+=' '
  print p
