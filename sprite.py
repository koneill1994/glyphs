#
#
#
import PIL
import Image
import random
from copy import deepcopy


'''
 _ 1 _ 2 _
 3   4   5
 _ 6 _ 7 _
 8   9   10
 _11 _12 _

list of 12 bools describe whether squares are connected or not

'''

# size of the icon
# keep this at 32 unless you want to rewrite a bunch of code
icon=32

# number down and across of glyphs to make
h=32
w=32

# locations to place bridges
bridges=[
  (9,2,True),(19,2,True),
  (2,9,False),(12,9,False),(22,9,False),
  (9,12,True),(19,12,True),
  (2,19,False),(12,19,False),(22,19,False),
  (9,22,True),(19,22,True)
]

# locations to place holes
holes=[
(10,10),(20,10),
(10,20),(20,20)
]

# bridges to check and see if a hole is necessary
hole_corr=[
[0,2,3,5],
[1,3,4,6],
[5,7,8,10],
[6,8,9,11]
]

im_array = [[255 for col in range(icon*w)] for row in range(icon*h)]

def RandomGlyphCode():
  output=[]
  for i in range(0,12):
    output.append(random.randrange(0,2))
  return output

def GlyphFromNumber(n):
  output=[0]*12
  b=bin(n)[2:]
  c=[0]*(12-len(b))+list(b)
  for e in range(len(c)):
    output[12-e]=c[e]
  return output

def draw_empty_block((x,y),array):
  s=8
  color=0
  for n in range(0,s):
    #draw top & bottom rows
    if(n==0 or n==s-1):
      for m in range(1,s-1):
        array[n+y][m+x]=color
    else:
    #draw middle rows
      for m in range(0,s):
        array[n+y][m+x]=color
  return array

# bool vert tells if bridge is vertical or horizontal
def draw_bridge((x,y,vert),array):
  s=8
  color=0
  if(vert):
    for n in range(0,s):
      #draw top & bottom rows
      if(n==0 or n==s-1):
        for m in range(0,4):
          array[n+y][m+x]=color
      else:
        #draw middle rows
        array[n+y][x+1]=color
        array[n+y][x+2]=color
  else:
    # horizontal bridge
    for n in range(0,4):
      #draw top & bottom rows
      if(n==0 or n==3):
        array[n+y][x]=color
        array[n+y][x+s-1]=color
      else:
        for m in range(0,s):
          #draw middle row
          array[n+y][x+m]=color
  return array

def draw_hole((x,y),array):
  s=2
  color=0
  array[y][x]=color
  array[y+1][x]=color
  array[y][x+1]=color
  array[y+1][x+1]=color
  return array

def test_drawing(im_array):
  #[2,2+8+2,2+8+2+8+2]
  # draw empty blocks
  for i in range(3):
    for j in range(3):
      im_array=draw_empty_block((2+10*i,2+10*j),im_array)
  #draw bridges
  for p in bridges:
    im_array=draw_bridge(p,im_array)
  #draw holes
  for l in holes:
    im_array=draw_hole(l,im_array)
  return im_array

def add_tuple((a,b),f):
  return (f[0]+a,f[1]+b)

def draw_glyph((a,b),code,array):
  # draw empty blocks
  for i in range(3):
    for j in range(3):
      array=draw_empty_block((2+10*i+a,2+10*j+b),array)
  #draw bridges
  for i in range(len(code)):
    if(code[i]):
      array=draw_bridge((bridges[i][0]+a,bridges[i][1]+b,bridges[i][2]),array)
  #draw holes
  for n in range(len(hole_corr)):
    t=True
    for m in hole_corr[n]:
      if(not code[m]):
        t=False
    if(t):
      array=draw_hole(add_tuple((a,b),holes[n]),array)
  return array

def draw_shadows(array):
  output=deepcopy(array)
  for y in range(len(array)):
    for x in range(len(array[y])):
      if(array[y][x]==0):
        if(array[y-1][x-1]==255 or array[y-2][x-2]==255):
          output[y][x]=0
        else:
          output[y][x]=195
  return output

for m in range(h):
  for n in range(w):
    k=RandomGlyphCode()
    #k=GlyphFromNumber(m*w+n)
    #print k
    im_array=draw_glyph((n*icon,m*icon),k,im_array)

im_array=draw_shadows(im_array)

img = Image.new( 'RGB', (icon*h,icon*w), "white") # create a new white image
pixels = img.load() # create the pixel map


for y in range(icon*h):
  for x in range(icon*w):
    c=im_array[y][x]
    pixels[x, y] = (c,c,c)

img.save("test.png")
