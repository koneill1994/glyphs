
import math

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
  'nine'
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

def break_up_compound_word(word):
  output=[]
  for i in range(1,len(word)-1):
    p=[]
    t=True
    try:
      #print(word[:i])
      p.append(words.index(word[:i].lower()+'\n'))
      #print(word[i:])
      p.append(words.index(word[i:].lower()+'\n'))
    except ValueError:
      #print '    valueerror'
      t=False
    #print
    if(t): output.append(p)
  print(output)
  if(len(output)>0):
    # return the pair split nearest to the center
    return output[int(math.floor(len(output)/2.0))]
  else: return [word]


with open('scrambled_list.txt') as f:
    words = f.readlines()

# input text to have its common words translated into the scrambled_list.txt encoding

while True:
  print(break_up_compound_word(raw_input()))

while True:
  m=raw_input('').split()
  glyphs=[]
  p=[]
  for n in m:
    try:
      p.append(words.index(n.lower()+'\n'))
      glyphs.append(n)
    except ValueError:
      if(is_int(n)):
        for char in n:
          p.append(words.index(digits[int(char)]+'\n'))
          glyphs.append(digits[int(char)])
      else:
        for char in n:
          p.append(words.index(char.lower()+'\n'))
          glyphs.append(char)
  print glyphs
  print p
  
