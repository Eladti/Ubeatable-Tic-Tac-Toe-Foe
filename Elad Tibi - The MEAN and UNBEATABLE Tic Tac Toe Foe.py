# Copyright (c) [2024] [Elad Tibi, BSC. ECE BGU]

import tkinter as tk
import random

# ---------------------------------------------- Variables ----------------------------------------------

spots_taken = 0
cycles = 0
me_start = None
you_start = None
skirt_axis = None
start = False
finish = False
middle = False
done_corner_cycle = False
skirt_added = False
skirt_first = False
skirt_second = False
first_corner = False
buttons = []
computer_moves = []
player_moves = []
player = 'X'
mean_computer = 'O'
corners = [0, 0], [0, 2], [2, 0], [2, 2]
middle_outskirts = [0, 1], [1, 0], [1, 2], [2, 1]
winnings = [[[0, 0], [1, 1], [2, 2]], [[2, 0], [1, 1], [0, 2]]]

for i in range(3):
    temp_group1 = []
    temp_group2 = []
    for j in range(3):
        temp_group1.append([i, j])
        temp_group2.append([j, i])
    winnings.append(temp_group1)
    winnings.append(temp_group2)

# ---------------------------------------------- Mean Responses Bank ----------------------------------------------

win_bank = ["Defeated by a computer? \nI didn't know they let amateurs play.",
    "Beaten by a machine? Maybe stick\n to tic-tac-toe for beginners.",
    "Losing to code? That's embarrassing,\n even for you.",
    "Outsmarted by a program? \nYou must be operating on autopilot.",
    "Computer 1, Human 0. \nBetter luck next time, if there is one.",
    "Beaten by an algorithm? \nMaybe upgrade your hardware.",
    "Defeated by a computer? \nTime to rethink your worth.",
    "Losing to binary code? \nIt's like losing to a brick wall.",
    "Beaten by AI? Congratulations,\n you played yourself.",
    "Losing to a machine? \nThat's a new low, even for you.",
    "Defeated by a program? \nMaybe it's time to retire from gaming.",
    "Outwitted by code? Don't worry,\n there's always solitaire.", "We can go all day buddy." ]
tie_bank = ["Any time you are not winning,\n i basically won.", "Just remember, you could've been \n smart enough to win, but no.", "Tying with me? Guess that's \nyour peak performance.",
    "A draw? Is that the best \nyou can muster against a machine?",
    "Tie? I'll accept your surrender\n in the form of a draw.",
    "Just remember, you could've been\n smart enough to win, but no.",
    "Any time you are not winning,\n i basically won.",
    "Even a deadlock is a victory \nfor my superior intellect.",
    "Tie? That's like losing twice,\n once to me and again to dignity.",
    "Stuck in a draw? Clearly, \nintelligence is not your strong suit.",
    "You managed a tie? Should've \naimed for mediocrity instead.",
    "Draw? Must feel like a defeat\n with a computer as your equal.",
    "A tie? Don't worry, it's almost\n as good as losing outright.",
    "Tying with me? It's like tying\n with a particularly dull brick."]
save_bank = ["I may not be a super-computer, but a calculator could still block you.", "Blocked by a computer? It's like losing to a malfunctioning toaster.", "Even my calculator laughs at your feeble attempts to win.",
    "Blocked by a machine? Maybe stick to tic-tac-toe for toddlers.",
    "You got blocked by code? That's just sad, even for you.",
    "A computer outsmarted you? That's a new low, even for you.",
    "Blocked by a simple algorithm? You're truly scraping the bottom of the barrel.",
    "Blocked by a computer? Looks like your brain needs a reboot.",
    "You got outwitted by a program? Maybe try a less challenging game.",
    "Blocked by the AI? Your intelligence must be on vacation.",
    "A machine foiled your plans? Time to rethink your life choices.",
    "Blocked by binary code? Clearly, you're not operating at full capacity.",
    "Computer 1, Human 0. Better luck next century, Einstein.",
    "A computer blocked you? I'd offer sympathy, but it's too hilarious."]
regular_move_bank = ["I did not know they allowed apes to use python, refreshing.", "Did you mistake 'winning' for 'losing'? It seems like it.",
    "Making moves like that, I'm surprised you even found the keyboard.",
    "There's no way that was a serious move. Are you playing blindfolded?",
    "Choosing that move? Even a cat walking on the keyboard could do better.",
    "Did you let a toddler take over your game? It sure seems like it.",
    "Picking moves like that, you must be playing with your eyes closed.",
    "Making moves like that, I'm starting to wonder if you're even awake.",
    "There's silly, and then there's whatever that move was.",
    "Choosing that move? It's like you're playing a different game entirely.",
    "Did you forget how to play? Or are you just pretending for laughs?",
    "Good thing this game isn't public.",
    "Choosing that move? I hope you have a good explanation for it.",
    "Making moves like that, I'd hate to see your strategy for real life." ]
overwrite_try = ["Trying to overwrite the past ? I wasn't coded to feel sorry, but still am.", "Click it all you want, not going to work buddy.", "I'll wait for you to realize this is already checked, say if you need help.",
                 "Attempting to overwrite the past? I wasn't programmed to feel sorry, but here we are.",
                 "Click it all you want, but it's not going to work, buddy.",
                 "I'll wait patiently for you to realize this move has already been made. Need a hint?",
                 "Trying to rewrite history? Sorry, this isn't a choose-your-own-adventure game.",
                 "Feeling nostalgic? That move has already been played, and it wasn't a good one.",
                 "Attempting to undo the inevitable? It's like trying to unring a bell.",
                 "You can keep clicking, but that move is set in stone. Quite literally.",
                 "Still trying to erase the past? It's like trying to erase your own shadow.",
                 "You seem determined to rewrite the game's history. Good luck with that.",
                 "Trying to overwrite moves? I'll just sit here and watch your futile attempts.",
                 "Attempting to change the course of history? I suggest focusing on the present."
                 ]

# ---------------------------------------------- Configuration ----------------------------------------------


def forget_me_you():
    global you_start, me_start, start
    you_start.grid_forget()
    me_start.grid_forget()
    start = True


def me_game():
    global player, start, you_start, me_start, mean_computer
    display_message('No take-backs')
    player = 'O'
    mean_computer = 'X'
    random_corner()
    forget_me_you()


def you_game():
    global player, start, me_start, you_start, mean_computer
    display_message("I hope you clicked accidentally, it is embarrassing if not.")
    player = 'X'
    mean_computer = 'O'
    forget_me_you()


def build_game():
    global you_start, me_start, buttons, finish, start, spots_taken

    start = False
    spots_taken = 0

    if not finish:
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(root, text=" ", width=30, height=10,
                                   command=lambda row=i, col=j: on_button_click(row, col, player))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            buttons.append(row_buttons)

    if not start:
        you_start = tk.Button(root, text='Player First', command=lambda: you_game())
        me_start = tk.Button(root, text='Computer First', command=lambda: me_game())
        you_start.grid(row=0, column=0, columnspan=4)
        me_start.grid(row=2, column=0, columnspan=4)


def on_button_click(row, col, sign):
    global spots_taken, finish, start, computer_moves, player_moves, cycles, middle, skirt_first, skirt_second

    if not start:
        return

    button_status = buttons[row][col].cget('text')
    if button_status == ' ':

        buttons[row][col].configure(text=sign)
        player_moves.append([row, col])
        spots_taken += 1

        if finish_move():
            spots_taken = 9

        elif defense():
            if spots_taken == 9:
                random_pick = random.randint(0, 13)
                buttons[1][1].configure(text=tie_bank[random_pick])
                buttons[2][1].configure(text='Want to lose again ?')
                computer_moves = []
                player_moves = []
                middle = False
                skirt_first = False
                skirt_second = False
                finish = True
                cycles = 0
            return

        if mean_computer == 'X' and spots_taken != 9:
            computer_first_routine(row, col)

        if mean_computer == 'O' and spots_taken != 9:
            player_first_routine(row, col)

        if spots_taken == 9:
            random_pick = random.randint(0, 13)
            buttons[1][1].configure(text=win_bank[random_pick])
            buttons[2][1].configure(text='Want to lose again ?')
            computer_moves = []
            player_moves = []
            cycles = 0
            middle = False
            skirt_first = False
            skirt_second = False
            finish = True

        if not finish and start:
            random_pick = random.randint(0, 13)
            display_message(regular_move_bank[random_pick])

    elif row == 2 and col == 1 and spots_taken >= 9:
        for p in range(3):
            for t in range(3):
                buttons[p][t].configure(text=' ')
        build_game()
        finish = False

    elif spots_taken < 9 and start:
        random_pick = random.randint(0, 13)
        display_message(overwrite_try[random_pick])

# ---------------------------------------------- Routines ----------------------------------------------


def computer_first_routine(row, col):
    global spots_taken, middle, done_corner_cycle, cycles

    if spots_taken == 2:
        check_middle_click(row, col)
        if not middle:
            done_corner_cycle = False
            cycles = 0
            far_corner()
        return

    if spots_taken == 4:
        if middle:
            random_corner()
        else:
            if row == 1 and col == 1:
                random_pick = random.randint(0, 13)
                display_message(regular_move_bank[random_pick])
                random_corner()
            else:
                done_corner_cycle = False
                cycles = 0
                far_corner()
        return
    return


def player_first_routine(row, col):
    global spots_taken, middle, done_corner_cycle, cycles, player_moves, computer_moves, skirt_first, skirt_second, skirt_axis, skirt_added, first_corner
    if spots_taken == 1 and row == 1 and col == 1:
        middle = True
        random_corner()
        return
    elif spots_taken >= 3 and middle:
        cycles = 0
        random_corner()
        if not skirt_added:
            cycles = 0
            random_middle_outskirts()
        skirt_added = False
        return

    if spots_taken == 1 and check_skirts():
        buttons[1][1].configure(text=mean_computer)
        computer_moves.append([1, 1])
        spots_taken += 1
        random_pick = random.randint(0, 13)
        display_message(regular_move_bank[random_pick])
        skirt_first = True
        return
    elif spots_taken == 3 and check_opposite_skirts() and skirt_first:
        skirt_second = True
        random_corner()
        return
    elif spots_taken == 5 and skirt_second:
        for move in computer_moves:
            if move in corners:
                if skirt_axis == 0:
                    new_move = [abs(move[0]-2), move[1]]
                    buttons[new_move[0]][new_move[1]].configure(text=mean_computer)
                    computer_moves.append(new_move)
                    spots_taken += 1
                    display_message('Good luck buddy.')
                    return
                if skirt_axis == 1:
                    new_move = [move[0], abs(move[1] - 2)]
                    buttons[new_move[0]][new_move[1]].configure(text=mean_computer)
                    computer_moves.append(new_move)
                    spots_taken += 1
                    display_message('Good luck buddy.')
                    return

    if spots_taken == 1 and check_corner():
        first_corner = True
        buttons[1][1].configure(text=mean_computer)
        computer_moves.append([1, 1])
        spots_taken += 1
        random_pick = random.randint(0, 13)
        display_message(regular_move_bank[random_pick])
        return
    elif spots_taken >= 3 and first_corner:
        cycles = 0
        random_middle_outskirts()
        if not skirt_added:
            cycles = 0
            random_corner()
            if spots_taken == 8:
                spots_taken += 1
        skirt_added = False
        return

    if spots_taken >= 3:
        cycles = 0
        random_middle_outskirts()
        if not skirt_added:
            cycles = 0
            random_corner()
            if spots_taken == 8:
                spots_taken += 1
        skirt_added = False
        return

# ---------------------------------------------- Checks ----------------------------------------------


def check_exists(move):
    global computer_moves, player_moves
    if move in computer_moves or move in player_moves:
        return True
    else:
        return False


def check_close_enemies():
    global player_moves, computer_moves
    for p_move in player_moves:
        for c_move in computer_moves:
            if p_move[0] - c_move[0] <= 1 and p_move[0] - c_move[0] <= 1:
                return True


def check_opposite_skirts():
    global player_moves, skirt_axis
    axis1 = abs(player_moves[0][0] - player_moves[1][0])
    axis2 = abs(player_moves[0][1] - player_moves[1][1])
    if axis1 == 2 and axis2 == 0:
        skirt_axis = 0
        return True
    elif axis1 == 0 and axis2 == 2:
        skirt_axis = 1
        return True
    else:
        return False


def check_middle_click(row, col):
    global buttons, computer_moves, spots_taken, mean_computer, middle
    if row == 1 and col == 1:
        random_pick = random.randint(0, 13)
        display_message(regular_move_bank[random_pick])
        middle = True

        temp_opposite = None
        if computer_moves[0][0] != computer_moves[0][1]:
            temp_opposite = [computer_moves[0][1], computer_moves[0][0]]
        elif computer_moves[0][0] == 2:
            temp_opposite = [0, 0]
        elif computer_moves[0][0] == 0:
            temp_opposite = [2, 2]

        computer_moves.append(temp_opposite)
        buttons[temp_opposite[0]][temp_opposite[1]].configure(text=mean_computer)
        spots_taken += 1


def check_all_corners():
    global corners
    corner_counter = 0
    for corner in corners:
        if check_exists(corner):
            corner_counter += 1
    if corner_counter == 4:
        return True
    else:
        return False


def check_skirts():
    global middle_outskirts
    for skirt in middle_outskirts:
        if check_exists(skirt):
            return True
    return False


def check_corner():
    global corners
    for corner in corners:
        if check_exists(corner):
            return True
    return False

# ---------------------------------------------- Random Inserts ----------------------------------------------


def random_corner():
    global spots_taken, buttons, computer_moves, mean_computer, corners, cycles, skirt_added
    cycles += 1
    if cycles > 25:
        return

    random_corner_number = random.randint(0, 3)
    if not check_exists(corners[random_corner_number]):
        buttons[corners[random_corner_number][0]][corners[random_corner_number][1]].configure(text=mean_computer)
        computer_moves.append([corners[random_corner_number][0], corners[random_corner_number][1]])
        spots_taken += 1
        skirt_added = True
    else:
        random_corner()
    return


def random_middle_outskirts():
    global spots_taken, buttons, computer_moves, mean_computer, middle_outskirts, cycles, skirt_added
    cycles += 1
    if cycles > 25:
        return

    random_corner_number = random.randint(0, 3)
    if not check_exists(middle_outskirts[random_corner_number]):
        buttons[middle_outskirts[random_corner_number][0]][middle_outskirts[random_corner_number][1]].configure(text=mean_computer)
        computer_moves.append([middle_outskirts[random_corner_number][0], middle_outskirts[random_corner_number][1]])
        spots_taken += 1
        skirt_added = True
    else:
        random_middle_outskirts()
    return

# ---------------------------------------------- Auto-Responses ----------------------------------------------


def defense():
    global player_moves, spots_taken, winnings, computer_moves, buttons, mean_computer
    for slot in winnings:
        temp_counter = 0
        save_move = None
        for move in slot:
            if move in player_moves:
                temp_counter += 1
            else:
                save_move = move
        if temp_counter == 2 and not check_exists(save_move):
            spots_taken += 1
            buttons[save_move[0]][save_move[1]].configure(text=mean_computer)
            computer_moves.append(save_move)
            random_pick = random.randint(0, 13)
            display_message(save_bank[random_pick])
            return True


def finish_move():
    global player_moves, spots_taken, winnings, computer_moves, buttons, mean_computer
    for slot in winnings:
        temp_counter = 0
        save_move = None
        for move in slot:
            if move in computer_moves:
                temp_counter += 1
            else:
                save_move = move
        if temp_counter == 2 and save_move not in player_moves:
            buttons[save_move[0]][save_move[1]].configure(text=mean_computer)
            computer_moves.append(save_move)
            display_message('Can we stop now ?')
            return True

# ---------------------------------------------- Extra Functions ----------------------------------------------


def computer_start_corner():
    global spots_taken, buttons, computer_moves, mean_computer, middle, player_midout
    random_x_row = None
    random_x_col = None

    if spots_taken == 0:
        random_x_row = random.choice([0, 2])
        random_x_col = random.choice([0, 2])
        buttons[random_x_row][random_x_col].configure(text=mean_computer)
        computer_moves.append([random_x_row, random_x_col])
        spots_taken += 1
        return

    if middle:
        random_x_row = random.choice([0, 2])
        random_x_col = random.choice([0, 2])
        temp_box = [random_x_row, random_x_col]
        if temp_box not in computer_moves and temp_box not in player_moves:
            computer_moves.append(temp_box)
            buttons[random_x_row][random_x_col].configure(text=mean_computer)
            computer_moves.append([random_x_row, random_x_col])
            spots_taken += 1
        else:
            computer_start_corner()

    else:
        useless_move = []
        if spots_taken == 1 and player_midout:
            for p in range(2):
                if abs(player_moves[0][p] - computer_moves[0][p]) == 1:
                    for rest in range(3):
                        if player_moves[0][p] != rest and computer_moves[0][p] != rest:
                            useless_move.append(rest)
                else:
                    useless_move.append(player_moves[0][p])
            player_midout = False
        random_x_row = random.choice([0, 2])
        random_x_col = random.choice([0, 2])
        temp_box = [random_x_row, random_x_col]
        if temp_box not in computer_moves and temp_box not in player_moves and temp_box != useless_move:
            computer_moves.append(temp_box)
            buttons[random_x_row][random_x_col].configure(text=mean_computer)
            spots_taken += 1
        else:
            computer_start_corner()
    return


def far_corner():
    global spots_taken, buttons, computer_moves, mean_computer, done_corner_cycle, cycles
    cycles += 1
    if cycles > 25:
        return

    if not check_close_enemies():
        random_corner()
        return
    else:
        for threes in winnings:
            temp_counter = 0
            temp_save = None
            for move in threes:
                if move in computer_moves or move in player_moves:
                    temp_counter += 1
                else:
                    temp_save = move
            if temp_counter == 2:
                random_corner_number = random.choice([0, 1, 2, 3])
                if not check_exists(corners[random_corner_number]) and temp_save != corners[
                    random_corner_number] and not check_all_corners():
                    if done_corner_cycle:
                        return
                    buttons[corners[random_corner_number][0]][corners[random_corner_number][1]].configure(
                        text=mean_computer)
                    computer_moves.append([corners[random_corner_number][0], corners[random_corner_number][1]])
                    spots_taken += 1
                    done_corner_cycle = True
                else:
                    far_corner()
    return


def display_message(message):
    message_label.config(text=message)
    root.after(2500, clear_message)


def clear_message():
    message_label.config(text="")

# ---------------------------------------------- Main ----------------------------------------------


root = tk.Tk()
root.title("The Unbeatable (and Mean) Tic Tac Toe Foe")

message_label = tk.Label(root, text="", fg="black", font=('Courier', 10))
message_label.grid(row=3, column=0, columnspan=3)

build_game()

root.mainloop()
