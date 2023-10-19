import random
import re

def dice_roll(dice):

    max_roll_amount = 10
    natural_max_dict = {4:"Nat 4!", 6:"Nat 6!", 8:"Nat 8!", 10:"Nat 10!!", 12:"Nat 12!!!", 20:"NAT 20!!!!!"}
    nat_one = "Natural 1. Big oof."
    flavor_text = ["Bingo-bango, you rolled a",
                   "The gods blessed you today. You roll a",
                   "You feel uncertain about this. You roll a",
                   "You close your eyes and roll a",
                   "You manipulate space and time to roll a"]

    dice_portions = re.search(r'(\d+)d(\d+)', dice)
    if dice_portions == None:
        return print("Inproper input, proper format: 1d6")
    else:
        roll_amount = int(dice_portions[1])
        dice_type = int(dice_portions[2])

    if roll_amount > max_roll_amount:
        raise ValueError('Maximum number of rolls is {}.'.format(max_roll_amount))
    assert dice_type in natural_max_dict.keys(), 'Dice type does not exist. Acceptable dice types are: [4, 6, 8, 10, 12, 20]'

    print(f"\n{roll_amount} roll(s) of a {dice_type}-sided dice")
    print("\nRolling... \n")

    for y in range(roll_amount):
        roll = random.randint(1, dice_type)
        if roll == 1:
            print(nat_one)
        elif roll == dice_type:
            print(natural_max_dict[dice_type])
        else:
            print(f"{random.choice(flavor_text)} {roll}.")
    print("\n")

#manual test
dice_roll("1cd6")
