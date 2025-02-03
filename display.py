import game_logic
import tkinter as tk
import imageUtils
import random
import time

#init window
root = tk.Tk()
root.title("Rock paper scissors!!")
root.geometry("600x600")

#init images
#(these need to always have active pointers to them or else they will be garbage collected and stop appearing)
global idle_image 
idle_image = imageUtils.get_idle()
global active_image
active_image = imageUtils.get_active_image()
global rock_image
rock_image = imageUtils.get_rock()
global paper_image
paper_image = imageUtils.get_paper()
global scissors_image
scissors_image = imageUtils.get_scissors()

main_picture = tk.Label(root, image = idle_image)
main_picture.place(x = 300, y = 150, anchor = "center")

#init status message
message = tk.Label(root, text = "Let's play rock paper scissors!", font=("Arial", 24))
message.place(x = 300, y = 350, anchor = "center")

#init global time variable
global start_time

global playing_flag
playing_flag = False
#reset function
def reset():
    #make sure theyre not in a game, AND make sure it has been long enough since game start
    if (playing_flag == True) or (time.time() - start_time < 5):
        #if conditions arent met, schedule another call for when they are
        root.after((time.time() - start_time) * 1000 + 5)
    #actual reset logic if conditions are met
    else:    
        message.config(text = "Let's play rock paper scissors!")
        main_picture.config(image = idle_image)
    

#play the game
def status_update(user_input):
    #reset flags
    global start_time
    start_time = time.time()
    global playing_flag
    playing_flag == True

    #set image to active image and start animation
    main_picture.config(image = active_image)
    message.config(text = "I pick...")
    shake_animation(user_input = user_input, count = 10)

#shake animation
def shake_animation(user_input, count = 8):
    if count > 0:
        #random offset
        x_offset = random.choice([-1, 1]) * random.randint(7, 10)
        y_offset = random.choice([-1, 1]) * random.randint(7, 10)
        main_picture.place(x=300 + x_offset, y=150 + y_offset, anchor="center")
        #recursive call with one fewer shakes queued
        root.after(100, shake_animation, user_input, count - 1) 
    else:
        #continue gameplay
        root.after(1, continue_status_update, user_input)

#continuing the game
def continue_status_update(user_input):
    #picking cpu play and getting result
    result, pick = game_logic.fight(user_input)
    #changing message
    message.config(text = pick.capitalize() + f"! You {result}!")

    #replacing picture with CPU choice
    main_picture.place(x = 300, y = 150, anchor = "center")
    if pick == "scissors":
        main_picture.config(image = scissors_image)
    if pick == "rock":
        main_picture.config(image = rock_image)
    if pick == "paper":
        main_picture.config(image = paper_image)

    #changing playing flag, queueing a reset for 5 seconds
    global playing_flag
    playing_flag = False
    root.after(5000, reset)

#defining button functions
rock_butt = tk.Button(root, text = "Rock", command = lambda: status_update("rock"))
paper_butt = tk.Button(root, text = "Paper", command = lambda: status_update("paper"))
scissors_butt = tk.Button(root, text = "Scissors", command = lambda: status_update("scissors"))

#placing buttons
rock_butt.place(x = 150, y = 450, anchor = "center")
paper_butt.place(x = 300, y = 450, anchor = "center")
scissors_butt.place(x = 450, y = 450, anchor = "center")

#run!
root.mainloop()





