"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""
import random
import tkinter as tk

choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
tie_score = 0

def play_rps(player_choice):
    global player_score, computer_score, tie_score
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        result = "It's a tie!"
        tie_score += 1
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
        player_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    return f"You chose: {player_choice}\nComputer chose: {computer_choice}\n{result}"
def start_gui():
    def on_choice(choice):
        result = play_rps(choice)
        result_label.config(text=result)
        update_scoreboard()

    def on_quit():
        root.destroy()

    def update_scoreboard():
        scoreboard_label.config(text=f"🏆 Player Wins: {player_score}\n🤖 Computer Wins: {computer_score}\n🤝 Ties: {tie_score}")

    root = tk.Tk()
    root.title("Rock Paper Scissors")
    root.configure(bg="#22223b")

    title_label = tk.Label(root, text="Rock Paper Scissors", font=("Helvetica", 20, "bold"), fg="#f2e9e4", bg="#22223b")
    title_label.pack(pady=(20, 10))

    tk.Label(root, text="Choose your move:", font=("Helvetica", 13), fg="#c9ada7", bg="#22223b").pack(pady=5)

    btn_frame = tk.Frame(root, bg="#22223b")
    btn_frame.pack(pady=10)
    btn_style = {"font": ("Helvetica", 13, "bold"), "bg": "#4a4e69", "fg": "#f2e9e4", "activebackground": "#9a8c98", "activeforeground": "#22223b", "width": 12, "height": 2, "bd": 0}
    for choice, emoji in zip(["rock", "paper", "scissors"], ["🪨", "📄", "✂️"]):
        tk.Button(btn_frame, text=f"{emoji} {choice.capitalize()}", command=lambda c=choice: on_choice(c), **btn_style).pack(side=tk.LEFT, padx=10)

    result_label = tk.Label(root, text="", font=("Helvetica", 14), fg="#f2e9e4", bg="#22223b")
    result_label.pack(pady=10)

    scoreboard_frame = tk.Frame(root, bg="#22223b")
    scoreboard_frame.pack(pady=10)
    scoreboard_label = tk.Label(scoreboard_frame, text=f"🏆 Player Wins: {player_score}\n🤖 Computer Wins: {computer_score}\n🤝 Ties: {tie_score}", font=("Helvetica", 13, "bold"), fg="#c9ada7", bg="#22223b", justify="left")
    scoreboard_label.pack()

    quit_btn = tk.Button(root, text="Quit", font=("Helvetica", 12, "bold"), bg="#c9ada7", fg="#22223b", activebackground="#f2e9e4", activeforeground="#22223b", width=10, bd=0, command=on_quit)
    quit_btn.pack(pady=20)

    update_scoreboard()
    root.mainloop()

if __name__ == "__main__":
    start_gui()