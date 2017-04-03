#
#
#
import PIL
import Image
import random


'''
 _ 1 _ 2 _
 3   4   5
 _ 6 _ 7 _
 8   9   10
 _11 _12 _

list of 12 bools describe whether squares are connected or not

'''

h=32
w=32

bridges=[
  (9,2,True),(19,2,True),
  (2,9,False),(12,9,False),(22,9,False),
  (9,12,True),(19,12,True),
  (2,19,False),(12,19,False),(22,19,False),
  (9,22,True),(19,22,True)
]

holes=[
(10,10),(20,10),
(10,20),(20,20)
]

hole_corr=[
[0,2,3,5],
[1,3,4,6],
[5,7,8,10],
[6,8,9,11]
]

im_array = [[255 for col in range(w)] for row in range(h)]

def RandomGlyphCode():
  output=[]
  for i in range(0,12):
    output.append(random.randrange(0,2))
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

def draw_glyph(code,array):
  # draw empty blocks
  for i in range(3):
    for j in range(3):
      array=draw_empty_block((2+10*i,2+10*j),array)
  #draw bridges
  for i in range(len(code)):
    if(code[i]):
      array=draw_bridge(bridges[i],array)
  #draw holes
  for n in range(len(hole_corr)):
    t=True
    for m in hole_corr[n]:
      if(not code[m]):
        t=False
    if(t):
      array=draw_hole(holes[n],array)
  return array

k=RandomGlyphCode()

print k
im_array=draw_glyph(k,im_array)




img = Image.new( 'RGB', (h,w), "white") # create a new white image
pixels = img.load() # create the pixel map


for y in range(h):
  for x in range(w):
    c=im_array[y][x]
    pixels[x, y] = (c,c,c)

img.save("test.png")
