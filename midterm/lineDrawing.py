def coolFilter(pic, border, color):
  linepic = lineDrawing(pic)
  #framepic = frame(linepic)
  textpic = addTextCustom(linepic, "Cool Filter", 50, 100)
  finalpic = frame(textpic, border, color)
  return finalpic

def lineDrawing(pic):
  for x in range(0, getWidth(pic) - 1):
    for y in range(0, getHeight(pic) - 1):
      px1 = getPixel(pic, x, y)
      px2 = getPixel(pic, x+1, y)
      px3 = getPixel(pic, x, y+1)
      c1 = getRed(px1) + getGreen(px1) + getBlue(px1)
      c2 = getRed(px2) + getGreen(px2) + getBlue(px2)
      c3 = getRed(px3) + getGreen(px3) + getBlue(px3)
      if (abs(c1 - c2) > 10) and (abs(c1 - c3) > 10):
        setColor(px1, red)
      elif (abs(c1 - c2) > 5) and (abs(c1 - c3) > 5):
        setColor(px1, black)
      else:
        setColor(px1, cyan)
  return pic

def frame(pic, border, color):
   background = makeEmptyPicture(getWidth(pic) + border, getHeight(pic) + border, color) 
   finalpic = copyInto(pic, background, border/2, border/2)
   return finalpic

def betterBnW(pic):
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)*0.299
    g = getGreen(p)*0.587
    b = getBlue(p)*0.114
    color = (r+g+b)
    setRed(p,color)
    setBlue(p,color)
    setGreen(p,color)
  repaint(pic)
  
def addTextCustom(pic, text, x, y):
  mystyle = makeStyle(mono, italic + bold, 28)
  addTextWithStyle(pic, x, y, text, mystyle, blue)
  return pic
  
pic = makePicture(pickAFile())