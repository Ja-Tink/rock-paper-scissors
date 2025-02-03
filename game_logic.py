import random

def fight(user_input):
    #random pick from cpu
    hands = ["rock", "paper", "scissors"]
    cpu_pick = random.choice(hands)

    #game outcomes
    outcomes = {
        "rock" : {"rock" : "tied", "paper" : "lost", "scissors" : "won"},
        "paper" : {"rock" : "won", "paper" : "tied", "scissors" : "lost"},
        "scissors" : {"rock" : "lost", "paper" : "won", "scissors" : "tied"}
    }

    return outcomes[user_input][cpu_pick], cpu_pick