#Tic_Tac_Toe_Game_With_python
#import necessary libraries

import tkinter as tk
from tkinter import messagebox
import winsound
import time

#------------------------------------
#Game Variables----------------------
#------------------------------------
current_player = 'X'
board = [""]*9
buttons = []

# Colors
BG_COLOR = "#B7C2E6"
BTN_COLOR = "#f2f7f2"
BTN_HOVER = "#505357"
COLOR_X = "#ff4d4d"
COLOR_O = "#101110"
WIN_COLOR = "#2ecc71"
RESET_COLOR = "#f1c40f"


#-------------------------------------
#sound effects -----------------------
#-------------------------------------

def sound_click ():
    winsound.Beep(700,80)  #frequency,duration

def sound_win ():
    winsound.Beep(900,200)
    winsound.Beep(600,200)

def sound_draw():
    winsound.Beep(400,200)

#--------------------------------------
#animation-----------------------------
#--------------------------------------
def animate_button(btn):
    "Button will flash on click (simple animation)"
    for _ in range(2):
        btn.config(bg="#fa0c0c")
        btn.update()
        time.sleep(0.05)
        btn.config(bg=BTN_COLOR)
        btn.update()
        time.sleep(0.05)

def pulse_winning_buttons(indices):
    "winning buttons briefly glow."
    for _ in range(4):
        for idx in indices:
            buttons[idx].config(bg=WIN_COLOR)
        root.update()
        time.sleep(0.15)

        for idx in indices:
            buttons[idx].config(bg=BTN_COLOR)
        root.update()
        time.sleep(0.15)

#---------------------------------------
# Game Logic ---------------------------
#---------------------------------------
def on_button_click(i):
    global current_player

    # --- Prevent clicking already-filled button ---
    if board[i] != "":
        return

    # --- Place X or O ---
    board[i] = current_player
    buttons[i].config(
        text=current_player,
        fg=COLOR_X if current_player == "X" else COLOR_O
    )

    sound_click()
    animate_button(buttons[i])

    # --- Check Winner ---
    winner_combo = check_winner(current_player)
    if winner_combo:
        pulse_winning_buttons(winner_combo)
        sound_win()
        messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        reset_board()     # FIXED
        return

    # --- Check Draw ---
    if "" not in board:
        sound_draw()
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_board()     # FIXED
        return

    # --- Switch Player ---
    current_player = "O" if current_player == "X" else "X"

def check_winner(player):
    combos =[
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in combos:
        if board[a]== board[b]== board[c]== player:
            return(a,b,c)
    return None

def reset_board():
    global board, current_player
    board=[""] *9
    current_player ='X'
    for btn in buttons:
        btn.config(text="",bg=BTN_COLOR)

#-------------------------------------
#GUI Window---------------------------
#-------------------------------------

root = tk.Tk()
root.title("TIC_TAC_TOE_GAME")
root.geometry("340x420")
root.config(bg=BG_COLOR)
root.resizable(False,False)

#-------------------------------------
#Create Buttons----------------------
#-------------------------------------

for i in range(9):
    btn = tk.Button(
        root,text="",font =("Aerial",26,"bold"),width = 4, height = 1, bg = BG_COLOR, fg="White",
        activebackground =BTN_HOVER, command =lambda i=i: on_button_click(i)
    )
    btn.grid(row=i//3, column=i % 3, padx=8, pady=8)
    buttons.append(btn)

# ------------------------------
# RESET BUTTON
# ------------------------------

reset_btn = tk.Button(
    root, text="Reset Game",font=("Aerial",14,"bold"),bg=RESET_COLOR,fg= "Black",width =12,command = reset_board
)
reset_btn.grid(row=3,column =0,columnspan =3,pady=20)

#### start app

root.mainloop()