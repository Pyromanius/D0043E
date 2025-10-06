import random

print("Welcome to dice game 12. You must roll 1-3 dice and try to get the sum of 12 ...")

dice_1 = 0
dice_2 = 0
dice_3 = 0
win_count = 0
loss_count = 0

def run_game():
    dice = random.randint(1, 6)
    return int(dice)

while True:
    dice_to_roll = input("Enter which dice you want to roll [1,2,3] (exit with q): ")
    
    if dice_to_roll not in ['1', '2' , '3', 'q']:
        print("Sorry, that is an invalid entry. Try again. Valid entries are 1, 2, 3, and q\n")
        continue
    else:
        if dice_to_roll == '1':
            if dice_1 != 0:
                print("Sorry, you have already rolled that dice. Try again")
                continue
            else:
                dice_1 = run_game()
        elif dice_to_roll == '2':
            if dice_2 != 0:
                print("Sorry, you have already rolled that dice. Try again")
                continue
            else:
                dice_2 = run_game()
        elif dice_to_roll == '3':
            if dice_3 != 0:
                print("Sorry, you have already rolled that dice. Try again")
                continue
            else:
                dice_3 = run_game()
        elif dice_to_roll == 'q':
            print(f"#win: {win_count} #loss: {loss_count}")
            exit()
        
        print(f"{dice_1} {dice_2} {dice_3} sum: {dice_1+dice_2+dice_3} #win: {win_count} #loss: {loss_count}")
        
        if dice_1 != 0 and dice_2 != 0 and dice_3 != 0:
            if dice_1 + dice_2 + dice_3 == 12:
                win_count = win_count + 1
            else:
                loss_count = loss_count + 1
            print(f"{dice_1} {dice_2} {dice_3} sum: {dice_1+dice_2+dice_3} #win: {win_count} #loss: {loss_count}")
            dice_1 = 0
            dice_2 = 0
            dice_3 = 0
