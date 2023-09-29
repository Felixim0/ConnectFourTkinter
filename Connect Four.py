import time
from tkinter import *

global totalRedCoOrds, totalBlueCoOrds, tempArray2, gameRunning, animation

root = Tk()
# Setup background assets
blankButtonImage = PhotoImage(file="./environment/blankButton.gif")
backgroundImage = PhotoImage(file="./environment/background.gif")
backgroundLabel = Label(root, image=backgroundImage)
backgroundLabel.grid(row=1, column=0, columnspan=12, rowspan=12)

# Setup Red and Blue button coordinate lists
totalRedCoOrds = []
totalBlueCoOrds = []

# Load Red and Blue button assets
redButtonImage = PhotoImage(file="./environment/redButton.gif")
blueButtonImage = PhotoImage(file="./environment/blueButton.gif")

# Setup global game variables
gameRunning = True
animation = False
currentColour = "Red"
nextAvailableSpaceNumber = 7

# Setup the array which will hold the board
boardArray = ["placeHolder"]
coloursArray = ["placeHolder"]

tempArray = []
tempArray2 = []

for i in range(1, 13):
  tempArray = []
  for j in range(1, 9):
    tempArray.append(0)
  boardArray.append(tempArray[:])
  coloursArray.append(tempArray[:])


def findNextAvailableSpace(column):
  global nextAvailableSpaceNumber
  #print(boardArray[column])
  for i in range(0, 8):
    if boardArray[column][i] == "*":
      nextAvailableSpaceNumber = int(i - 1)
      break

def colourChange():
  global currentColour
  currentColour = "Blue" if currentColour == "Red" else "Red"

def create_window(winner):
  top = Toplevel()
  top.title("You Win")
  if winner == "R":
    winner = "Red"
  elif winner == "B":
    winner = "Blue"
  message = str(str(winner) + " Winns!!!")
  msg = Label(top,
              text=message,
              bg=winner,
              font="Calibri 180",
              fg="white",
              pady=20)
  msg.grid(column=0, row=0)


def checkForWinner():
  global totalRedCoOrds, totalBlueCoOrds, coloursArray, gameRunning
  tempColoursArray = coloursArray[:]

  for x in range(1, len(tempColoursArray)):
    for j in range(0, len(tempColoursArray[x])):
      if (j + 3) < len(tempColoursArray[x]):
        if (tempColoursArray[x][j] !=
            0) and (tempColoursArray[x][j] == tempColoursArray[x][j + 1]) and (
                tempColoursArray[x][j] == tempColoursArray[x][j + 2]) and (
                    tempColoursArray[x][j] == tempColoursArray[x][j + 3]):
          print("found 4 in a row Vertical")
          gameRunning = False
          makeNewButtons("Disabled")
          create_window(tempColoursArray[x][j])

  for x in range(1, len(tempColoursArray)):
    for j in range(0, len(tempColoursArray[x])):
      if (x) < len(tempColoursArray) - 3:
        if (tempColoursArray[x][j] !=
            0) and (tempColoursArray[x][j] == tempColoursArray[x + 1][j]) and (
                tempColoursArray[x][j] == tempColoursArray[x + 2][j]) and (
                    tempColoursArray[x][j] == tempColoursArray[x + 3][j]):
          print("Found 4 in row Horizontal")
          gameRunning = False
          makeNewButtons("Disabled")
          create_window(tempColoursArray[x][j])

  for x in range(1, len(tempColoursArray)):
    for j in range(0, len(tempColoursArray[x])):
      if ((x) < len(tempColoursArray) - 3) and (
          (j) < len(tempColoursArray[x]) - 3):
        if (tempColoursArray[x][j] != 0) and (
            tempColoursArray[x][j] == tempColoursArray[x + 1][j + 1]) and (
                tempColoursArray[x][j] == tempColoursArray[x + 2][j + 2]) and (
                    tempColoursArray[x][j] == tempColoursArray[x + 3][j + 3]):
          print("Found 4 in row DiagonalRight")
          gameRunning = False
          makeNewButtons("Disabled")
          create_window(tempColoursArray[x][j])

  for x in range(1, len(tempColoursArray)):
    for j in range(0, len(tempColoursArray[x])):
      if ((x) < len(tempColoursArray) - 3) and (
          (j) < len(tempColoursArray[x]) - 3):
        if (tempColoursArray[x][j] != 0) and (
            tempColoursArray[x][j] == tempColoursArray[x - 1][j + 1]) and (
                tempColoursArray[x][j] == tempColoursArray[x - 2][j + 2]) and (
                    tempColoursArray[x][j] == tempColoursArray[x - 3][j + 3]):
          print("Found 4 in row DiagonalRight")
          gameRunning = False
          makeNewButtons("Disabled")
          create_window(tempColoursArray[x][j])


def moveButton(i, button):
  global nextAvailableSpaceNumber, currentColour, totalRedCoOrds, totalBlueCoOrds, tempArray2, coloursArray, gameRunning, animation
  if animation == False:
    animation = True
    column = i + 1
    nextAvailableSpaceNumber = 7
    findNextAvailableSpace(column)
    tempArray2 = []
    if (gameRunning == True):
      if (boardArray[column][0] != "*"):
        for z in range(0, nextAvailableSpaceNumber + 2):
          root.button[i].grid(column=i, row=z)
          time.sleep(0.04)
          root.update()
        root.button[i].grid(column=i, row=nextAvailableSpaceNumber + 1)
        root.update()

        boardArray[column][int(nextAvailableSpaceNumber)] = "*"

        if currentColour == "Red":
          coloursArray[column][int(nextAvailableSpaceNumber)] = "R"
        elif currentColour == "Blue":
          coloursArray[column][int(nextAvailableSpaceNumber)] = "B"

        tempArray2.append(column)
        tempArray2.append(int(nextAvailableSpaceNumber))

        if currentColour == "Red":
          totalRedCoOrds.append(tempArray2[:])
        elif currentColour == "Blue":
          totalBlueCoOrds.append(tempArray2[:])

        colourChange()
        if gameRunning == True:
          for x in range(0, 2):
            makeNewButtons("Enabled")
        animation = False
        checkForWinner()
    else:
      makeNewButtons("Disabled")


def makeNewButtons(abled):
  root.button = []
  for i in range(0, 12):
    if abled == "Enabled":
      if currentColour == "Red":
        root.button.append(
            Button(root,
                   image=redButtonImage,
                   command=lambda i=i: moveButton(i, "0"),
                   borderwidth=0,
                   state="normal"))
        root.button[i].grid(column=i, row=0)
      elif currentColour == "Blue":
        root.button.append(
            Button(root,
                   image=blueButtonImage,
                   command=lambda i=i: moveButton(i, "0"),
                   borderwidth=0,
                   state="normal"))
        root.button[i].grid(column=i, row=0)
    elif abled == "Disabled":
      if currentColour == "Red":
        root.button.append(
            Button(root,
                   image=redButtonImage,
                   command=lambda i=i: moveButton(i, "0"),
                   borderwidth=0,
                   state=DISABLED))
        root.button[i].grid(column=i, row=0)
      elif currentColour == "Blue":
        root.button.append(
            Button(root,
                   image=blueButtonImage,
                   command=lambda i=i: moveButton(i, "0"),
                   borderwidth=0,
                   state=DISABLED))
        root.button[i].grid(column=i, row=0)


def makeBoard():
  row = 1
  column = 0
  root.button2 = []
  for i in range(0, 96):
    root.button2.append(Button(root, image=blankButtonImage, borderwidth=0))
    root.button2[i].grid(column=column, row=row)
    column = column + 1
    if column == 12:
      column = 0
      row = row + 1


makeBoard()
for x in range(0, 2):
  makeNewButtons("Enabled")
root.title("Connect Four")
