# Wordle
# Dec 17
__author__ = "Ryan Xue"
import time, random, turtle #imports

# Global Variables
row = 1
word = ""
window = turtle.Screen() #turtle graphics
drawer = turtle.Turtle()

#user defined methods
#get all 5 letter words from list.txt and put them in words.txt
def convert():
  with open("list.txt", "r") as file, open("words.txt", "w") as newfile: #text files
    for line in file: #iteration
      if len(line) == 6: 
        newfile.write(line)

#choose random 5 letter word from words.txt
def getRandomWord():
  global word
  with open("words.txt", "r") as file:
    word = random.choice(file.read().split("\n")) #random and lists

#set up background, title, word grid, and turtles
def turtleSetup():
  window.tracer(0)
  window.bgcolor("black")
  drawer.width(5)
  drawer.speed(0)
  drawer.penup()
  drawer.hideturtle()
  drawer.color("white")
  drawer.sety(150)
  drawer.write('Wordle', font=('Courier', 30, 'normal'), align='center')
  setBoxes()
  window.update()

#used in turtleSetup() to draw the grid
def setBoxes():
  for y in range(-130, 140, 45):
    for x in range(-105, 105, 45):
      drawBox(x, y, drawer)

#draw a square with specified turtle and coordinates (used for coloring squares and drawing the grid)
def drawBox(x, y, t):
  t.penup()
  t.sety(y)
  t.setx(x)
  t.setheading(90)
  t.pendown()
  for i in range(4):
    t.forward(30)
    t.right(90)
  t.penup()

#checks if the word inputted only has letters and is 5 letters long
def vaildWord(sigma):
  try: #try/except block
    if sigma.isalpha() and len(sigma) == 5: #short circuited evaluation and string slices
      with open("words.txt", "r") as rizz:
        if sigma in rizz.read().split("\n"): #check if its a real word
          return True
        else:
          print(10/0)
    else:
      print(10/0)
  except:
    return False
    

#checks the letter inputted if it is in the same spot as the word, included in the word, or not in the word
def checkLetter(guess, index):
  global word
  if guess == word[index]: #selection structures
    return 2
  elif guess in word: # in
    return 1
  else:
    return 0

#game framework
def main():
  global row, word, drawer
  tw = turtle.Turtle()
  tw.penup()
  tw.hideturtle()
  tw.color("white")
  convert()
  getRandomWord()
  #reveals answer at beginning of the game (for debugging)
  #print(word)
  turtleSetup()
  while row<7:
    attempt = input('Attempt ' + str(row)).lower() #user input
    if vaildWord(attempt):
      #print("Valid")
      row += 1
      tw.sety(185-row*45+5)
      for i in range(5):
        tw.setx(-90+i*45)
        tw.write(attempt.upper()[i], font=('Courier', 25, 'normal'), align='center') #string built in methods: upper()
        accuracy = checkLetter(attempt[i], i)
        if accuracy == 0:
          drawer.color("white")
        elif accuracy == 1:
          drawer.color("yellow")
        elif accuracy == 2:
          drawer.color("light green")
        drawBox(-105+45*(i), 140-45*(row-1), drawer)
        window.update()
      if attempt == word:
        drawer.color('white')
        drawer.sety(-180)
        drawer.setx(0)
        if row == 2:
          drawer.write('You won in 1 guess!', font=('Courier', 20, 'normal'), align='center')
        else:
          drawer.write('You won in '+str(row-1)+' guesses!', font=('Courier', 20, 'normal'), align='center') #type conversion
        window.update()
        exit()
    else:
      print("Invalid input! Try again.") #machine output
  drawer.color('white')
  drawer.sety(-180)
  drawer.setx(0)
  drawer.write('The word was '+word, font=('Courier', 20, 'normal'), align='center')
  window.update()

#call main
if __name__ == '__main__':
  main()
