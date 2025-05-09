import tkinter as tk
import random
from PIL import Image, ImageTk

# Function to get computer choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle button click
def play(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    
    user_label.config(text=f"You chose: {choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    
    # Update images based on choices
    user_image.config(image=user_images[choice])
    computer_image.config(image=computer_images[computer_choice])

# Setting up the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Creating labels for displaying choices and results
user_label = tk.Label(root, text="", font=("Helvetica", 16))
user_label.pack(pady=10)

computer_label = tk.Label(root, text="", font=("Helvetica", 16))
computer_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

# Load user images
user_images = {
    'rock': ImageTk.PhotoImage(Image.open("user_rock.png").resize((150, 150))),
    'paper': ImageTk.PhotoImage(Image.open("user_paper.png").resize((150, 150))),
    'scissors': ImageTk.PhotoImage(Image.open("user_scissors.png").resize((150, 150)))
}

# Load computer images
computer_images = {
    'rock': ImageTk.PhotoImage(Image.open("computer_rock.png").resize((150, 150))),
    'paper': ImageTk.PhotoImage(Image.open("computer_paper.png").resize((150, 150))),
    'scissors': ImageTk.PhotoImage(Image.open("computer_scissors.png").resize((150, 150)))
}

# Create labels for images
computer_image = tk.Label(root)
computer_image.pack(pady=10)

user_image = tk.Label(root)
user_image.pack(pady=10)

# Creating buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: play('rock'), width=10, height=2)
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", command=lambda: play('paper'), width=10, height=2)
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play('scissors'), width=10, height=2)
scissors_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
