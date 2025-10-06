import random

def pick_dice():
    while True:
        dice_to_roll = input("Enter which dice you want to roll [1,2,3] (exit with q): ")

        if dice_to_roll not in ['1', '2' , '3', 'q']:
            print("Sorry, that is an invalid entry. Try again. Valid entries are 1, 2, 3, and q")
            continue
        else:
            if dice_to_roll == '1' and dice_1 != 0:
                print("Sorry, you have already rolled that dice. Try again")
                continue
            elif dice_to_roll == '2' and dice_2 != 0:
                print("Sorry, you have already rolled that dice. Try again")
                continue
            elif dice_to_roll == '3' and dice_3 != 0:
                print("Sorry, you have already rolled that dice. Try again")
                continue
            elif dice_to_roll == 'q':
                print(f"#win: {win_count} #loss: {loss_count}")
                exit()
            else:
                return dice_to_roll


def run_game(dice):
    dice = random.randint(1, 6)
    return int(dice)
    

dice_1 = 0
dice_2 = 0
dice_3 = 0
win_count = 0
loss_count = 0

print("Welcome to dice game 12. You must roll 1-3 dice and try to get the sum of 12 ...")

while True:
    dice_to_roll = pick_dice()
    if dice_1 != 0 and dice_2 != 0 and dice_3 != 0:
        if dice_1 + dice_2 + dice_3 == 12:
            win_count = win_count + 1
        else:
            loss_count = loss_count + 1
    if dice_to_roll == '1':
        dice_1 = run_game(dice_1)
        print(f"{dice_1} {dice_2} {dice_3} sum: {dice_1+dice_2+dice_3} #win: {win_count} #loss: {loss_count}")
    elif dice_to_roll == '2':
        dice_2 = run_game(dice_2)
        print(f"{dice_1} {dice_2} {dice_3} sum: {dice_1+dice_2+dice_3} #win: {win_count} #loss: {loss_count}")
    elif dice_to_roll == '3':
        dice_3 = run_game(dice_3)
        print(f"{dice_1} {dice_2} {dice_3} sum: {dice_1+dice_2+dice_3} #win: {win_count} #loss: {loss_count}")
    else:
        continue
