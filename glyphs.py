# code to generate glyphs from a list of 12 bools
'''
for i in range(9000,10100):
  print i, unichr(i)
'''
#print unichr(2500)

#print int("2500",16)

'''
 _ 1 _ 2 _
 3   4   5
 _ 6 _ 7 _
 8   9   10
 _11 _12 _

list of 12 bools describe whether squares are connected or not

'''

import string
import random
import math
import os
rows, columns = os.popen('stty size', 'r').read().split()

def BoxChars():
  return [" ",unichr(9594),unichr(9592),unichr(9552),
    unichr(9595),unichr(9556),unichr(9559),unichr(9574),
    unichr(9593),unichr(9562),unichr(9565),unichr(9577),
    unichr(9553),unichr(9568),unichr(9571),unichr(9580)]


def PrintTop(a,b):
  line=unichr(9484)
  if a:
    line+=unichr(9573)
  else:
    line+=unichr(9472)
  if b:
    line+=unichr(9573)
  else:
    line+=unichr(9472)
  line+=unichr(9488)
  return line
 
def PrintBottom(a,b):
  line=unichr(9492)
  if a:
    line+=unichr(9576)
  else:
    line+=unichr(9472)
  if b:
    line+=unichr(9576)
  else:
    line+=unichr(9472)
  line+=unichr(9496)
  return line

# l = [up,down,left,right]

def MidChar(l):
  pos=""
  for b in l:
    pos+=str(b) 
  return BoxChars()[int(pos,2)]

def PrintMiddle(upa,upb,a,b,c,downa,downb):
  line=""
  if a:
    line+=unichr(9566)
  else:
    line+=unichr(9474)
  
  line+=MidChar([upa,downa,a,b])
  line+=MidChar([upb,downb,b,c])
  
  if c:
    line+=unichr(9569)
  else:
    line+=unichr(9474)
  return line


def PrintOdd(a,b):
  line=unichr(9474)
  if a:
    line+=unichr(9553)
  else:
    line+=" "
  if b:
    line+=unichr(9553)
  else:
    line+=" "
  line+=unichr(9474)
  return line

def PrintGlyph(l):
  a= PrintTop(l[0],l[1])
  b= PrintMiddle(l[0],l[1],l[2],l[3],l[4],l[5],l[6])
  c= PrintMiddle(l[5],l[6],l[7],l[8],l[9],l[10],l[11])
  d= PrintBottom(l[10],l[11])
  return a+'\n'+b+'\n'+c+'\n'+d

def RandomGlyphCode():
  output=[]
  for i in range(0,12):
    output.append(random.randrange(0,2))
  return output

def ListToString(l):
  output=""
  for i in l:
    output+=str(i)
  return output

def ConcatMultilineString(strings):
  lines=['']*len(strings[0].split('\n'))
  output=''
  for g in strings:
    g_lines=g.split('\n')
    for x in range(0,len(g_lines)):
      lines[x]+=g_lines[x]
  for line in lines:
    output+=line+'\n'
  return output[0:-1]

def PrintOneByOne():
  while True:
    raw_input("---")
    code = RandomGlyphCode()
    print ListToString(code)
    print PrintGlyph(code)

def PrintByLine(y):
  for m in range(0,y):
    glyphs=[]
    for x in range(0,(int(columns)/4)):
      code = RandomGlyphCode()
      glyphs.append(PrintGlyph(code))
    print ConcatMultilineString(glyphs)

#PrintOneByOne()
PrintByLine(int(raw_input('number of lines')))

#PrintGlyph([1,0,1,1,0,1,0,0,1,1,0,1])

#PrintMiddle(1,1,0,1,0,0,1)
