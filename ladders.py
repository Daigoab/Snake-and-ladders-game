import tkinter as tk
from PIL import ImageTk,Image
import random
from gtts import gTTS
from playsound import playsound
import os

def Speak (Text):
    obj = gTTS(text = Text, lang = "en", slow = False)
    obj.save("Text.mp3")
    playsound("Text.mp3")
    os.remove("Text.mp3")

def start_game() :

    global im
    global b1, b2

    #Buttons for player
    #Player -1
    b1.place(x=900 ,y=400)

    #Player -2
    b2.place(x=900 ,y=500)

    #Dice button

    im = Image.open("dice.png")
    im = im.resize((65, 65))
    im = ImageTk.PhotoImage(im)
    b = tk.Button(root, 
                image= im, 
                height= 80, 
                width = 80, 
                )
    b.place(x=980 ,y=200)

    #Exit button

    b3 = tk.Button(root, 
                text="Click here to exit the game", 
                height= 3, 
                width = 20, 
                fg = "red", 
                bg = "cyan", 
                font = ("cursive", 14,"bold"), 
                activebackground = "grey",
                command = root.destroy )
    b3.place(x=900 ,y=20)

#Reset the coins to start position
def reset_coins ():
    global player_1, player_2
    global pos1, pos2

    player_1.place(x=45, y=585)
    player_2.place(x=45, y=585)

    pos1 = 0 
    pos2 = 0

#Load images to program
def load_dice_images ():
    global Dice
    names = ["dice1.png", "dice2.png", "dice3.png", "dice4.png", "dice5.png", "dice6.png"]
    for nam in names:
        im = Image.open(""+ nam)
        im = im.resize((65, 65))
        im = ImageTk.PhotoImage(im)
        Dice.append(im)

#Check for ladder
def check_ladder (Turn):
    global pos1, pos2

    f = 0 # No ladder
    if Turn == 1:
        if pos1 in Ladder:
            pos1 = Ladder[pos1] #Changing position to top for player 1
    else:
        if pos2 in Ladder:
            pos2 = Ladder[pos2] #For player 2
            f = 1
    return f

#Check for snake
def check_snake (Turn):
    global pos1, pos2

    if Turn == 1:
        if pos1 in Snakes:
            pos1 = Snakes[pos1] #Changing positon to tail for player 1
    else:
        if pos2 in Snakes:
            pos2 = Snakes[pos2] #For player 2

#Roll the dice
def roll_dice ():
    global Dice
    global turn
    global pos1, pos2
    global b1, b2

    r = random.randint(1,6)
    b3 = tk.Button(root, 
                image= Dice[r-1], 
                height= 80, 
                width = 80, 
                )
    b3.place(x=980 ,y=200)

    Speak(str(r))

    Lad = 0 #No ladder

    if turn == 1:
        if (pos1 + r) <= 100:
            pos1 = pos1 + r
        Lad = check_ladder(turn)
        check_snake(turn)
        move_coin(turn, pos1)
        if r != 6 and Lad != 1:
            turn = 2
            b1.configure(state= "disabled")
            b2.configure(state= "normal")
    else:
        if (pos2 + r) <= 100:
            pos2 = pos2 + r
        Lad = check_ladder(turn)
        check_snake(turn)
        move_coin(turn, pos2) 
        if r != 6 and Lad != 1:
            turn = 1
            b1.configure(state= "normal")
            b2.configure(state= "disabled")
    Speak("Player - " + str(turn) + "turn")
    is_winner()

#Determine who is the winner
def is_winner ():
    global pos1, pos2

    if pos1 == 100:
        msg = "Player 1 wins"
        Speak(msg)
        Lab = tk.Label(root, text=msg, height = 2, width = 20, font = ("cursive", 30, "bold"))
        Lab.place(x = 300, y = 300)
        reset_coins()
    elif pos2 == 100:        
        msg = "Player 2 wins"
        Speak(msg)
        Lab = tk.Label(root, text=msg, height = 2, width = 20, font = ("cursive", 30, "bold"))
        Lab.place(x = 300, y = 300)
        reset_coins()
#Move the coins upon rolling dice
def move_coin (Turn , r):
    global player_1, player_2
    global Index, pos1, pos2

    if Turn == 1:
        player_1.place(x= Index[r][0], y= Index[r][1])
        Speak("Player 1, you are at" + str(pos1))
    else:
        player_2.place(x= Index[r][0], y= Index[r][1])
        Speak("Player 2, you are at" + str(pos2))

#Get index 
def get_index ():
    global player_1, player_2
    Num = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 80, 79, 78, 77, 76 ,75, 74, 73, 72, 71, 61, 62, 63, 64, 65, 66, 67, 68, 68, 69, 70, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    row = 45
    i = 0
    for x in range (1, 11):
        col = 45
        for y in range (1, 11):
            Index[Num[i]] = (col, row)
            col = col +61
            i = i+1
        row = row +61
    print(Index)


#To store dice images
Dice = []

#To store x and y coordinates of given numbers
Index = {}

#Initial positions of players
pos1 = None
pos2 = None

#Ladder to move coin from bottom to top
Ladder = {4:14, 9:31, 21:42, 28:84, 51:67, 72:91, 80:99}

#Snakes to move coin from head to tail  
Snakes = {98:79, 95:75, 93:73, 87:36, 64:60, 62:19, 54:34, 38:1, 17:7}

root = tk.Tk()
root.geometry("1366x768")
root.title("Snake and Ladders Game")
F1 = tk . Frame(root, width = 1368, height = 800, relief = "raised")
F1.place(x=0, y=0)

#Set board
img1 = ImageTk.PhotoImage(Image.open("board1.png"))
Lab = tk.Label(F1, image=img1)
Lab.place(x=40, y=40)

#Player 1 button
b1 = tk.Button(root, 
    text="Player - 1", 
    height= 3, 
    width = 20, 
    fg = "red", 
    bg = "cyan", 
    font = ("cursive", 14,"bold"), 
    activebackground = "blue", 
    command = roll_dice )

#Player 2 button
b2 = tk.Button(root, 
    text="Player - 2", 
    height= 3, 
    width = 20, 
    fg = "red", 
    bg = "orange", 
    font = ("cursive", 14,"bold"), 
    activebackground = "red",
    command = roll_dice)

#Player 1 coin
player_1 = tk.Canvas(root, width = 40, height = 40)
player_1.create_oval(10, 10, 40, 40, fill = "blue")

#Player 2 coin
player_2 = tk.Canvas(root, width = 40, height = 40)
player_2.create_oval(10, 10, 40, 40, fill = "green")

#Who rolls first by default
turn = 1

reset_coins()

get_index()

load_dice_images()

Speak("Welcome to snake and ladders game .... Start with player one")

start_game()
root.mainloop()
