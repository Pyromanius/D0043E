import random


# If correct dice was chosen, then assign a number to it
def assign_no():
    dice = random.randint(1, 6)

    return int(dice)


# Resets the dice to 0
def reset(dice_1, dice_2, dice_3):
    dice_1 = dice_2 = dice_3 = 0
    print("\nNext round!\n")

    return dice_1, dice_2, dice_3


# Check if the sum of the dice is 12 or different
def check_result(dice_1, dice_2, dice_3, win_count, loss_count):
    if dice_1 + dice_2 + dice_3 == 12:
        win_count = win_count + 1
        print_score(dice_1, dice_2, dice_3, win_count, loss_count)
        print("You won!!")
    elif dice_1 + dice_2 + dice_3 > 12:
        loss_count = loss_count + 1
        print_score(dice_1, dice_2, dice_3, win_count, loss_count)
        print("You lost!!")
    else:
        print_score(dice_1, dice_2, dice_3, win_count, loss_count)
        print("You neither won nor lost the game")

    return win_count, loss_count


# Checks if all dice have been rolled
def is_roll_done(dice_1, dice_2, dice_3):
    if dice_1 * dice_2 * dice_3 == 0:
        return False
    else:
        return True


# Print the current win/losses count
def print_score(dice_1, dice_2, dice_3, win_count, loss_count):
    print(f"{dice_1} {dice_2} {dice_3} sum: {dice_1 + dice_2 + dice_3} #win: {win_count} #loss: {loss_count}")


# Prints the start-up screen
def print_welcome():
    print("Welcome to dice game 12. You must roll 1-3 dice and try to get the sum of 12 ...")


# Double-checks choice is a digit and then rolls the dice and assigns a no to it
def attempt_roll(choice, dice_1, dice_2, dice_3):
    if choice.isdigit():
        chosen_dice = int(choice)
    else:
        exit

    if chosen_dice == 1:
        if dice_1 != 0:
            return dice_1, dice_2, dice_3, False
        else:
            dice_1 = assign_no()
    elif chosen_dice == 2:
        if dice_2 != 0:
            return dice_1, dice_2, dice_3, False
        else:
            dice_2 = assign_no()
    elif chosen_dice == 3:
        if dice_3 != 0:
            return dice_1, dice_2, dice_3, False
        else:
            dice_3 = assign_no()

    return dice_1, dice_2, dice_3, True


# Get the user's choice from menu
def get_choice():
    while True:
        choice = input("Enter which dice you want to roll [1,2,3] (exit with q): ")
        if choice != '1' and choice != '2' and choice != '3' and choice != 'q':
            print("Sorry, that is an invalid entry. Try again. Valid entries are 1, 2, 3, and q")
            continue
        else:
            return choice


# Run the actual game routine and initialize the dice
def run_game(win_count, loss_count):
    dice_1 = dice_2 = dice_3 = 0

    while True:
        choice = get_choice()
        is_valid_choice = False
        if choice != 'q':
            dice_1, dice_2, dice_3, is_valid_choice = attempt_roll(choice, dice_1, dice_2, dice_3)
            if is_roll_done(dice_1, dice_2, dice_3):
                win_count, loss_count = check_result(dice_1, dice_2, dice_3, win_count, loss_count)
                dice_1, dice_2, dice_3 = reset(dice_1, dice_2, dice_3)
            else:
                if is_valid_choice:
                    print_score(dice_1, dice_2, dice_3, win_count, loss_count)
                else:
                    print("Sorry, you have already rolled that dice. Try again")
                continue
        elif choice == 'q':
            print(f"#win: {win_count} #loss: {loss_count}\nGame Over!")
            exit()


# Startup. Keeps tracks of wins/Losses
def main():
    win_count = loss_count = 0

    print_welcome()
    run_game(win_count, loss_count)


if __name__ == "__main__":
    main()
