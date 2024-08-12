import random
import tkinter as tk
from tkinter import messagebox


def play_game():
    playerin = player_choice.get().lower()

    try:
        playerdict = {
            'r': 2,
            's': 1,
            'p': 0,
        }
        player = playerdict[playerin]
        reversedict = {
            2: 'Rock',
            1: 'Scissor',
            0: 'Paper'
        }
        computer = random.choice([0, 1, 2])

        def choose():
            result.set(f'You chose {reversedict[player]}, Computer chose {reversedict[computer]}.')

        def condition(name, ending):
            if computer != player:
                if computer == 2 and player == 1:
                    messagebox.showinfo('Result', f'Rock broke Scissor\nYou lose. {ending} {name}')
                elif computer == 1 and player == 0:
                    messagebox.showinfo('Result', f'Scissor cut Paper\nYou lose. {ending} {name}')
                elif computer == 0 and player == 2:
                    messagebox.showinfo('Result', f'Paper covered Rock\nYou lose. {ending} {name}')
                elif computer == 0 and player == 1:
                    messagebox.showinfo('Result', f'Scissor cut Paper\nYou win! {ending} {name}')
                elif computer == 1 and player == 2:
                    messagebox.showinfo('Result', f'Rock broke Scissor\nYou win! {ending} {name}')
                elif computer == 2 and player == 0:
                    messagebox.showinfo('Result', f'Paper covered Rock\nYou win! {ending} {name}')
            else:
                messagebox.showinfo('Result', f'It\'s a draw! {ending} {name}')

        choose()
        condition(n.get(), 'Thank you for playing.')

    except KeyError:
        messagebox.showerror('Invalid Input!!', 'Invalid input! Please select Rock (r), Paper (p), or Scissor (s).')


# Setting up the main window
root = tk.Tk()
root.title('Rock, Paper, Scissors Game')
root.geometry('600x400')
root.configure(bg='#e1c9f8')

# Title Label
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=('Helvetica', 18, 'bold'), bg='#e1c9f8', fg='#000000')
title_label.pack(pady=20)

# Player's name input
name_frame = tk.Frame(root, bg='#e1c9f8')
name_frame.pack(pady=10)
tk.Label(name_frame, text="Enter your name:", font=('Helvetica', 12), bg='#e1c9f8', fg='#000000').pack(side='left')
n = tk.Entry(name_frame, font=('Helvetica', 12))
n.pack(side='left', padx=10)

# Choice instructions
instructions_label = tk.Label(root, text='Rock = "r" \nPaper = "p" \nScissor = "s"', font=('Helvetica', 10), bg='#e1c9f8',
                              fg='#000000')
instructions_label.pack(pady=5)

# Player's choice input
choice_frame = tk.Frame(root, bg='#e1c9f8')
choice_frame.pack(pady=10)
tk.Label(choice_frame, text="Choose one:", font=('Helvetica', 12), bg='#e1c9f8', fg='#000000').pack(side='left')
player_choice = tk.Entry(choice_frame, font=('Helvetica', 12))
player_choice.pack(side='left', padx=10)



# Display result
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=('Helvetica', 12), bg='#e1c9f8', fg='#000000')
result_label.pack(pady=20)

# Play button
play_button = tk.Button(root, text="Play", font=('Helvetica', 14), bg='#0B0D0A', fg='#ECF0F1', command=play_game)
play_button.pack(pady=40)

# Run the application
root.mainloop()
