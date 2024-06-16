import random

#function for generating random numbers between two fixed points
def roll():   
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

value = roll()
print(value)

while True:
    no_of_players = input("Enter the number of players(2-4): ")
    if no_of_players.isdigit():
        no_of_players = int(no_of_players)
        if 2 <= no_of_players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, please try again.")

print(no_of_players)


max_score = 100

players_scores = [0 for _ in range(no_of_players)]

print(players_scores)

while max(players_scores) < max_score:
    for player_index in range(no_of_players):
        print("\nPlayer number ", player_index + 1, "turn has just started.\n")
        print("Your total score is: ", players_scores[player_index], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() == "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1. Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is: ", current_score)

        players_scores[player_index] += current_score
        print("Your total score is: ", players_scores[player_index])

max_score = max(players_scores)
winning_index = players_scores.index(max_score)
print("Player number ", winning_index + 1, "is the winner with a score of: ", max_score)