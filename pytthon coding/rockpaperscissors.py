import random
while True:
    user_action=input("Enter a choice:rock,paper,scissors:")
    possible_actions=["rock","scissors","paper"]
    computer_action=random.choice(possible_actions)
    print(f"\nYou chose {user_action},computer chose {computer_action}.\n")
    if user_action == computer_action:
        print(f"both players chose {user_action}! It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock beats scissors.you win!")
        else:
            print("paper beats rock.you lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper beats rock.you win!")
        else:
            print("scissors beats paper.you lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors beats paper.you win!")
        else:
            print("rock beats scissors.you lose")
    play_again=input("play again?(y/n):")
    if play_again != "y":
        break